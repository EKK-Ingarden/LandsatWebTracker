import {
    defineConfig,
    presetAttributify,
    presetTagify,
    presetTypography,
    presetUno,
    presetWebFonts
} from "unocss";

export default defineConfig({
    presets: [
        presetUno(),
        presetTagify(),
        presetAttributify(),
        presetTypography(),
        presetWebFonts()
    ]
});
