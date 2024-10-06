<template>
  <div>
    <h1>Raport</h1>
    <p>id: {{ route.params.id }}</p>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();

const { data, error}

// When accessing /posts/1, route.params.id will be 1
console.log(route.params.id)
</script>
