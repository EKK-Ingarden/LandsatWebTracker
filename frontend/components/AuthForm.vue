<template>
  <div class="bg-[url(assets/img/background.png)]" bg-cover bg-center full-height-without-header>
    <div h-full flex items-center justify-center bg-black bg-opacity-85>
      <div h-90 w-80 flex flex-col items-center rounded-lg bg-black bg-opacity-50 mb="20vh">
        <div mb-5 self-start p-5 text-2xl font-bold>
          {{ props.isLogin ? 'Sign in' : 'Register' }}
        </div>
        <div w-full flex justify-center>
          <div w="90%" flex flex-col gap-3>
            <Input v-model="email" type="email" placeholder="Email" border-1 border-gray-400 bg-gray-900 placeholder:text-white />
            <Input v-model="password" type="password" placeholder="Password" border-1 border-gray-400 bg-gray-900 placeholder:text-white />
          </div>
        </div>
        <span :class="error ? '' : 'invisible'" h-7 text-red>{{ error }}</span>
        <Button w="90%" size="default" bg-color="gray300" @click="props.isLogin ? signIn() : signUp()">
          Continue
        </Button>
        <div mt-5 flex gap-2>
          <button
            class="i-ci:google"
            text-5xl @click="auth.signInWithOAuth({ provider: 'google', options: { redirectTo } })"
          />
          <button
            class="i-ci:github"
            text-5xl @click="auth.signInWithOAuth({ provider: 'github', options: { redirectTo } })"
          />
        </div>
        <p mt-3 text-sm>
          {{ props.isLogin ? "New to our site?" : "Already a user?" }}
          <NuxtLink font-bold :to="props.isLogin ? 'register' : 'login'">
            {{ props.isLogin ? "Sign up now!" : "Login now!" }}
          </NuxtLink>
        </p>
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
