<template>
  <div class="h-screen flex items-center justify-center">
    <div class="mx-auto max-w-xl text-center">
      <div class="mb-5 text-5xl">
        {{ props.isLogin ? 'Login' : 'Register' }}
      </div>

      <div class="mx-20">
        <input v-model="email" type="email" placeholder="Email" class="mx-auto my-5 block">
        <input v-model="password" type="password" placeholder="Password" class="mx-auto my-5 block">
      </div>

      <span v-if="error" my-5 text-red>{{ error }}</span>

      <div>
        <Button @click="auth.signInWithOAuth({ provider: 'google', options: { redirectTo } })">
          Google
        </Button>
        <Button mx-3 @click="auth.signInWithOAuth({ provider: 'github', options: { redirectTo } })">
          Github
        </Button>
        <Button @click="props.isLogin ? signIn() : signUp()">
          Sign {{ props.isLogin ? 'in' : 'up' }} with password
        </Button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  isLogin: boolean
}>();

const { auth } = useSupabaseClient();

const email = ref("");
const password = ref("");
const error = ref("");

const redirectTo = `${useRuntimeConfig().public.baseUrl}/confirm`;

async function signIn() {
  const value = await auth.signInWithPassword({ email: email.value, password: password.value });

  if (value.error) {
    error.value = value.error.message;
  } else {
    navigateTo("/confirm");
  }
}

async function signUp() {
  const value = await auth.signUp({ email: email.value, password: password.value });

  if (value.error) {
    error.value = value.error.message;
  } else {
    navigateTo("/confirm");
  }
}
</script>
