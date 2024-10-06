<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <img
        h-9 aria-label="User profile picture" alt="" rounded-full
        :src="avatarUrl"
        :class="avatarUrl ? '' : 'i-carbon:user-avatar-filled'"
      >
    </DropdownMenuTrigger>
    <DropdownMenuContent class="w-56">
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuGroup>
        <NuxtLink to="/panel">
          <DropdownMenuItem>
            <span>Dashboard</span>
          </DropdownMenuItem>
        </NuxtLink>
        <NuxtLink to="/pane/watch_my_pixell">
          <DropdownMenuItem>
            <span>Watch my pixel</span>
          </DropdownMenuItem>
        </NuxtLink>
        <NuxtLink to="/panel/my_pixel_watches">
          <DropdownMenuItem>
            <span>My pixel watches</span>
          </DropdownMenuItem>
        </NuxtLink>
        <DropdownMenuItem>
          <span>Watch my pixel</span>
        </DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuItem cursor-pointer @click="signOut()">
        <span color-red>Log out</span>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>

<script setup lang="ts">
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger
} from "@/components/ui/dropdown-menu";

defineProps<{
  avatarUrl?: string
}>();

const { auth } = useSupabaseClient();

function signOut() {
  auth.signOut();
  navigateTo("/");
}
</script>
