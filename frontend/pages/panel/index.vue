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

    <Button>
      <a href="/panel/wmpform" font-bold underline>WMP Form</a>
    </Button>
  </div>
</template>

<script setup lang="ts">
import apiAuth from "~/utils/api-auth";

const user = useSupabaseUser();
const { auth } = useSupabaseClient();

async function getUser() {
  console.log(useSupabaseSession().value?.access_token);
  const { data, error } = await apiAuth("/auth/get_user");
  console.log(data, error);
}
function signOut() {
  auth.signOut();
  navigateTo("/");
}
</script>
