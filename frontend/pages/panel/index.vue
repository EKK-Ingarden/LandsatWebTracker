<template>
  <div>
    <h1>This page is only visible for logged users</h1>

    <Button @click="getUser">
      Get user from backend
    </Button>

    {{ user?.email }}
    <Button @click="signOut">
      Sign out
    </Button>
  </div>
</template>

<script setup lang="ts">
const user = useSupabaseUser();

const { auth } = useSupabaseClient();
async function getUser() {
  console.log(useSupabaseSession().value?.access_token);
  const { data, error } = await useApi("/auth/get_user", {
    headers: {
      Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
    }
  });
  console.log(data, error);
}
function signOut() {
  auth.signOut();
  navigateTo("/");
}
</script>
