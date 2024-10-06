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
      <div v-for="(item, index) in faqList" :key="`key-${index}`" mx-19 mt-6>
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
    question: "What is the purpose of this application?",
    answer: "This app allows users to compare ground-based spectral measurements with Landsat data. It enables users to define a location, receive notifications when Landsat passes over that location, and access the corresponding Landsat data."
  },
  {
    question: "Who can benefit from using this app?",
    answer: "The application is designed for teachers, researchers, students, geographers, and anyone who is interested in comparing satellite data with ground observations. It encourages scientific exploration and fosters interdisciplinary learning."
  },
  {
    question: "Do I need any prior knowledge to use this app?",
    answer: "Basic knowledge of remote sensing and spectral data is helpful but not necessary. The application will be user-friendly with guides to help you through the process."
  },
  {
    question: "How do I define my target location?",
    answer: "You can either input the geographical coordinates (latitude and longitude) or select a location using an interactive map."
  },
  {
    question: "Do I need to create an account to use the application?",
    answer: "Yes, users will need to create an account to access certain features, such as saving locations and receiving notifications."
  },
  {
    question: "What if I forget my password?",
    answer: "The application includes a password recovery option, allowing you to reset your password via email verification."
  },
  {
    question: "How reliable is the Landsat data used in this application?",
    answer: "Landsat data is collected by NASA and the USGS, and it undergoes rigorous calibration and validation processes to ensure its accuracy and reliability."
  },
  {
    question: "Do I need to install any software to use the application?",
    answer: "No, the application is web-based and can be accessed via any modern browser without the need for additional software installations."
  },
  {
    question: "How will I know when a Landsat satellite will pass over my location?",
    answer: "The application will send you notifications based on your selected location when a Landsat satellite is scheduled to pass over, you will get email notification."
  },
  {
    question: "How can this application be used in educational settings?",
    answer: "Teachers and students can use the app to study the real-world environment by comparing satellite data with ground-based observations. It promotes interdisciplinary learning, including geography, environmental science, and data analysis."
  },
  {
    question: "How often do Landsat satellites pass over the same location?",
    answer: "Landsat satellites typically revisit the same location every 16 days. However, by using both Landsat 8 and Landsat 9, users can effectively get coverage every 8 days for most regions."
  },
  {
    question: "Can Landsat be used for climate change studies?",
    answer: "Yes, Landsat data is widely used to monitor long-term environmental changes, such as glacier retreat, sea-level rise, deforestation, and desertification, which are all indicators of climate change."
  },
  {
    question: "How is Landsat used in agriculture?",
    answer: "In agriculture, Landsat imagery helps farmers monitor crop health, soil moisture, and irrigation needs by analyzing the spectral reflectance of plants and soil. It can also detect early signs of stress in crops."
  },
  {
    question: "What is the Landsat program?",
    answer: "The Landsat program is a joint effort between NASA and the U.S. Geological Survey (USGS) that provides satellite imagery of Earth's surface. Launched in 1972, it is the longest-running Earth observation program and is used for monitoring environmental changes, land use, and natural resources."
  },
  {
    question: "What does Landsat data show?",
    answer: "Landsat data provides imagery that captures visible and infrared light reflected off the Earth's surface. This data can be used to study vegetation, urban growth, water bodies, forests, agricultural lands, and more."
  },
  {
    question: "How is Landsat different from other satellite programs?",
    answer: "Landsat's main strengths are its long history (over 50 years of continuous data) and its moderate spatial resolution (30 meters), which is ideal for regional and global studies. Other satellites, like Sentinel or MODIS, may offer different spatial, temporal, or spectral characteristics, but Landsat provides a balance between detail and coverage."
  }
];
</script>
