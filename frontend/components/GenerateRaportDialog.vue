<template>
  <AlertDialog>
    <AlertDialogTrigger as-child>
      <Button variant="outline">
        Generate Report
      </Button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Do you want to generate report?</AlertDialogTitle>
        <AlertDialogDescription>
          This action may take a while, so be careful
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel>Cancel</AlertDialogCancel>
        <AlertDialogAction @click="generateReport">
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
} from "@/components/ui/alert-dialog";
import { Button } from "@/components/ui/button";

const props = defineProps<{
  sceneId: string
}>();

async function generateReport() {
  await useApi("/report/generate_report", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${useSupabaseSession().value?.access_token}`
    },
    query: {
      scene_id: props.sceneId
    }
  });
  navigateTo("/panel/reports");
}
</script>
