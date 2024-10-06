<template>
  <div>
    <h1>Raport</h1>
    <p>id: {{ route.params.id }}</p>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();


const { data, error } = useApi("/report/get_report", {
  query: {
    scene_id: route.params.id.toString()
  }
});

// data.value.
console.log(data, error)

</script>
