<template>
  <div h-screen w="1/4" flex justify-center bg-black>
    <div mx-auto mt-32 max-w-full flex flex-col items-center text-left text-gray-300>
      <div text-center text-4xl>
        Watch my pixel form
      </div>
      <div mt-8 flex flex-col items-center text-lg>
        <form flex flex-col items-center @submit.prevent="submitForm">
          <FormField name="username" :validate-on-blur="!isFieldDirty">
            <FormItem>
              <FormControl>
                <Input v-model="formData.name" type="text" placeholder="Name" !w="full" />
              </FormControl>
            </FormItem>
          </FormField>
          <FormField name="username" :validate-on-blur="!isFieldDirty">
            <FormItem w="full" flex flex-col items-center>
              <FormControl>
                <Popover>
                  <PopoverTrigger as-child>
                    <Button variant="outline" mt-4 w-full bg-black>
                      {{ formData.date ? df.format(formData.date.toDate(getLocalTimeZone())) : "Date to capture pixel" }}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent class="w-auto p-0">
                    <Calendar v-model="formData.date" initial-focus />
                  </PopoverContent>
                </Popover>
              </FormControl>
            </FormItem>
          </FormField>
          <FormField name="latitude" :validate-on-blur="!isFieldDirty">
            <FormItem>
              <FormControl>
                <Input v-model="formData.lat" type="text" placeholder="Latitude" />
              </FormControl>
            </FormItem>
          </FormField>
          <FormField name="longtitude" :validate-on-blur="!isFieldDirty">
            <FormItem>
              <FormControl>
                <Input v-model="formData.lng" type="text" placeholder="Longtitude" />
              </FormControl>
            </FormItem>
          </FormField>
          <Button type="submit" mt-8>
            Submit
          </Button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { DateFormatter, getLocalTimeZone } from "@internationalized/date";
import { toTypedSchema } from "@vee-validate/zod";
import { useForm } from "vee-validate";
import * as z from "zod";

const df = new DateFormatter("en-US", {
  dateStyle: "long"
});

const formData = ref({
  name: "",
  date: "",
  lat: "",
  lng: ""
});

const formSchema = toTypedSchema(z.object({
  username: z.string().min(2).max(50)
}));

const { isFieldDirty, handleSubmit } = useForm({
  validationSchema: formSchema
});

const submitForm = handleSubmit((values) => {
  toast({
    title: "You submitted the following values:",
    description: h("pre", { class: "mt-2 w-[340px] rounded-md bg-slate-950 p-4" }, h("code", { class: "text-white" }, JSON.stringify(values, null, 2)))
  });
});
</script>
