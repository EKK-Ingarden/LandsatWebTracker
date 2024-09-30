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
      v-if="isUserLoggedIn" h="5vh" alt="User profile picture"
      :src="isUserLoggedIn ? user.avatar.url : '~/assets/img/placeholder_pfp.png'" rounded-full
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

async function getUser() {
  console.log(useSupabaseSession().value?.access_token);
  const { data, error } = await useApi("/auth/get_user", {
    headers: {
      Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
    }
  });
  console.log(data, error);
}

const user = getUser();

if (user.value !== undefined) {
  isUserLoggedIn.value = true;
}
</script>
