<template>
  <div bg="#232323" mt-6 border-rd-sm>
    <Accordion type="single" collapsible mx-4>
      <AccordionItem :value="item.value">
        <AccordionTrigger>
          <p>{{ item.question }}</p>
        </AccordionTrigger>
        <AccordionContent>
          <p color="#a3a3a3">
            {{ item.answer }}
          </p>
        </AccordionContent>
      </AccordionItem>
    </Accordion>
  </div>
</template>

<script setup lang="ts">
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

defineProps<{
  item: {
    value: string
    question: string
    answer: string
  }
}>();
</script>

<style scoped lang="scss">

</style>
