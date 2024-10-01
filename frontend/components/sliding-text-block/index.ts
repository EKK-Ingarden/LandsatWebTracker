import { type VariantProps, cva } from "class-variance-authority";

export { default as SlidingTextBlock } from "./SlidingTextBlock.vue";

export const slidingTextBlockVariants = cva(
  "text-left w-30vw md:h-10vh h-5vh bg-none md:mt-10vh mt-15vh",
  {
    variants: {
      direction: {
        left: "md:ml-20vw ml-10vw mr-auto",
        right: "md:mr-20vw mr-10vw ml-auto"
      }
    },
    defaultVariants: {
      direction: "left"
    }
  }
);

export type SlidingTextBlockVariants = VariantProps<typeof slidingTextBlockVariants>;
