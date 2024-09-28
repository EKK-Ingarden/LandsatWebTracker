<template>
  <Map :selected-polygon="polygon" :image-overlay="image" @map-click="mapClick" />
</template>

<script setup lang="ts">
import { LatLng } from "leaflet";

const polygon: LatLng[] = [new LatLng(51.342800656448965, 14.370216927521078), new LatLng(49.64140114815556, 13.69019407190872), new LatLng(49.20099186105633, 16.184743219759543), new LatLng(50.89540578366285, 16.955436093090825), new LatLng(51.342800656448965, 14.370216927521078)];
const image = {
  url: "https://planetarycomputer.microsoft.com/api/data/v1/item/preview.png?collection=landsat-c2-l2&item=LC09_L2SP_191025_20240919_02_T1&assets=red&assets=green&assets=blue&color_formula=gamma+RGB+2.7%2C+saturation+1.5%2C+sigmoidal+RGB+15+0.55&format=png",
  bounds: polygon.map(({ lat, lng }) => [lat, lng]) as L.LatLngBoundsLiteral
};

function mapClick(location: LatLng) {
  console.log("Clicked at", location);
}
</script>
