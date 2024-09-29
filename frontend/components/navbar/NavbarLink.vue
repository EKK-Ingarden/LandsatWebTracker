<template>
  <NuxtLink :to="url" class="relative text-center text-white no-underline before:absolute before:bottom-0 before:left-0 before:block before:h-[2px] before:w-full before:scale-x-0 before:bg-white before:transition-transform before:duration-200 before:ease-linear before:content-[''] hover:before:scale-x-100">
    <slot />
  </NuxtLink>
</template>

<script setup lang="ts">
defineProps<{ url: string }>();
</script>
