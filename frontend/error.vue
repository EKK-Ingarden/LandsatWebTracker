<template>
  <div class="bg-[url(public/background.png)]" h-screen w-screen bg-cover bg-no-repeat>
    <div h-full w-full flex flex-col items-center justify-center bg-black bg-opacity-85>
      <h1 text-7xl>
        Error {{ error.statusCode }}
      </h1>
      <p mt-4 text-2xl text-gray-400>
        {{ error.statusMessage }}
      </p>
      <Button variant="grayDefault" size="lg" text-size="base" mt-6>
        <NuxtLink to="/">
          Go back home
        </NuxtLink>
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { NuxtError } from "#app";

// eslint-disable-next-line unused-imports/no-unused-vars
const props = defineProps({
  error: Object as () => NuxtError
});

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
</script>
