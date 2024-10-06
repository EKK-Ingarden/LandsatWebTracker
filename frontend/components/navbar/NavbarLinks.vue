<template>
  <div
    :class="cn(navbarLinksVariants({ variant }), props.class)"
  >
    <NavbarLink url="/faq" :variant="firstLinkVariant">
      FAQ
    </NavbarLink><NavbarLink url="/how-does-it-work" :variant="linksVariant">
      How does it work?
    </NavbarLink>
    <NavbarLink url="#" :variant="linksVariant">
      Landsat Locator
    </NavbarLink>
    <NavbarLink url="#" :variant="linksVariant">
      Search for data
    </NavbarLink>
    <NavbarLink url="/map" :variant="linksVariant">
      Map
    </NavbarLink>
    <NuxtLink v-if="user" to="/panel">
      <img
        h-9 aria-label="User profile picture" alt="" rounded-full
        :src="user?.user_metadata.avatar_url"
        :class="user?.user_metadata.avatar_url ? '' : 'i-carbon:user-avatar-filled'"
      >
    </NuxtLink>
    <NavbarLink v-else url="/register" :variant="linksVariant">
      Sign in
    </NavbarLink>
  </div>
</template>

<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { type NavbarLinksVariants, navbarLinksVariants } from ".";
import { cn } from "@/lib/utils";

interface Props {
  variant?: NavbarLinksVariants["variant"]
  linksVariant?: NavbarLinksVariants["linksVariant"]
  firstLinkVariant?: NavbarLinksVariants["firstLinkVariant"]
  class?: HTMLAttributes["class"]
}

const props = defineProps<Props>();

const user = useSupabaseUser();
</script>
