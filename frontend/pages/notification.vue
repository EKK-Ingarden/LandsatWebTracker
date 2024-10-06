<script setup lang="ts">

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

const notifications = ref([
  {
    date: "11.9.2024", row: 21, path: 37, latitude: 69, longitude: 88,
  }
])

const deleteNotification = (rowIndex: number) => {
  notifications.value.splice(rowIndex, 1);
};


</script>

<template>
<div mt-20 mx-35>
  <p text-xl>
    Incoming Notifications
  </p>

  <div mt-8 border rounded-md border-color="#737373">
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Date</TableHead>
          <TableHead>Row</TableHead>
          <TableHead>Path</TableHead>
          <TableHead>Latitude</TableHead>
          <TableHead>Longitude</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow v-for="(notification, index) in notifications" :key="notification.row">          <TableCell>{{notification.date}}</TableCell>
          <TableCell>{{ notification.row }}</TableCell>
          <TableCell>{{ notification.path }}</TableCell>
          <TableCell>{{ notification.latitude }}</TableCell>
          <TableCell>{{ notification.longitude }}</TableCell>
          <TableCell>
          <button @click="deleteNotification(index)" class="text-red-500 hover:text-red-700">
            DELETE
            </button>
          </TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </div>
</div>
</template>



<style scoped lang="scss">

</style>