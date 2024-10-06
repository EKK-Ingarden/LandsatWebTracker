<template>
  <div bg="#232323" mt-6 border-rd-sm>
    <Accordion type="single" collapsible mx-4>
      <AccordionItem value=":3">
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
    question: string
    answer: string
  }
}>();
</script>
