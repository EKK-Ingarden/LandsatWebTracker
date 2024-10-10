<template h-screen>
  <div flex full-height-without-header>
    <div class="w-1/4 p-4">
      <div h="1/4" flex flex-col overflow-auto p-5>
        <div flex items-center justify-around border-b-2 border-gray-800 rounded-t-md bg-gray-900 py-2>
          <p>Path</p>
          <p>Row</p>
        </div>
        <button
          v-for="(polygon, index) in polygons" :key="index" flex
          items-center justify-around border-b-2 border-gray-900 py-2 hover="bg-gray-600" :class="{ 'bg-gray-600': polygon === selectedPolygonData }" @click="selectPolygon(polygon)"
        >
          <p>{{ polygon.coordinates.wrs_path }}</p>
          <p>{{ polygon.coordinates.wrs_row }}</p>
        </button>
      </div>
      <div h="3/5" flex flex-col overflow-auto p-5>
        <div flex items-center justify-around border-b-2 border-gray-800 rounded-t-md bg-gray-900 py-2>
          <p>Landsat version</p>
          <p>Reminder date</p>
        </div>
        <button
          v-for="(aquasition, index) in aquasitions" :key="index" flex
          items-center justify-around border-b-2 border-gray-900 py-2 hover="bg-gray-600" :class="{ 'bg-gray-600': aquasition === selectedAcquisition }" @click="selectAcquisition(aquasition)"
        >
          <p>{{ aquasition[0] }}</p>
          <p>{{ aquasition[1] }}</p>
        </button>
      </div>
      <WatchMyPixelDialog v-if="selectedAcquisition" my-5 :selected-acquisition="selectedAcquisition" :polygon-data="selectedPolygonData" :selected-position="selectedPosition" w-full p-5 />
    </div>
    <div class="w-3/4">
      <Map :selected-polygon="selectedPolygon" :tile-layer-overlay="tileLayer" @updated-marker-position="updateMarkerPosition" @search-location="search" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { LatLng } from "leaflet";
import WatchMyPixelDialog from "~/components/WatchMyPixelDialog.vue";

const tileLayer = ref<{
  url: string
  bounds: L.LatLngBoundsLiteral
} | undefined>(undefined);

const polygons = ref<Polygon[]>([]);
const selectedPolygon = ref<LatLng[] | undefined>(undefined);
const selectedPolygonData = ref<any | undefined>(undefined);
const selectedAcquisition = ref<any | undefined>(undefined);
const selectedPosition = ref<LatLng | undefined>(undefined);
// todo: typescript
const aquasitions = ref<any | undefined>(undefined);

function selectAcquisition(aquasition: any) {
  selectedAcquisition.value = aquasition;
}

export interface Polygon {
  coordinates: {
    path: number
    row: number
  }
  mode: "A" | "D"
  polygon: {
    coordinates: {
      lat: number
      lon: number
    }[]
  }
}

async function updateMarkerPosition(latlng: LatLng) {
  selectedPosition.value = latlng;

  aquasitions.value = [];
  selectedAcquisition.value = undefined;

  const { data } = await useApi("/landsat/get_scene", {
    query: {
      lat: latlng.lat,
      lng: latlng.lng,
      mode: "D"
    }
  });

  if (data.value != null) {
    polygons.value = data.value;
  }
}

async function selectPolygon(polygon: Polygon) {
  // console.log(polygon);
  const coordinates = polygon.polygon.coordinates;
  const new_polygon = [];
  for (let i = 0; i < coordinates.length; i++) {
    new_polygon.push(new LatLng(coordinates[i].lat, coordinates[i].lon));
  }
  selectedPolygon.value = new_polygon;
  selectedPolygonData.value = polygon;

  const today = new Date();
  const { data } = await useApi("/landsat/get_acquisitions", {
    query: {
      path: polygon.coordinates.path,
      from_date: today.toISOString().split("T")[0]
    }
  });

  if (data.value != null) {
    console.log(data.value);
    aquasitions.value = data.value;
  }
}

function search(data: any) {
  updateMarkerPosition(new LatLng(data.location.y, data.location.x));
}
</script>
