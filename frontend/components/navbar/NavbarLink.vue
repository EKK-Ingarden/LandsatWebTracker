<template>
  <NuxtLink
    :to="url"
    :class="cn(navbarLinkVariants({ variant }), props.class)"
  >
    <slot />
  </NuxtLink>
</template>

<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { type NavbarLinkVariants, navbarLinkVariants } from ".";
import { cn } from "@/lib/utils";

interface Props {
  variant?: NavbarLinkVariants["variant"]
  class?: HTMLAttributes["class"]
  url: string
}

const props = defineProps<Props>();
</script>
