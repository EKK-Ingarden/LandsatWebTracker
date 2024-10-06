<template>
  <div h-screen w-screen>
    <LMap
      ref="map"
      :zoom="zoom"
      :center="currentPosition"
      :use-global-leaflet="true"
      @click="$emit('mapClick', $event.latlng)"
      @ready="mapReady"
    >
      <LTileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
        layer-type="base"
        name="OpenStreetMap"
      />

      <LTileLayer
        url="https://planetarycomputer.microsoft.com/api/data/v1/mosaic/41a94eed11ae5df9b6a03cfd5806c0c0/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=nir08&assets=red&assets=green&color_formula=gamma+RGB+2.7%2C+saturation+1.5%2C+sigmoidal+RGB+15+0.55&nodata=0&collection=landsat-c2-l2&format=png"
        layer-type="base"
        name="Landsat"
        :min-zoom="8"
      />

      <LPolygon
        v-if="selectedPolygon"
        :lat-lngs="selectedPolygon"
        color="#41b782"
        :fill="true"
        :fill-opacity="0.5"
        fill-color="#41b782"
      />

      <LControl position="topLeft" absolute left="0" top="50">
        <div w-13 border-2 border-gray-500 rounded-r-md border-l-none>
          <Input v-model="inputCoordinates.lat" bg-color="white" border-setup="borderB2Gray500" rounded="topRight" text-black placeholder="Lat" />
          <Input v-model="inputCoordinates.lng" bg-color="white" border-setup="borderB2Gray500" rounded="none" text-black placeholder="Lng" />
          <button
            h-9 w-full flex items-center justify-center rounded-br-md bg-white text-black
            @click="coordinatesSearch(inputCoordinates.lat, inputCoordinates.lng)"
          >
            <img text-xl class="i-material-symbols:search">
          </button>
        </div>
        <p v-if="error" w-50 pl-2 h-auto mt-5 rounded-r-md border-2 border-l-none border-gray-500 text-base bg-white text-red>{{ error ? error : "" }}</p>
      </LControl>

      <LImageOverlay v-if="imageOverlay" :url="imageOverlay.url" :bounds="imageOverlay.bounds" />

      <LMarker v-model="marker" :lat-lng="marker" />
    </LMap>
  </div>
</template>

<script setup lang="ts">
import type { LatLng, Map } from "leaflet";
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import "leaflet-geosearch/dist/geosearch.css";
import { LMarker } from "#components";

defineProps<{
  selectedPolygon?: LatLng[]
  imageOverlay?: {
    url: string
    bounds: L.LatLngBoundsLiteral
  }
}>();

defineEmits<{
  (event: "mapClick", latlng: LatLng): void
}>();

const marker = ref<LatLng | undefined>(undefined);

const map = ref(null);
const inputCoordinates = ref<{
  lat: string
  lng: string
}>;
const zoom = ref(6);
const error = ref<string | false>(false);
const currentPosition = ref<[number, number]>([50.9, 15.73]);

function mapReady(map: Map) {
  const search: any = new (GeoSearchControl as any)({
    provider: new OpenStreetMapProvider()
  });
  map.addControl(search);
}

function coordinatesSearch(lat, lng) {
  let newLatLng;

  try {
    newLatLng = L.latLng(Number(lat), Number(lng));
  } catch {
    error.value = "Excepted number, got string";
    console.log(error.value);
    return;
  }

  if (Number(lat) > 90 || Number(lat) < -90) {
    error.value = "Latitude value out of range <-90, 90>";
    console.log(error.value);
    return;
  } else if (Number(lng) > 180 || Number(lng) < -180) {
    error.value = "Longitude value out of range <-180, 180>";
    console.log(error.value);
    return;
  }

  marker.value = newLatLng;
  currentPosition.value = [Number(lat), Number(lng)];
}
</script>
