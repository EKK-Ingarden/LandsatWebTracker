<template>
  <span>Redirecting...</span>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "no-scrollable"
});

const user = useSupabaseUser();

watch(user, () => {
  if (user.value) {
    return navigateTo("/panel");
  }
}, { immediate: true });
</script>
