<template>
  <div mx-35 mt-20>
    <h1 text-2xl>
      Reports
    </h1>
    <span>Your generated reports</span>

    <div mt-8 border rounded-md border-color="#737373">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Is Processed</TableHead>
            <TableHead>Created at</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Scene</TableHead>
            <TableHead><!-- extends table header to full width --></TableHead>
            <TableHead><!-- extends table header to full width --></TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(report, index) in reports" :key="index">
            <TableCell>{{ report.is_processed }}</TableCell>
            <TableCell>{{ report.created_at }}</TableCell>
            <TableCell>{{ report.scene_id }}</TableCell>
            <TableCell><NuxtLink :to="`/panel/report/${report.scene_id}`"><img class="i-material-symbols-light:open-in-new" text-2xl></NuxtLink></TableCell>
            <TableCell>
              <button class="text-red-500 hover:text-red-700">
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
const reports = ref<{
  scene_id: string
  is_processed: boolean
  created_at: string
  raw_data: string | null
}[]>();

const { data, error } = useApi("/report/get_reports", {
  headers: {
    Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
  }
});

if (data.value) {
  reports.value = data.value;
}
</script>
