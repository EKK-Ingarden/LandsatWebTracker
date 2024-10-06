<template>
  <div mx-auto w-full overflow-x-hidden bg-black bg-opacity-85 full-height-without-header>
    <div mx-19 mt-6>
      <p text-6xl font-950>
        FAQ
      </p>
      <p text-5xl font-850 color="#d4d4d4">
        How can we help?
      </p>
    </div>
    <div mt-10 flex-col bg-cover bg-center>
      <div v-for="item in faqList" :key="item.value" mx-19 mt-6>
        <AccordionItemComponent :item="item" />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import AccordionItemComponent from "@/components/FaqAccordionComponent.vue";

const faqList = [
  {
    value: "item-1",
    question: "How often do Landsat satellites pass over the same location?",
    answer: "Landsat satellites typically revisit the same location every 16 days. However, by using both Landsat 8 and Landsat 9, users can effectively get coverage every 8 days for most regions."
  },
  {
    value: "item-2",
    question: "What does Landsat data show?",
    answer: "Landsat data provides imagery that captures visible and infrared light reflected off the Earth's surface. This data can be used to study vegetation, urban growth, water bodies, forests, agricultural lands, and more."
  },
  {
    value: "item-3",
    question: "How do I define my target location?",
    answer: "To define your target location, you can use coordinates or select from a map interface provided in the application."
  },
  {
    value: "item-4",
    question: "Do I need to install any software to use the application?",
    answer: "No, you can access Landsat data directly through web applications without needing to install any software."
  }
];
</script>

<style scoped lang="scss">
</style>

<style scoped lang="scss">

</style>
