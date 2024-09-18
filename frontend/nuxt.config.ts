// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    "@unocss/nuxt",
    "shadcn-nuxt",
    "@nuxt/eslint",
    "@nuxtjs/leaflet"
  ],
  css: [
    "@unocss/reset/tailwind.css"
  ],
  devtools: { enabled: true },
  compatibilityDate: "2024-04-03",
  eslint: {
    config: {
      standalone: false
    }
  },

  shadcn: {
    prefix: "",
    componentDir: "./components/ui"
  },

  imports: {
    dirs: [
      "./lib"
    ]
  }
});
