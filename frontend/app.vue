<template>
  <div>
    <h1 text-green>
      LandsatWebTracker
    </h1>

    <Button @click="count++">
      count is {{ count }}
    </Button>
  </div>
</template>

<script setup lang="ts">
import { Button } from "~/components/ui/button";

const count = ref(0);
</script>
