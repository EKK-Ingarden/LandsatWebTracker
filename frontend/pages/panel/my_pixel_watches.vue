<template>
  <div mx-35 mt-20>
    <h1 text-10>
      Incoming Notifications
    </h1>
    <span>Your upcoming "watch my pixel" notifications</span>

    <div mt-8 border rounded-md border-color="#737373">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Date</TableHead>
            <TableHead>Path</TableHead>
            <TableHead>Row</TableHead>
            <TableHead>Latitude</TableHead>
            <TableHead>Longitude</TableHead>
            <TableHead>Form</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow v-if="notifications.length === 0">
            <div p8>
              You don't have any notifications!
              Go to <NuxtLink to="/panel/watch_my_pixel" font-bold underline>
                watch my pixel
              </NuxtLink> to subscribe to one!
            </div>
          </TableRow>
          <TableRow v-for="(notification, index) in notifications" v-else :key="index">
            <TableCell>{{ formatDate(notification.datetime) }}</TableCell>
            <TableCell>{{ notification.path }}</TableCell>
            <TableCell>{{ notification.row }}</TableCell>
            <TableCell>{{ notification.latitude }}</TableCell>
            <TableCell>{{ notification.longitude }}</TableCell>
            <TableCell>Email</TableCell>
            <!--            todo: maybe bring back remove -->
            <!--            <TableCell> -->
            <!--              <button class="text-red-500 hover:text-red-700" @click="deleteNotification(index)"> -->
            <!--                DELETE -->
            <!--              </button> -->
            <!--            </TableCell> -->
          </TableRow>
        </TableBody>
      </Table>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from "@/components/ui/table";

const notifications = ref<any[]>([]);

// const deleteNotification = (rowIndex: number) => {
//   notifications.value.splice(rowIndex, 1);
// };

const { data, error } = await useApi("/watch_my_pixel/get_list", {
  headers: {
    Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
  }
});

if (data.value) {
  notifications.value = data.value;
} else {
  console.error(error);
}

function formatDate(date_str: string) {
  const date = new Date(date_str);
  const options = {
    weekday: "long",
    year: "numeric",
    month: "short",
    day: "numeric"
  };
  return date.toLocaleDateString("en-US", options);
}
</script>
