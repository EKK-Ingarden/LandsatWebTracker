import { type VariantProps, cva } from "class-variance-authority";

export { default as Button } from "./Button.vue";

export const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        grayDefault: "bg-gray-400 text-gray-700 shadow hover:bg-gray-600",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline"
      },
      size: {
        default: "md:h-9 md:px-4 md:py-2 h-7 px-2 py-1",
        xs: "h-7 rounded px-2",
        sm: "h-8 rounded-md px-3",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9"
      },
      textSize: {
        default: "text-sm",
        xs: "text-xs",
        base: "text-base",
        lg: "text-lg"
      },
      bgColor: {
        default: "",
        gray300: "bg-gray-300"
      }
    },
    defaultVariants: {
      variant: "default",
      size: "default",
      textSize: "default",
      bgColor: "default"
    }
  }
);

export type ButtonVariants = VariantProps<typeof buttonVariants>;
