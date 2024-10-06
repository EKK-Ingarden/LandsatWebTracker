<template h-screen>
  <div flex full-height-without-header>
    <div class="w-1/4 p-4">
      <div flex flex-col items-center justify-center>
        <p font-size="0.90rem">
          Enter Date
        </p>
        <p font-size="0.75rem" mt-2>
          Start
        </p>
        <DatePicker v-model="dateFrom" placeholder="Start" mt-4 text-align-center />
        <p font-size="0.75rem" mt-2>
          End
        </p>
        <DatePicker v-model="dateTo" placeholder="End" />
      </div>
      <div mt-3 flex justify-center>
        <p>
          Max Cloud Coverage {{ maxCloudCover[0] }}%
        </p>
      </div>
      <Slider v-model="maxCloudCover" mt-3 :default-value="20" :max="100" :step="1" />

      <div overflow-auto h="5/7" p-5>
        <div v-for="(polygon, index) in polygons" :key="index" bg-white @mouseover="logPolygon(polygon)" @click="showPolygon(polygon)">
          <button>
            <img h-20 :src="polygon.rendered_preview">
            <span font-size="0.75rem">{{ polygon.id }}</span><br><br>
            <div flex gap-2>
              <span font-size="0.5rem" color="#a3a3a3">{{ polygon.datetime }}</span>
              <span font-size="0.5rem" color="#a3a3a3">{{ polygon.eo_cloud_cover }}</span>
            </div>
          </button>
        </div>
        <div v-if="polygons.length === 0">
          <p>No data</p>
          <p>Try selecting new point on map!</p>
          <span v-if="error" text-red>{{ error }}</span>
        </div>
      </div>
      <!--      todo: get which raport is selected -->
      <GenerateRaportDialog v-if="polygons.length !== 0" mb-5 />
    </div>
    <div class="w-3/4">
      <Map :marker="marker" :selected-polygon="selectedPolygon" :tile-layer-overlay="tileLayer" @map-click="updateMarkerPosition" @search-location="search" />
    </div>
  </div>
</template>

<script setup lang="ts">
import L, { LatLng } from "leaflet";
import type { DateValue } from "@internationalized/date";
import { Slider } from "@/components/ui/slider";

const marker = ref<LatLng | undefined>(undefined);
const tileLayer = ref<{
  url: string
  bounds: L.LatLngBoundsLiteral
} | undefined>(undefined);

const polygons = ref<Polygon[]>([]);
const selectedPolygon = ref<LatLng[] | undefined>(undefined);

const dateFrom = ref<DateValue | null>(null); // Parent holds the selected date
const dateTo = ref<DateValue | null>(null); // Parent holds the selected date
const maxCloudCover = ref([20]);

const error = ref<string | undefined>(undefined);
const map = ref<any | undefined>(undefined);

interface Polygon {
  id: string
  datetime: string
  eo_cloud_cover: number
  wrs_coordinates: {
    path: number
    row: number
  }
  rendered_preview: string
  mosaic_endpoints: {
    natural_color: string
    color_infrared: string
    atmospheric_penetration: string
  }
  polygon: {
    coordinates: {
      lat: number
      lon: number
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
      max_cloud_cover: maxCloudCover.value / 100
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
    new_polygon.push(new LatLng(coordinates[i].lat, coordinates[i].lon));
  }
  selectedPolygon.value = new_polygon;
  console.log(selectedPolygon.value);
}

async function showPolygon(polygon: Polygon) {
  const sceneId = polygon.id;

  L.map("map").setView([polygon.polygon.coordinates[0].lat, polygon.polygon.coordinates[0].lon], 6);

  map.value.curentPosition = [polygon.polygon.coordinates[0].lat, polygon.polygon.coordinates[0].lon];

  // marker.value

  // todo: swithcc to useApi
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
    bounds: polygon.polygon.coordinates.map(({ lat, lon }) => [lat, lon] as [number, number])
  };
  console.log(url);
}

function search(data: any) {
  updateMarkerPosition(new LatLng(data.location.y, data.location.x));
}
</script>
