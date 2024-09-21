<template>
  <div h-full>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { useColorMode } from "@vueuse/core";

useColorMode().preference = "dark";

useHead({
  meta: [
    { charset: "utf-8" },
    { name: "viewport", content: "width=device-width, initial-scale=1" }
  ],
  link: [
    { rel: "icon", href: "/favicon.ico" }
  ],
  htmlAttrs: {
    lang: "en"
  }
});

const title = "Landsat Web Tracker";
const description = "Project made by EKK Ingarden for Nasa Space Apps 2024.";

useSeoMeta({
  title,
  description,
  ogTitle: title,
  ogDescription: description
});
</script>
