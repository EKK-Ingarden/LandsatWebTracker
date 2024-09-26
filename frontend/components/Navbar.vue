<template>
  <div w-full h="10vh" bg-black>
    <div flex justify-between mx-5 items-center h-full>
      <NuxtLink to="https://github.com/EKK-Ingarden/LandsatWebTracker" flex items-center gap-3>
        <img src="/assets/img/logo.png" w-auto h="5vh">
        <p font-700>Landsat Web Tracker</p>
      </NuxtLink>
      <ul flex gap-5>
        <li>
          <NuxtLink to="#">
            Landsat Locator
          </NuxtLink>
        </li>
        <li>
          <NuxtLink to="#">
            Search for data
          </NuxtLink>
        </li>
        <li>
          <NuxtLink to="#">
            About us
          </NuxtLink>
        </li>
        <li>
          <NuxtLink to="/register">
            Sign in
          </NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
</script>
