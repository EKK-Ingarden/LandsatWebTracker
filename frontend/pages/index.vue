<template>
  <div w-full overflow-x-hidden bg-black>
    <div class="bg-[url(assets/img/background.webp)]" bg-cover bg-center md="h-screen" full-height-without-header>
      <div h-full w-full flex justify-center bg-black bg-opacity-85>
        <div md="full-height-without-header w-70%" w-full flex flex-col items-center justify-center text-center text-gray-100>
          <div md="text-5xl leading-14" text-4xl font-bold w="65%">
            <span
              from="#6983EA" via="#5BC0BE" to="#9EF01A" bg-gradient-to-r bg-clip-text text-transparent
            ><span bg-white bg-opacity-50 bg-clip-text>Landsat</span></span>: Where Every Pixel Tells a Story!
          </div>
          <div w="60%" mt-6 text-base leading-5>
            We provide a wealth of satellite imagery data that can be accessed through our web application.
          </div>
          <Button from="#b4c3f3" via="#b5e5cd" to="#cbf596" text-size="xs" md="mt-10" mt-5 bg-gradient-to-r>
            <NuxtLink to="login" flex items-center justify-center>
              Get started<img md="text-xl" text-base text-black class="i-ci:play-arrow">
            </NuxtLink>
          </Button>
        </div>
      </div>
    </div>

    <Arch :stroke-width="0.2" md="block" hidden arch-number="1" w-screen mt="-15" />
    <Arch :stroke-width="0.5" md="hidden" block arch-number="2" w-screen mt="-5" />

    <div h-screen md="mt-10 mb-40" mt="-25">
      <SlidingTextBlock data-aos="fade-right" header="Our mission">
        is to grant users the access to the corresponding Landsat Surface Reflection data.
      </SlidingTextBlock>
      <SlidingTextBlock header="Reminders" data-aos="fade-left" is-right>
        You can request us to sent you email reminder or push notification, whenever the Landsat passes over given location
      </SlidingTextBlock>
      <SlidingTextBlock header="Data we provide" data-aos="fade-right">
        For every chosen picture we provide variety of Landsat data, fe. temperature, cloud coverage, image quality and Earth-Sun distance
      </SlidingTextBlock>
      <SlidingTextBlock
        data-aos="fade-left" is-right
        header="Get your results in a couple of easy steps!"
      >
        <div>
          <p>Choose a target location</p>
          <p>Select the parameters you need</p>
          <p>Add reminder</p>
          <p>Get notification about your reminder</p>
        </div>
      </SlidingTextBlock>
    </div>
    <Footer />
  </div>
</template>
