<template>
  <div
    :class="cn(navbarLinksVariants({ variant }), props.class)"
  >
    <NavbarLink url="#" :variant="firstLinkVariant">
      Landsat Locator
    </NavbarLink>
    <NavbarLink url="#" :variant="linksVariant">
      Search for data
    </NavbarLink>
    <NavbarLink url="#" :variant="linksVariant">
      About us
    </NavbarLink>
    <img
      v-if="user" h="5vh" alt="User profile picture" rounded-full
      :src="user ? user?.user_metadata.avatar_url : ''"
      :class="user ? user?.user_metadata.avatar_url ? '' : 'i-carbon:user-avatar-filled' : ''"
    >
    <NavbarLink v-if="!isUserLoggedIn" url="/register" :variant="linksVariant">
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

const props = withDefaults(defineProps<Props>(), {
  as: "navbar-links"
});

const isUserLoggedIn = ref(false);

const user = useSupabaseUser();
</script>
