// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    "@unocss/nuxt",
    "shadcn-nuxt",
    "@nuxt/eslint",
    "@nuxtjs/leaflet",
    "nuxt-open-fetch"
  ],
  css: [
    "@unocss/reset/tailwind.css"
  ],
  devtools: { enabled: true },
  compatibilityDate: "2024-04-03",
  runtimeConfig: {
    public: {
      apiBase: "http://localhost:8000/"
    }
  },

  eslint: {
    config: {
      standalone: false
    }
  },

  shadcn: {
    prefix: "",
    componentDir: "./components/ui"
  },

  openFetch: {
    clients: {
      api: {
        baseURL: "http://localhost:8000/"
      }
    }
  },

  imports: {
    dirs: [
      "./lib"
    ]
  }
});
