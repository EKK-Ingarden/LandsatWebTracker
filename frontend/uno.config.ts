import {
  defineConfig,
  presetAttributify,
  presetTagify,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup
} from "unocss";
import { presetShadcn } from "unocss-preset-shadcn";

export default defineConfig({
  presets: [
    presetUno(),
    presetTagify(),
    presetAttributify(),
    presetTypography(),
    presetWebFonts({
      provider: "google",
      fonts: {
        sans: "Inter",
      }
    }),
    presetShadcn({
      color: "neutral"
    })
  ],
  transformers: [
    transformerDirectives(),
    transformerVariantGroup({ separators: [":"] })
  ],
  content: {
    pipeline: {
      include: [
        // the default
        /\.(vue|svelte|[jt]sx|mdx?|astro|elm|php|phtml|html)($|\?)/,
        // include js/ts files
        "components/ui/**/*.{js,ts}"
      ]
    }
  }
});
