<template h-screen>
  <div class="flex-col-reverse md:flex-row" flex full-height-without-header>
    <div class="p-4 2xl:w-1/4 lg:w-2/4 md:w-3/5 xl:w-2/5">
      <div flex flex-col>
        <p text-xl>
          Enter a date
        </p>
        <div mt-4 flex flex-row gap-4>
          <div flex flex-col class="w-1/2">
            <p text-xs>
              Start
            </p>
            <DatePicker v-model="dateFrom" placeholder="Start" />
          </div>
          <div flex flex-col class="w-1/2">
            <p text-xs>
              End
            </p>
            <DatePicker v-model="dateTo" placeholder="End" />
          </div>
        </div>
      </div>
      <div mt-10 flex>
        <p>
          Max Cloud Coverage
        </p>
        <div flex-1 text-right>
          <p>
            {{ maxCloudCover[0] }}%
          </p>
        </div>
      </div>
      <Slider v-model="maxCloudCover" mt-3 :default-value="20" :max="100" :step="1" />

      <div overflow-auto h="5/7" p-5>
        <div v-for="(polygon, index) in polygons" :key="index" @mouseover="logPolygon(polygon)" @mouseleave="selectedPolygon = undefined" @click="showPolygon(polygon)">
          <div mt-5 border border-2 border-white border-rounded-md>
            <button h-full w-full>
              <div flex>
                <div mx-4 mb-4 mt-4 flex-shrink-0>
                  <img h-25 border-rd border-solid :src="polygon.rendered_preview" :class="{ 'bg-gray-600': polygon === selectedPolygonData }">
                </div>
                <div mt-8 flex flex-col overflow-auto>
                  <span break-words text-sm>{{ polygon.id }}</span>
                  <div mt-8 flex gap-2>
                    <span text-xs color="#a3a3a3">{{ formatDate(polygon.datetime) }}</span>
                    <span text-right text-xs color="#a3a3a3">{{ roundToThreeDigits(polygon.eo_cloud_cover) }} %</span>
                  </div>
                </div>
              </div>
            </button>
          </div>
        </div>
        <div v-if="polygons.length === 0">
          <p>No data</p>
          <p>Try selecting new point on map!</p>
          <span v-if="error" text-red>{{ error }}</span>
        </div>
      </div>
      <div mt-5 flex justify-center>
        <GenerateRaportDialog v-if="selectedPolygonData" :scene-id="selectedPolygonData.id" mb-5 />
      </div>
    </div>
    <div class="w-full md:w-3/4">
      <Map :marker="marker" :selected-polygon="selectedPolygon" :tile-layer-overlay="tileLayer" @map-click="updateMarkerPosition" @search-location="search" />
    </div>
  </div>
</template>

<script setup lang="ts">
import type L from "leaflet";
import { LatLng } from "leaflet";
import type { DateValue } from "@internationalized/date";
import { Slider } from "@/components/ui/slider";

const marker = ref<LatLng | undefined>(undefined);
const tileLayer = ref<{
  url: string
  bounds: L.LatLngBoundsLiteral
} | undefined>(undefined);

const polygons = ref<Polygon[]>([]);
const selectedPolygon = ref<LatLng[] | undefined>(undefined);
const selectedPolygonData = ref<Polygon | undefined>(undefined);

const dateFrom = ref<DateValue | null>(null); // Parent holds the selected date
const dateTo = ref<DateValue | null>(null); // Parent holds the selected date
const maxCloudCover = ref([20]);

const error = ref<string | undefined>(undefined);

interface Polygon {
  platform: string
  id: string
  datetime: string
  eo_cloud_cover: number
  wrs_coordinates: {
    wrs_path: number
    wrs_row: number
  }
  rendered_preview: string
  mosaic_endpoints: {
    natural_color: string
    color_infrared: string
    atmospheric_penetration: string
  }
  polygon: {
    coordinates: {
      latitude: number
      longitude: number
    }[]
  }
}

async function updateMarkerPosition(latlng: LatLng) {
  error.value = undefined;
  if (!dateFrom.value || !dateTo.value) {
    error.value = "Please provide all data";
    return;
  }

  const { data } = await useApi("/landsat/search", {
    query: {
      latitude: latlng.lat,
      longitude: latlng.lng,
      start_date: dateFrom.value!.toString(),
      end_date: dateTo.value!.toString(),
      max_cloud_cover: maxCloudCover.value[0] / 100
    }
  });

  if (data.value != null) {
    polygons.value = data.value;
  }
}

function logPolygon(polygon: Polygon) {
  // console.log(polygon);
  const coordinates = polygon.polygon.coordinates;
  const new_polygon = [];
  for (let i = 0; i < coordinates.length; i++) {
    new_polygon.push(new LatLng(coordinates[i].latitude, coordinates[i].longitude));
  }
  selectedPolygon.value = new_polygon;
  console.log(selectedPolygon.value);
}

async function showPolygon(polygon: Polygon) {
  const sceneId = polygon.id;

  selectedPolygonData.value = polygon;

  const { data } = await useApi("/landsat/mosaic", {
    query: {
      scene_id: sceneId.toString(),
      collection_id: "landsat-c2-l2",
      mosaic_type: "0"
    }
  });
  let url: string = data.value!.toString();
  url = url.replace("%7Bz%7D", "{z}");
  url = url.replace("%7Bx%7D", "{x}");
  url = url.replace("%7By%7D", "{y}");
  tileLayer.value = {
    url,
    bounds: polygon.polygon.coordinates.map(({ latitude, longitude }) => [latitude, longitude] as [number, number])
  };
  console.log(url);
}

function search(data: any) {
  updateMarkerPosition(new LatLng(data.location.y, data.location.x));
}

function formatDate(datetime: string): string {
  const date = new Date(datetime);
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function roundToThreeDigits(num: number): number {
  return Math.round(num * 1000) / 1000;
}
</script>
