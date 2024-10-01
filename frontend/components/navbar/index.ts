import { type VariantProps, cva } from "class-variance-authority";

export { default as Navbar } from "./Navbar";
export { default as NavbarLink } from "./NavbarLink";
export { default as NavbarLinks } from "./NavbarLinks";

export const navbarLinkVariants = cva(
  "items-center",
  {
    variants: {
      variant: {
        default: "relative text-center text-white no-underline before:absolute before:bottom-0 before:left-0 "
          + "before:block before:h-[2px] before:w-full before:scale-x-0 before:bg-white before:transition-transform "
          + "before:duration-200 before:ease-linear before:content-[''] hover:before:scale-x-100",
        sidebar: "border-b-1 pb-4 border-gray-500 w-full",
        firstSidebar: "border-y-1 py-4 border-gray-500 w-full"
      }
    },
    defaultVariants: {
      variant: "default"
    }
  }
);

export const navbarLinksVariants = cva(
  "items-center gap-5",
  {
    variants: {
      variant: {
        default: "md:flex hidden flex-row",
        sidebar: "flex flex-col text-2xl text-center"
      },
      linksVariant: {
        default: "default",
        sidebar: "sidebar"
      },
      firstLinkVariant: {
        default: "default",
        firstSidebar: "firstSidebar"
      }
    },
    defaultVariants: {
      variant: "default",
      linksVariant: "default",
      firstLinksVariant: "default"
    }
  }
);

export type NavbarLinkVariants = VariantProps<typeof navbarLinkVariants>;
export type NavbarLinksVariants = VariantProps<typeof navbarLinksVariants>;
