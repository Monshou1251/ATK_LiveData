<template>
    <div>
      <a-input-search v-model:value="value" placeholder="search..."  />
      <br />
      <!-- <br />
      <a-input-search
        v-model:value="value"
        placeholder="search"
        loading
        enter-button
      /> -->
    </div>
  </template>
  <script>
  import { defineComponent, ref } from 'vue';
  export default defineComponent({
    setup() {
      const value = ref('');
      return {
        value,
      };
    },
  });
  </script>