<template>
  <div mx-auto w-full overflow-x-hidden bg-black bg-opacity-85 full-height-without-header>
    <div mx-19 mt-6>
      <span text-6xl font-950>
        How does it work?
      </span>
      <div flex-col>
        <div mt-8>
          <p text-4xl color="#a3a3a3">
            Landsat
          </p>
          <p mt-4>
            Landsat is a series of Earth-observing satellites that capture detailed images of the planet's surface. Operated by NASA and the USGS, it provides data used for monitoring land use, agriculture, forestry, climate change, and natural disasters over time.
          </p>
        </div>
        <div mt-8>
          <p text-4xl color="#a3a3a3">
            Landsat Pixel
          </p>
          <p mt-4>
            A Landsat pixel represents the smallest unit of a satellite image, capturing data for a specific area on Earth's surface. Each pixel corresponds to a fixed ground area, typically 30 meters by 30 meters for most Landsat sensors, and contains information about the reflected light in different spectral bands.
          </p>
        </div>
        <div mt-8>
          <p text-4xl color="#a3a3a3">
            Landsat Tile
          </p>
          <p mt-4>
            A Landsat tile is a section of a larger satellite image, representing a specific geographic area on Earth's surface. Each tile is made up of thousands of individual pixels and covers a predefined region, typically following a grid system.
          </p>
        </div>
        <div mt-8>
          <p text-4xl color="#a3a3a3">
            Landsat Data
          </p>
          <p mt-4>
            Landsat provides two main types of data products:<br><br>
            <ul>
              <li>
                Level 1 products: These are raw, unprocessed data directly captured by the satellite.
              </li>
              <li>
                Level 2 products: These are preprocessed data, corrected and enhanced for easier analysis.
              </li>
            </ul>
          </p>
        </div>
        <div mt-8>
          <p text-4xl color="#a3a3a3">
            Landsat Data Flow
          </p>
          <p mt-4>
            Landsat 9: <br><br>
            Level-1 Products: Delivered within 4-6 hours after image acquisition. <br>
            Level-2 Products (Surface Reflectance and Surface Temperature): Available in about 3 days. <br><br>

            Landsat 8: <br><br>
            Level-1 Products: Initially processed as Real-Time (RT) products. To create the complete products, data on the sensor's line of sight is needed, which can take up to 10 days. <br>
            Level-2 Products (Surface Reflectance and Surface Temperature): Typically available within 24 hours after the complete product is generated.
          </p>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
