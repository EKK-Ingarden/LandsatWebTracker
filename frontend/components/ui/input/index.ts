import { type VariantProps, cva } from "class-variance-authority";

export { default as Input } from "./Input.vue";

export const inputVariants = cva(
  "flex w-full px-3 py-1 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50",
  {
    variants: {
      size: {
        default: "h-9",
        authForm: "h-10"
      },
      bgColor: {
        default: "bg-transparent",
        gray900: "bg-gray-900",
        white: "bg-white"
      },
      // not simplest possible name to avoid conflicts with unocss properties
      borderSetup: {
        default: "border border-input",
        border1Gray400: "border-1 border-gray-400",
        border2Black: "border-2 border-black",
        borderB2Gray500: "border-b-2 border-gray-500",
        none: "bg-none"
      },
      rounded: {
        default: "rounded-md",
        right: "rounded-r-md",
        topRight: "rounded-tr-md",
        bottomRight: "rounded-br-md",
        none: "rounded-none"
      }
    },
    defaultVariants: {
      size: "default",
      bgColor: "default",
      borderSetup: "default"
    }
  }
);

export type InputVariants = VariantProps<typeof inputVariants>;
