<template>
  <div h-screen w="1/4" flex justify-center bg-black>
    <div mx-auto mt-32 max-w-full flex flex-col text-left text-gray-300>
      <div text-center text-4xl>
        Watch my pixel form
      </div>
      <div mt-8 text-lg>
        <form flex flex-col items-center @submit.prevent="submitForm">
          <input
            id="name" v-model="formData.name" type="text" w="2/3" border-b-3 border-b-gray-700 rounded-sm bg-black
            placeholder="Name" focus="outline-none" autocomplete="off"
          >
          <div w="2/3" mt-4 flex gap-10>
            <input
              id="lat" v-model="formData.lat" type="text" w="1/2" border-b-3 border-b-gray-700 rounded-sm bg-black
              placeholder="Latitude" focus="outline-none" autocomplete="off"
            >
            <input
              id="lng" v-model="formData.lng" type="text" w="1/2" border-b-3 border-b-gray-700 rounded-sm bg-black
              placeholder="Longtitude" focus="outline-none" autocomplete="off"
            >
          </div>
          <div mt-8 flex flex-col items-center>
            <label for="date">Date to capture pixel</label>
            <Calendar
              v-model="formData.date"
              calendar-label="Date to capture pixel"
            />
          </div>
          <div mt-4>
            <Button type="submit">
              Submit
            </Button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
const formData = ref({
  name: "",
  date: "",
  lat: "",
  lng: ""
});

function submitForm() {
  console.log(formData);
};
</script>
