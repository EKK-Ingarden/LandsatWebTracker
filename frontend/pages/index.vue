<template>
  <div h-screen flex items-center justify-center>
    <div mx-auto max-w-xl text-center>
      <div text-5xl>
        Landsat Web Tracker
      </div>
      <div mt-4 text-lg text-gray-500>
        Work in progress! View source code <a font-bold underline href="https://github.com/EKK-Ingarden/LandsatWebTracker">here</a><br>
        Project made by EKK Ingarden for Nasa Space Apps 2024.
      </div>
      <li v-for="item in data" :key="item.username">
        Email: {{ item.email }} Username: {{ item.username }}
      </li>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data } = await useApi("/get_users");
</script>
