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
    <div flex md="gap-10" gap-5 text-2xl>
      <NuxtLink to="https://github.com/EKK-Ingarden/LandsatWebTracker">
        <p class="i-lucide:github" />
      </NuxtLink>
      <NuxtLink to="#">
        <p class="i-ci:mail" />
      </NuxtLink>
    </div>
  </div>
</template>
