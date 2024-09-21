<template>
  <div h-screen w="25svw" flex justify-center bg-black>
    <div mx-auto mt-32 max-w-full flex flex-col items-center text-left text-gray-300>
      <div text-center text-4xl>
        Watch my pixel form
      </div>
      <div mt-8 flex flex-col items-center text-lg>
        <form flex flex-col items-center w="15svw" @submit.prevent="submitForm">
          <FormField v-slot="{ componentField }" name="name" :validate-on-blur="!isFieldDirty">
            <FormItem w="full">
              <FormMessage />
              <FormControl>
                <Input v-bind="componentField" type="text" placeholder="Name" !w="full" />
              </FormControl>
            </FormItem>
          </FormField>
          <FormField v-slot="{ componentField }" name="date" :validate-on-blur="!isFieldDirty">
            <FormItem w="full" flex flex-col items-center>
              <FormMessage />
              <FormControl>
                <div>
                  <Popover>
                    <PopoverTrigger as-child>
                      <Button variant="outline" mt-4 w-full bg-black>
                        <CalendarIcon mr-2 h-4 w-4 />
                        {{ dateValue ? df.format(toDate(dateValue)) : "Date to capture pixel" }}
                      </Button>
                    </PopoverTrigger>
                    <PopoverContent class="w-auto" p-0>
                      <Calendar
                        v-bind="componentField"
                        v-model="dateValue"
                        initial-focus
                        @update:model-value="(v) => {
                          if (v) {
                            setFieldValue('date', v.toString())
                          }
                          else {
                            setFieldValue('date', undefined)
                          }
                        }"
                      />
                    </PopoverContent>
                  </Popover>
                </div>
              </FormControl>
            </FormItem>
          </FormField>
          <div mt-4 flex gap-2>
            <FormField v-slot="{ componentField }" name="lat" :validate-on-blur="!isFieldDirty">
              <FormItem>
                <FormMessage />
                <FormControl>
                  <Input v-bind="componentField" type="text" placeholder="Latitude" !w="full" />
                </FormControl>
              </FormItem>
            </FormField>
            <FormField v-slot="{ componentField }" name="lng" :validate-on-blur="!isFieldDirty">
              <FormItem>
                <FormMessage />
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
import { DateFormatter, parseDate } from "@internationalized/date";
import { toTypedSchema } from "@vee-validate/zod";
import { useForm } from "vee-validate";
import * as z from "zod";
import { CalendarIcon } from "@radix-icons/vue";
import { toDate } from "radix-vue/date";

const df = new DateFormatter("en-US", {
  dateStyle: "long"
});

const formSchema = toTypedSchema(z.object({
  name: z.string().min(2).max(50),
  date: z.string().date(),
  lat: z.number().min(-90).max(90),
  lng: z.number().min(-180).max(180)
}));

const { isFieldDirty, handleSubmit, setFieldValue, values } = useForm({
  validationSchema: formSchema
});

watch(
  () => values.lat,
  (newLat) => {
    if (newLat !== undefined) {
      setFieldValue("lat", Number(newLat));
    }
  }
);

watch(
  () => values.lng,
  (newLng) => {
    if (newLng !== undefined) {
      setFieldValue("lng", Number(newLng));
    }
  }
);

const dateValue = computed({
  get: () => values.date ? parseDate(values.date) : undefined,
  set: (val) => val
});

const submitForm = handleSubmit((values) => {
  console.log(values);
});
</script>
