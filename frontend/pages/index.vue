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
          <svg class="arch" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20" preserveAspectRatio="none" mb="-20vh" md="block" hidden w-screen>
            <path d="M 0 20 Q 50 15 100 20" stroke="url(#grad1)" stroke-width="0.2" fill="transparent" />
            <defs>
              <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#6983EA; stop-opacity:1" />
                <stop offset="25%" style="stop-color:#5BC0BE; stop-opacity:1" />
                <stop offset="100%" style="stop-color:#9EF01A; stop-opacity:1" />
              </linearGradient>
            </defs>
          </svg>
          <svg class="arch" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20" preserveAspectRatio="none" mb="-10vh" md="hidden" block w-screen>
            <path d="M 0 20 Q 50 15 100 20" stroke="url(#grad2)" stroke-width="0.5" fill="transparent" />
            <defs>
              <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#6983EA; stop-opacity:1" />
                <stop offset="25%" style="stop-color:#5BC0BE; stop-opacity:1" />
                <stop offset="100%" style="stop-color:#9EF01A; stop-opacity:1" />
              </linearGradient>
            </defs>
          </svg>
        </div>
      </div>
    </div>
    <div h-40vh md="-mt-15vh" mt="-30vh">
      <SlidingTextBlock data-aos="fade-right" header="Our mission">
        is to grant users the access to the corresponding Landsat SR data.
      </SlidingTextBlock>
      <SlidingTextBlock data-aos="fade-left" direction="right" header="Get your results in a couple of easy steps!">
        <ul ml-3 list-disc>
          <li>Choose a target location</li>
          <li>etc</li>
        </ul>
      </SlidingTextBlock>
    </div>
    <Footer />
  </div>
</template>
