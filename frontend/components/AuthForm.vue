<template>
  <div class="bg-[url(assets/img/background.webp)]" bg-cover bg-center full-height-without-header>
    <div h-full flex items-center justify-center bg-black bg-opacity-85>
      <div h-95 w-85 flex flex-col items-center rounded-lg bg-black bg-opacity-60 mb="20vh" p-5>
        <div w="90%" mb-5 ml-3 self-start text-2xl font-bold>
          {{ props.isLogin ? 'Sign in' : 'Sign up' }}
        </div>
        <div w-full flex justify-center>
          <div w="90%" flex flex-col gap-3>
            <Input
              v-model="email" type="email" placeholder="Email"
              size="authForm" bg-color="gray900" border-setup="border1Gray400" placeholder:text-white
            />
            <Input
              v-model="password" type="password" placeholder="Password"
              size="authForm" bg-color="gray900" border-setup="border1Gray400" placeholder:text-white
            />
          </div>
        </div>
        <span :class="error ? '' : 'invisible'" h-7 text-red>{{ error }}</span>
        <Button w="90%" size="default" bg-color="gray300" @click="passwordAuth(isLogin)">
          Continue
        </Button>
        <div mt-7 flex gap-2>
          <button
            hover="brightness-120"
            class="i-logos:google-icon" scale-85 rounded-full text-5xl
            @click="auth.signInWithOAuth({ provider: 'google', options: { redirectTo } })"
          />
          <button
            rounded-full hover="bg-white" bg-gray-300
            class="i-ci:github" text-5xl
            @click="auth.signInWithOAuth({ provider: 'github', options: { redirectTo } })"
          />
        </div>

        <p mt-5 text-sm>
          {{ props.isLogin ? "New to our site?" : "Already a user?" }}
          <NuxtLink font-bold :to="props.isLogin ? 'register' : 'login'" underline>
            {{ props.isLogin ? "Sign up now!" : "Sign in now!" }}
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

async function passwordAuth(isLogin: boolean) {
  let value;
  if (error.value) {
    error.value = "";
  }

  if (isLogin) {
    value = await auth.signInWithPassword({ email: email.value, password: password.value });
  } else {
    value = await auth.signUp({ email: email.value, password: password.value });
  }

  if (value.error) {
    error.value = value.error.message;
  } else {
    navigateTo("/confirm");
  }
}
</script>
