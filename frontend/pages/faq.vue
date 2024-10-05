<template>
  <div w-full overflow-x-hidden bg-black>
    <div mx-19 mt-6 bg-opacity-85 full-height-without-header>
      <p text-6xl font-950>
        FAQ
      </p>
      <p text-5xl font-850 color="#d4d4d4">
        How can we help?
      </p>
      <div mt-10 flex-col items-center bg-cover bg-center>
        <div bg="#232323" border-rd-sm>
          <Accordion type="single" collapsible mx-4>
            <AccordionItem value="item-1">
              <AccordionTrigger>
                <p>
                  How often do Landsat satellites pass over the same location?
                </p>
              </AccordionTrigger>
              <AccordionContent>
                <p color="#a3a3a3">
                  Landsat satellites typically revisit the same location every 16 days. However, by using both Landsat 8 and Landsat 9, users can effectively get coverage every 8 days for most regions..
                </p>
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
        <div bg="#232323" mt-6 border-rd-sm>
          <Accordion type="single" collapsible mx-4>
            <AccordionItem value="item-1">
              <AccordionTrigger>
                <p>
                  What does Landsat data show?
                </p>
              </AccordionTrigger>
              <AccordionContent>
                <p color="#a3a3a3">
                  Landsat data provides imagery that captures visible and infrared light reflected off the Earth's surface. This data can be used to study vegetation, urban growth, water bodies, forests, agricultural lands, and more.
                </p>
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
        <div bg="#232323" mt-6 border-rd-sm>
          <Accordion type="single" collapsible mx-4>
            <AccordionItem value="item-1">
              <AccordionTrigger>
                <p>
                  How do I define my target location?
                </p>
              </AccordionTrigger>
              <AccordionContent>
                <p color="#a3a3a3">
                  Landsat satellites typically revisit the same location every 16 days. However, by using both Landsat 8 and Landsat 9, users can effectively get coverage every 8 days for most regions..
                </p>
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
        <div bg="#232323" mt-6 border-rd-sm>
          <Accordion type="single" collapsible mx-4>
            <AccordionItem value="item-1">
              <AccordionTrigger>
                <p>
                  Do I need to install any software to use the application?
                </p>
              </AccordionTrigger>
              <AccordionContent>
                <p color="#a3a3a3">
                  Landsat satellites typically revisit the same location every 16 days. However, by using both Landsat 8 and Landsat 9, users can effectively get coverage every 8 days for most regions..
                </p>
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
        <Footer />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
</script>

<style scoped lang="scss">

</style>
