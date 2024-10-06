<template>
  <div class="w-full p-10">
    <Skeleton v-if="data === null" />
    <div v-else>
      <h1 class="text-2xl">
        {{ sceneId }}
      </h1>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Skeleton } from "@/components/ui/skeleton";

const props = defineProps<{
  sceneId: string
}>();

const { data } = useApi("/landsat/generate_report", {
  query: {
    scene_id: props.sceneId
  }
});
</script>
