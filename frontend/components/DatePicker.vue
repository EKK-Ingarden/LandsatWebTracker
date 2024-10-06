<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        :class="cn(
          'w-[280px] justify-start text-left font-normal',
          !value && 'text-muted-foreground',
        )"
      >
        <div mr-2 h-4 w-4 class="i-material-symbols:calendar-month" />
        {{ value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date" }}
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0">
      <Calendar v-model="value" initial-focus />
    </PopoverContent>
  </Popover>
</template>

<script setup lang="ts">
import { DateFormatter, type DateValue, getLocalTimeZone } from "@internationalized/date";

const emit = defineEmits(["update:modelValue"]);
const value = ref<DateValue>();

watch(value, (newValue) => {
  emit("update:modelValue", newValue);
});

const df = new DateFormatter("en-US", {
  dateStyle: "long"
});
</script>
