<template>
  <div>
    <Navbar sticky top-0 />
    <slot />
  </div>
</template>

<script setup lang="ts">
useHead({
  meta: [
    { charset: "utf-8" },
    { name: "viewport", content: "width=device-width, initial-scale=1" },
    { property: "og:image", content: "/favicon.ico" }
  ],
  link: [
    { rel: "icon", href: "/favicon.ico" }
  ],
  htmlAttrs: {
    lang: "en"
  },
  bodyAttrs: {
    class: "dark dark-mode inter"
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

<style lang="scss">
@font-face {
    font-family: "inter";
    src: url("assets/fonts/Inter.ttf") format("truetype");
    font-weight: normal;
    font-style: normal;
}

.inter{
  font-family: inter, serif;
}
</style>
