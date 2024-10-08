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
            <TableHead>Status</TableHead>
            <TableHead>Created at</TableHead>
            <TableHead>Scene</TableHead>
            <TableHead>Action</TableHead>
            <TableHead />
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-for="(report, index) in data" :key="index">
            <TableCell>{{ report.is_processed ? "Processed" : "Processing..." }}</TableCell>
            <TableCell>{{ report.created_at }}</TableCell>
            <TableCell>{{ report.scene_id }}</TableCell>
            <TableCell>
              <NuxtLink :to="`/panel/report/${report.scene_id}`">
                <img class="i-material-symbols-light:open-in-new" text-2xl>
              </NuxtLink>
            </TableCell>
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
import type { RealtimeChannel } from "@supabase/supabase-js";

const supabase = useSupabaseClient();

const { data, refresh } = await useApi("/report/get_reports", {
  headers: {
    Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
  }
});

let realtimeChannel: RealtimeChannel;

onMounted(() => {
  realtimeChannel = supabase.channel("public:reports").on(
    "postgres_changes",
    { event: "*", schema: "public", table: "reports" },
    () => {
      refresh();
    }
  );
  realtimeChannel.subscribe();
});

onUnmounted(() => {
  supabase.removeChannel(realtimeChannel);
});
</script>
