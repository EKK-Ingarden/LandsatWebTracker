<template>
  <div class="bg-[url(public/background.png)]" h-full bg-cover bg-no-repeat>
    <div bg-black bg-opacity-85>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
    </div>
  </div>
</template>

<script setup lang="ts">
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
  },
  bodyAttrs: {
    class: "dark dark-mode"
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
