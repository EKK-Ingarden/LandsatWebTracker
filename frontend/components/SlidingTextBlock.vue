<template>
  <div
    md="mt-20vh w-30vw" mt-20vh h-5vh w-70vw bg-none
    :class="props.isRight ? 'mr-10vw ml-auto text-right' : 'ml-10vw mr-auto text-left'"
  >
    <h2 md="text-4xl" text-2xl font-bold>
      {{ props.header }}
    </h2>
    <p text-base>
      <slot />
    </p>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  isRight?: boolean
  header?: string
}>();
</script>
