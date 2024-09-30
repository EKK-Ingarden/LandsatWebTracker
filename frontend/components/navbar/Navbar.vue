<template>
  <div h="10vh" w-full bg-transparent from-transparent to-black bg-gradient-to-t to="50%">
    <div mx-5 h-full flex items-center justify-between>
      <NuxtLink to="/" flex items-center gap-3>
        <img alt="LandsatWebTracker logo" src="~/assets/img/logo.svg" h="5vh">
        <p font-700>
          Landsat Web Tracker
        </p>
      </NuxtLink>
      <Button size="icon" variant="ghost" md="hidden" @click="isExpanded = !isExpanded">
        <span class="i-ci:hamburger" text-2xl />
      </Button>
      <NavbarLinks />
    </div>
    <div
      md="hidden" top="10vh" fixed h-screen w-screen
      :class="isExpanded ? '' : 'translate-x-100vw'" overflow-auto bg-gray-900 duration-300
    >
      <NavbarLinks variant="sidebar" links-variant="sidebar" first-link-variant="firstSidebar" />
    </div>
  </div>
</template>

<script setup lang="ts">
const isExpanded = ref(false);
</script>
