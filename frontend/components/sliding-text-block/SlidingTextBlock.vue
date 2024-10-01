<template>
  <div
    :class="cn(slidingTextBlockVariants({ direction }), props.class)"
  >
    <h2 md="text-4xl" text-xl font-bold>
      {{ props.header }}
    </h2>
    <p ml-3 md="text-base" text-sm>
      <slot />
    </p>
  </div>
</template>

<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { type SlidingTextBlockVariants, slidingTextBlockVariants } from ".";

interface Props {
  direction?: SlidingTextBlockVariants["direction"]
  class?: HTMLAttributes["class"]
  header?: string
}

const props = defineProps<Props>();
</script>
