<template>
  <svg class="arch" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20" preserveAspectRatio="none">
    <path d="M 0 20 Q 50 15 100 20" stroke="url(#grad1)" :stroke-width="strokeWidth" fill="transparent" />
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#6983EA; stop-opacity:1" />
        <stop offset="25%" style="stop-color:#5BC0BE; stop-opacity:1" />
        <stop offset="100%" style="stop-color:#9EF01A; stop-opacity:1" />
      </linearGradient>
    </defs>
  </svg>
</template>

<script setup lang="ts">
defineProps<{ strokeWidth: number }>();
</script>
