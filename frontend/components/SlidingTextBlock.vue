<template>
  <div text-left w-30vw md="h-10vh mt-10vh" h-5vh mt-15vh bg-none>
    <h2 md="text-4xl" text-xl font-bold>
      {{ props.header }}
    </h2>
    <p ml-3 md="text-base" text-sm>
      <slot />
    </p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ header?: string }>();
</script>
