<template>
  <AlertDialog>
    <AlertDialogTrigger w-full flex justify-center>
      <Button variant="wmpDialog" size="wmpDialog" mx-5>
        Watch My Pixel
      </Button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Watch My Pixel</AlertDialogTitle>
        <AlertDialogDescription>
          Subscribe for notifiation {{ selectedAcquisition }} when landsat passes over this tile.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel>Cancel</AlertDialogCancel>
        <AlertDialogAction @click="watchMyPixel">
          Continue
        </AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>

<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger
} from "~/components/ui/alert-dialog";
import { Button } from "~/components/ui/button";

import apiAuth from "~/utils/api-auth";

const props = defineProps<{
  selectedAcquisition: any
  polygonData: any
  selectedPosition: any
}>();

async function watchMyPixel() {
  const { error } = await apiAuth("/watch_my_pixel/watch", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
    },
    body: {
      wrs_coordinates: {
        path: props.polygonData.coordinates.path,
        row: props.polygonData.coordinates.row
      },
      coordinates: {
        lat: props.selectedPosition.lat,
        lon: props.selectedPosition.lng
      },
      date: props.selectedAcquisition[1] as string
    }
  });

  if (error) {
    console.error(error);
    return;
  }

  await navigateTo("/panel/my_pixel_watches");
}
</script>
