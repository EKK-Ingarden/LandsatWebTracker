<template>
  <div md="h-80 py-15" h-90 w-screen flex flex-col items-center gap-10 bg-black pb-20 pt-25>
    <img src="~/assets/img/logo.svg" h-14>
    <div flex md="gap-15" gap-10 text-xs>
      <NuxtLink to="/">
        Home
      </NuxtLink>
      <NuxtLink to="#">
        Our Team
      </NuxtLink>
      <NuxtLink to="#">
        Contact
      </NuxtLink>
      <NuxtLink to="#">
        FAQ
      </NuxtLink>
    </div>
    <hr w="80%" b-1 border-gray-700>
    <div>
      Made by EKK Ingarden for Nasa Space Apps 2024. Website is
      <NuxtLink to="https://github.com/EKK-Ingarden/LandsatWebTracker">
        open source
      </NuxtLink>
    </div>
  </div>
</template>
