<template>
  <Map :selected-polygon="polygon" :image-overlay="image" @map-click="mapClick" />
</template>

<script setup lang="ts">
import { LatLng } from "leaflet";

const polygon: LatLng[] = [new LatLng(0, 0), new LatLng(1, 1), new LatLng(5000, 500)];
const image = {
  url: "https://www.printablee.com/postpic/2011/06/blank-100-square-grid-paper_405041.jpg",
  bounds: [[-20, -15], [10, 15]] as L.LatLngBoundsLiteral
};

function mapClick(e) {
  console.log("Clicked at", e);
}
</script>
