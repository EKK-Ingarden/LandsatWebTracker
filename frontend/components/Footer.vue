<template>
  <div h-50 w-screen flex flex-col items-center justify-center md="gap-10" gap-5 bg-black my-10>
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
    <div w="70%" md="text-base" text-sm text-center>
      Made by EKK Ingarden for Nasa Space Apps 2024. Website is
      <NuxtLink to="https://github.com/EKK-Ingarden/LandsatWebTracker">
        open source
      </NuxtLink>
    </div>
  </div>
</template>
