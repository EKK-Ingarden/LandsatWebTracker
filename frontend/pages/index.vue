<template>
  <div w-full overflow-x-hidden bg-black>
    <div class="bg-[url(assets/img/background.webp)]" bg-cover bg-center full-height-without-header>
      <div flex flex-col items-center justify-center bg-black bg-opacity-85 full-height-without-header>
        <div flex flex-col items-center justify-center text-center text-gray-100>
          <div md="text-5xl leading-14" text-3xl font-bold w="55%">
            <span
              from="#6983EA" via="#5BC0BE" to="#9EF01A" bg-gradient-to-r bg-clip-text text-transparent
            ><span bg-white bg-opacity-50 bg-clip-text>Landsat</span></span>: Where Every Pixel Tells a Story!
          </div>
          <div mt-6 w="50%" md="leading-5 text-base" text-sm>
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

    <Arch :stroke-width="0.2" md="block" hidden arch-number="1" w-screen mt="-8" />

    <div h-50vh md="h-40vh mt-10" mt="-30vh">
      <SlidingTextBlock data-aos="fade-right" header="Our mission">
        is to grant users the access to the corresponding Landsat SR data.
      </SlidingTextBlock>
      <SlidingTextBlock
        data-aos="fade-left" is-right
        header="Get your results in a couple of easy steps!"
      >
        <ul ml-3 list-disc>
          <li>Choose a target location</li>
          <li>etc</li>
        </ul>
      </SlidingTextBlock>
    </div>
    <Footer />
  </div>
</template>
