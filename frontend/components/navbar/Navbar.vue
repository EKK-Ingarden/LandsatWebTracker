<template>
  <div z-2 h-20 w-full bg-black>
    <div mx-5 h-full flex items-center justify-between>
      <NuxtLink to="/" flex items-center gap-3>
        <img alt="LandsatWebTracker logo" src="~/assets/img/logo.svg" h-11>
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
      :class="isExpanded ? '' : 'translate-x-100vw'" overflow-auto bg-black duration-300
    >
      <NavbarLinks variant="sidebar" links-variant="sidebar" first-link-variant="firstSidebar" />
    </div>
  </div>
</template>

<script setup lang="ts">
const isExpanded = ref(false);
const router = useRouter();

watch(() => router.currentRoute.value, () => {
  isExpanded.value = false;
});
</script>
