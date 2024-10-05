<template>
  <input v-model="modelValue" :class="cn(inputVariants({ size, bgColor, borderSetup }), props.class)">
</template>

<script setup lang="ts">
import type { HTMLAttributes } from "vue";
import { useVModel } from "@vueuse/core";
import type { InputVariants } from ".";
import { inputVariants } from ".";
import { cn } from "@/lib/utils";

const props = defineProps<{
  defaultValue?: string | number
  modelValue?: string | number
  size?: InputVariants["size"]
  bgColor?: InputVariants["bgColor"]
  borderSetup?: InputVariants["borderSetup"]
  class?: HTMLAttributes["class"]
}>();

const emits = defineEmits<{
  (e: "update:modelValue", payload: string | number): void
}>();

const modelValue = useVModel(props, "modelValue", emits, {
  passive: true,
  defaultValue: props.defaultValue
});
</script>
