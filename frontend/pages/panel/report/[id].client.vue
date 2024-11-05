<template>
  <div>
    <h1 text-5xl mb-5 ml-4>
      Report data
    </h1>
    <div grid grid-cols-1 gap-4 h-0 mx-4 md="grid-cols-2">
      <div p-4 border-2 border-white rounded-lg>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead class="w-[150px]">
                Data
              </TableHead>
              <TableHead>Value</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow v-for="(value, key) in metadata" :key="key">
              <TableCell class="font-medium">
                {{ key }}
              </TableCell>
              <TableCell>
                {{ value }}
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </div>
      <div>
        <Map :tile-layer-overlay="selectedMosaic" mb-5 h-100 :not-full-height="true"/>
        <Button @click="selectMosaic(0)">
          Natural
        </Button>
        <Button @click="selectMosaic(1)" m-x-1>
          Temperature
        </Button>
        <Button @click="selectMosaic(3)">
          Agriculture
        </Button>
        <Button @click="selectMosaic(4)" m-x-1>
          Vegetation
        </Button>
        <Button @click="selectMosaic(5)">
          Moisture
        </Button>
        <Button @click="selectMosaic(6)" m-x-1>
          Atmospheric Penetration
        </Button>
      </div>
      <div border-2 border-white rounded-lg>
        <LineChart
          :data="reportData.temperature_chart"
          index="temperature"
          :categories="['distribution']"
          :colors="['#13b982']"
        />
      </div>
      <div border-2 border-white rounded-lg>
        <LineChart
          :data="reportData.reflectance_chart"
          index="wave_length"
          :categories="['reflectance']"
          :colors="['#13b982']"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { LatLngBoundsLiteral } from "leaflet";
import { LineChart } from "~/components/ui/chart-line";

const route = useRoute();
const reportData: any = ref(null);
const selectedMosaic = ref<{
  url: string
  bounds: LatLngBoundsLiteral
} | undefined>(undefined);

async function selectMosaic(type: number) {
  const { data } = await useApi("/landsat/mosaic", {
    query: {
      scene_id: reportData.value.id,
      collection_id: "landsat-c2-l2",
      mosaic_type: type.toString() as any
    }
  });
  let url: string = data.value!.toString();
  url = url.replace("%7Bz%7D", "{z}");
  url = url.replace("%7Bx%7D", "{x}");
  url = url.replace("%7By%7D", "{y}");
  selectedMosaic.value = {
    url,
    bounds: reportData.value.polygon.coordinates.map(({ latitude, longitude }) => [latitude, longitude] as [number, number])
  };
}

const { data, error } = await useApi("/report/get_report", {
  query: {
    scene_id: route.params.id.toString()
  }
});

if (error.value) {
  console.error("Error fetching report:", error.value);
} else if (data.value) {
  reportData.value = data.value;
  selectMosaic(0);
}

const metadata = {
  "Scene ID": reportData.value.id,
  Satellite: reportData.value.platform.replace("-", " ").replace("landsat", "Landsat"),
  "Cloud Coverage": reportData.value.eo_cloud_cover,
  Path: reportData.value.wrs_coordinates.wrs_path,
  Row: reportData.value.wrs_coordinates.wrs_row,
  "Collection Category": reportData.value.metadata.collection_category,
  "Collection Number": reportData.value.metadata.collection_number,
  "Created At": reportData.value.metadata.created,
  "Sun Azimuth": reportData.value.metadata.sun_azimuth,
  "Sun Elevation": reportData.value.metadata.sun_elevation,
  Instruments: reportData.value.metadata.instruments.join(", ")
};
</script>
