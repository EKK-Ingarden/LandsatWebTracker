<template>
  <div mx-35 mt-20>
    <p text-xl>
      Reports
    </p>

    <div mt-8 border rounded-md border-color="#737373">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Satelite</TableHead>
            <TableHead>Date</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Link</TableHead>
            <TableHead><!-- extends table header to full width --></TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(report, index) in reports" :key="report.row">
            <TableCell>{{ report.satelite }}</TableCell>
            <TableCell>{{ report.date }}</TableCell>
            <TableCell>{{ report.status }}</TableCell>
            <TableCell><NuxtLink to="{{ report.link }}">Link</NuxtLink></TableCell>
            <TableCell>
              <button class="text-red-500 hover:text-red-700" @click="deleteReport(index)">
                DELETE
              </button>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  </div>
</template>

<script setup lang="ts">
const reports = ref([
  {
    satelite: "Landsat 9",
    date: "11.9.2024",
    status: "Finished",
    link: "/panel/report/id"
  }
]);

const deleteReport = (rowIndex: number) => {
  reports.value.splice(rowIndex, 1);
};
</script>
