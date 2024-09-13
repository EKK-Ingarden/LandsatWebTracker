import eslintConfig from "@antfu/eslint-config";
import nuxtConfig from "./.nuxt/eslint.config.mjs";

export default eslintConfig(
    // General
    {
        typescript: true,
        vue: true,
        unocss: true,
        stylistic: {
            indent: 4,
            quotes: "double"
        },
        rules: {
            curly: "off",
            "no-console": "off",
            "no-new-func": "off",
            "style/semi": ["error", "always"],
            "style/indent": ["error", 4],
            "style/quote-props": ["warn", "as-needed"],
            "style/comma-dangle": ["warn", "never"],
            "style/brace-style": ["warn", "1tbs"],
            "style/arrow-parens": ["error", "always"],
            "vue/block-order": ["error", {
                order: ["template", "script", "style"]
            }],
            "vue/script-indent": ["error", 4, {
                baseIndent: 1
            }],
            "antfu/top-level-function": "off",
            "node/prefer-global/process": ["off"]
        }
    },

    nuxtConfig()
);
