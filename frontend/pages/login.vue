<template>
  <div class="h-screen flex items-center justify-center">
    <div class="mx-auto max-w-xl text-center">
      <div class="mb-5 text-5xl">
        Login
      </div>

      <div class="mx-20">
        <input v-model="email" type="email" placeholder="Email" class="mx-auto my-5 block">
        <input v-model="password" type="password" placeholder="Password" class="mx-auto my-5 block">
      </div>

      <span v-if="error" my-5 text-red>{{ error }}</span>

      <div>
        <Button @click="auth.signInWithOAuth({ provider: 'google', options: { redirectTo } })">
          Sign in with Google
        </Button>
        <Button mx-3 @click="auth.signInWithOAuth({ provider: 'github', options: { redirectTo } })">
          Sign in with Github
        </Button>
        <Button @click="signIn">
          Sign in with password
        </Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { auth } = useSupabaseClient();

const email = ref("");
const password = ref("");
const error = ref("");

const redirectTo = `${useRuntimeConfig().public.baseUrl}/confirm`;

async function signIn() {
  console.log({ email: email.value, password: password.value });
  const value = await auth.signInWithPassword({ email: email.value, password: password.value });

  if (value.error) {
    error.value = value.error.message;
  } else {
    navigateTo("/confirm");
  }
}
</script>
