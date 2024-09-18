<template>
  <Map @map-click="mapClick" />
</template>

<script setup>
function mapClick(e) {
  console.log("Clicked at", e);
}
</script>
