// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    "@unocss/nuxt",
    "shadcn-nuxt",
    "@nuxt/eslint",
    "@nuxtjs/leaflet",
    "nuxt-open-fetch",
    "@nuxtjs/supabase"
  ],
  css: [
    "@unocss/reset/tailwind.css"
  ],
  devtools: { enabled: true },
  compatibilityDate: "2024-04-03",
  runtimeConfig: {
    public: {
      //     apiBase: "http://localhost:8000/",
      baseUrl: process.env.BASE_URL || "http://localhost:3000"
    }
  },

  eslint: {
    config: {
      standalone: false
    }
  },

  supabase: {
    redirectOptions: {
      login: "/login",
      callback: "/confirm",
      include: ["/panel(/*)?"]
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
