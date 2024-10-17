<template>
  <div text-black full-height-without-header>
    <LMap
      ref="map"
      z-0
      :zoom="zoom"
      :center="currentPosition"
      :use-global-leaflet="true"
      @click="mapClick"
      @ready="mapReady"
    >
      <LTileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors"
        layer-type="base"
        name="OpenStreetMap"
      />

      <LPolygon
        v-if="selectedPolygon"
        :lat-lngs="selectedPolygon"
        color="#41b782"
        :fill="true"
        :fill-opacity="0.1"
        fill-color="#41b782"
      />

      <LImageOverlay v-if="imageOverlay" :url="imageOverlay.url" :bounds="imageOverlay.bounds" />
      <LTileLayer v-if="tileLayerOverlay" :url="tileLayerOverlay.url" :bounds="tileLayerOverlay.bounds" />

      <LMarker v-model="marker" :lat-lng="marker" />
    </LMap>
  </div>
</template>

<script setup lang="ts">
import { LatLng, type Map } from "leaflet";
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import "leaflet-geosearch/dist/geosearch.css";
import { LMarker } from "#components";

defineProps<{
  selectedPolygon?: LatLng[]
  imageOverlay?: {
    url: string
    bounds: L.LatLngBoundsLiteral
  }
  tileLayerOverlay?: {
    url: string
    bounds: L.LatLngBoundsLiteral
  }
}>();

const emit = defineEmits<{
  (event: "mapClick", latlng: LatLng): void
  (event: "updatedMarkerPosition", data: any): void
}>();

const marker = ref<LatLng | undefined>(undefined);

const map = ref(null);
const zoom = ref(6);
const currentPosition = ref<[number, number]>([50.9, 15.73]);

function mapClick(event: any) {
  emit("mapClick", event.latlng);
  emit("updatedMarkerPosition", event.latlng);
  marker.value = event.latlng;
}

function mapReady(map: Map) {
  const search: any = new (GeoSearchControl as any)({
    provider: new OpenStreetMapProvider()
  });
  map.addControl(search);
  map.on("geosearch/showlocation", (event: any) => {
    emit("updatedMarkerPosition", event);
    marker.value = new LatLng(event.marker.location.y, event.marker.location.x);
  });
}
</script>
