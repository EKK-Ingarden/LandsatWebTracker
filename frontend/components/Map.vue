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

      <LImageOverlay v-if="imageOverlay" :url="imageOverlay.url" :bounds="imageOverlay.bounds" />

      <LMarker :lat-lng="[50.90473781103003, 15.731811290627371]">
        <LTooltip> Best place on Earth! </LTooltip>
      </LMarker>
    </LMap>
  </div>
</template>

<script setup lang="ts">
import type { LatLng, Map } from "leaflet";
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import "leaflet-geosearch/dist/geosearch.css";

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

const map = ref(null);
const currentPosition = ref<[number, number]>([50.9, 15.73]);
const zoom = ref(6);

function mapReady(map: Map) {
  const search: any = new (GeoSearchControl as any)({
    provider: new OpenStreetMapProvider()
  });
  map.addControl(search);
}
</script>
