<template>
  <div>
    <h1>Report</h1>
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
    <LineChart
      :data="reportData.temperature_chart"
      index="temperature"
      :categories="['distribution']"
      :colors="['#13b982']"
    />
    <LineChart
      :data="reportData.reflectance_chart"
      index="wave_length"
      :categories="['reflectance']"
      :colors="['#13b982']"
    />
  </div>
</template>

<script setup lang="ts">
import { LineChart } from "~/components/ui/chart-line";

const route = useRoute();
const reportData: any = ref(null);

const { data, error } = await useApi("/report/get_report", {
  query: {
    scene_id: route.params.id.toString()
  }
});

if (error.value) {
  console.error("Error fetching report:", error.value);
} else if (data.value) {
  reportData.value = data.value;
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
