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
