<template>
  <CalendarPrev
    :class="cn(
      buttonVariants({ variant: 'outline' }),
      'h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100 text-white',
      props.class,
    )"
    v-bind="forwardedProps"
  >
    <slot>
      &lt;-
    </slot>
  </CalendarPrev>
</template>

<script lang="ts" setup>
import { type HTMLAttributes, computed } from "vue";
import { CalendarPrev, type CalendarPrevProps, useForwardProps } from "radix-vue";
import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

const props = defineProps<CalendarPrevProps & { class?: HTMLAttributes["class"] }>();

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props;

  return delegated;
});

const forwardedProps = useForwardProps(delegatedProps);
</script>
