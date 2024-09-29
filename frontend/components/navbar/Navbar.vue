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
        <img src="~/assets/img/options.svg">
      </Button>
      <div md="flex flex-row gap-5 items-center" hidden>
        <NavbarLink url="#">
          Landsat Locator
        </NavbarLink>
        <NavbarLink url="#">
          Search for data
        </NavbarLink>
        <NavbarLink url="#">
          About us
        </NavbarLink>
        <img h="5vh" alt="User profile picture" src="~/assets/img/placeholder_pfp.png" v-if="isUserLoggedIn" rounded-full>
        <NavbarLink url="/register" v-if="!isUserLoggedIn">
          Sign in
        </NavbarLink>
      </div>
    </div>
    <div h-screen w-screen bg-gray-900 fixed md="hidden" top="10vh"
         :class="isExpanded ? '' : 'translate-x-100vw'" duration-300 overflow-auto
    >
      <div flex flex-col gap-5 text-2xl items-center text-center>
        <NuxtLink to="#" border-y-2 py-4 border-gray-500 w-full>
          Landsat Locator
        </NuxtLink>
        <NuxtLink to="#" border-b-2 pb-4 border-gray-500 w-full>
          Search for data
        </NuxtLink>
        <NuxtLink to="#" border-b-2 pb-4 border-gray-500 w-full>
          About us
        </NuxtLink>
        <img h="5vh" alt="User profile picture" src="~/assets/img/placeholder_pfp.png" v-if="isUserLoggedIn" rounded-full>
        <NuxtLink to="/register" v-if="!isUserLoggedIn" border-b-2 pb-4 border-gray-500 w-full>
          Sign in
        </NuxtLink>
        <!-- maybe footer here? -->
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const isExpanded = ref(false);

const isUserLoggedIn = ref(false);
const user = useSupabaseUser();

watch (user, () => {
  if (user.id) {
    isUserLoggedIn.value = true;
  }
});
</script>
