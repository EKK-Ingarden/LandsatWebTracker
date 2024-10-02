<template>
  <NuxtLayout>
    <div class="bg-[url(assets/img/background.png)]" max-w-screen bg-cover bg-no-repeat full-height-without-header>
      <div h-full w-full flex flex-col items-center justify-center bg-black bg-opacity-85>
        <h1 text-7xl>
          Error {{ error?.statusCode }}
        </h1>
        <p mt-4 text-2xl text-gray-400>
          {{ error?.statusMessage }}
        </p>
        <Button variant="grayDefault" size="lg" text-size="base" mt-6>
          <NuxtLink to="/">
            Go back home
          </NuxtLink>
        </Button>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import type { NuxtError } from "#app";

defineProps({
  error: Object as () => NuxtError
});
</script>
