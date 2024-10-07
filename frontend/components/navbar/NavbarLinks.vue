<template>
  <div
    :class="cn(navbarLinksVariants({ variant }), props.class)"
  >
    <NavbarLink url="/faq" :variant="firstLinkVariant">
      FAQ
    </NavbarLink>
    <NavbarLink url="/how_does_it_work" :variant="linksVariant">
      How does it work?
    </NavbarLink>
    <NavbarLink v-if="user" url="/panel/select_scene" :variant="linksVariant">
      Select scene
    </NavbarLink>
    <NavbarLink url="/panel/reports" :variant="linksVariant">
      Reports
    </NavbarLink>
    <NavbarLink v-if="user" url="/panel/watch_my_pixel" :variant="linksVariant">
      Watch My Pixel
    </NavbarLink>
    <NavbarLink v-if="user" url="/panel/my_pixel_watches" :variant="linksVariant">
      My Pixel Watches
    </NavbarLink>
    <NuxtLink v-if="user" to="/panel">
      <UserNav :avatar-url="user?.user_metadata.avatar_url" />
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
import UserNav from "~/components/navbar/UserNav.vue";

interface Props {
  variant?: NavbarLinksVariants["variant"]
  linksVariant?: NavbarLinksVariants["linksVariant"]
  firstLinkVariant?: NavbarLinksVariants["firstLinkVariant"]
  class?: HTMLAttributes["class"]
}

const props = defineProps<Props>();

const user = useSupabaseUser();
</script>
