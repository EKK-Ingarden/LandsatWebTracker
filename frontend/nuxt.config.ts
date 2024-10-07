// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    "@unocss/nuxt",
    "shadcn-nuxt",
    "@nuxt/eslint",
    "@nuxtjs/leaflet",
    "nuxt-open-fetch",
    "@nuxtjs/supabase",
    "nuxt-aos"
  ],
  css: [
    "@unocss/reset/tailwind.css",
    "~/assets/css/uno.css"
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
        baseURL: process.env.NUXT_OPEN_FETCH_API_BASE_URL || "http://localhost:8000/"
      }
    }
  },

  imports: {
    dirs: [
      "./lib"
    ]
  }
});
