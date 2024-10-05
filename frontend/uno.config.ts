import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTagify,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup
} from "unocss";
import { presetShadcn } from "unocss-preset-shadcn";
import { createLocalFontProcessor } from '@unocss/preset-web-fonts/local'


export default defineConfig({
  presets: [
    presetUno(),
    presetTagify(),
    presetAttributify(),
    presetTypography(),
    presetWebFonts({
      provider: "none",
      fonts: {
        inter: "Inter"
      },
      processors: createLocalFontProcessor({
        cacheDir: 'node_modules/.cache/unocss/fonts',
        fontAssetsDir: '/assets/fonts',
        fontServeBaseUrl: '/assets/fonts'
      }),
    }),
    presetIcons(),
    presetShadcn({
      color: "neutral"
    })
  ],
  rules: [
    ["full-height-without-header", { height: "calc(100% - 5rem)" }]
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
        "components/**/*.{js,ts}"
      ]
    }
  }
});
