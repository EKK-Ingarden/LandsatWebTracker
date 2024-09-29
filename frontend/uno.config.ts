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
        sans: "Inter"
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
  },
  safelist: [
    "pb-4",
    "border-gray-500",
    "border-b-2",
    "border-y-2",
    "py-4",
    "md:flex",
    "gap-5",
    "before:absolute",
    "before:bottom-0",
    "before:left-0",
    "before:block",
    "before:h-[2px]",
    "before:w-full",
    "before:scale-x-0",
    "before:bg-white",
    "before:transition-transform",
    "before:duration-200",
    "before:ease-linear",
    "before:content-['']",
    "hover:before:scale-x-100"
  ]
});
