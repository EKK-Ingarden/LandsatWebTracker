<template>
  <div h-screen w="25svw" flex justify-center bg-black>
    <div mx-auto mt-32 max-w-full flex flex-col items-center text-left text-gray-300>
      <div text-center text-4xl>
        Watch my pixel form
      </div>
      <div mt-8 flex flex-col items-center text-lg>
        <form flex flex-col items-center w="15svw" @submit="submitForm">
          <FormField v-slot="{ componentField }" name="username" :validate-on-blur="!isFieldDirty">
            <FormItem w="full">
              <FormControl>
                <Input v-bind="componentField" type="text" placeholder="Name" !w="full" />
              </FormControl>
            </FormItem>
          </FormField>
          <FormField v-slot="{ componentField }" name="date" :validate-on-blur="!isFieldDirty">
            <FormItem w="full" flex flex-col items-center>
              <FormControl>
                <Popover>
                  <PopoverTrigger as-child>
                    <Button variant="outline" mt-4 w-full bg-black>
                      <CalendarIcon mr-2 h-4 w-4 />
                      {{ formData.date ? df.format(formData.date.toDate(getLocalTimeZone())) : "Date to capture pixel" }}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent class="w-auto" p-0>
                    <Calendar v-bind="componentField" initial-focus />
                  </PopoverContent>
                </Popover>
              </FormControl>
            </FormItem>
          </FormField>
          <div mt-4 flex gap-2>
            <FormField v-slot="{ componentField }" name="latitude" :validate-on-blur="!isFieldDirty">
              <FormItem>
                <FormControl>
                  <Input v-bind="componentField" type="text" placeholder="Latitude" !w="full" />
                </FormControl>
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="longtitude" :validate-on-blur="!isFieldDirty">
              <FormItem>
                <FormControl>
                  <Input v-bind="componentField" type="text" placeholder="Longtitude" !w="full" />
                </FormControl>
              </FormItem>
            </FormField>
          </div>
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
import { CalendarIcon } from "@radix-icons/vue";

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
  name: z.string().min(2).max(50),
  date: z.string().date(),
  lat: z.number().min(-90).max(90),
  lng: z.number().min(-180).max(180)
}));

const { isFieldDirty, handleSubmit } = useForm({
  validationSchema: formSchema
});

const submitForm = handleSubmit((values) => {
  console.log("dziengiel");
  console.log(values);
});
</script>
