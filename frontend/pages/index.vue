<template>
  <div w-full overflow-x-hidden bg-black>
    <div h-screen>
      <div class="bg-[url(assets/img/background.png)]" bg-cover bg-center full-height-without-header>
        <div h-full flex flex-col items-center justify-center bg-black bg-opacity-85>
          <div flex flex-col items-center justify-center text-center text-gray-100>
            <div md="text-5xl leading-14" text-3xl font-bold w="55%">
              <span
                from-indigo-300 via-blue-300 to-green-300 bg-gradient-to-r bg-clip-text text-transparent
              >Landsat</span>: Where Every Pixel Tells a Story!
            </div>
            <div mt-6 w="50%" md="leading-5 text-base" text-sm>
              We provide a wealth of satellite imagery data that can be accessed through our web application.
            </div>
            <Button bg-color="green" md="mt-10" mt-5 text-size="xs">
              <NuxtLink to="login" flex items-center justify-center>
                Get started<img md="text-xl" text-base text-black class="i-ci:play-arrow">
              </NuxtLink>
            </Button>
          </div>
          <Arch stroke-width="0.2" mb="-20vh" md="block" arch-number="1" hidden w-screen />
          <Arch stroke-width="0.5" mb="-10vh" md="hidden" block arch-number="2" w-screen />
        </div>
      </div>
    </div>
    <div h-50vh md="h-40vh -mt-15vh" mt="-30vh">
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
