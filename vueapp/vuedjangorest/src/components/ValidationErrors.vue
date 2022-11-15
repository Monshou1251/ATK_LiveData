<template>
  <ul class="error-messages">
    <li v-for="errorMessage in errorMessages" :key="errorMessage">
      {{ errorMessage }}
    </li>
  </ul>
  <!-- <div>Here are sharable validation errors {{ validationErrors }}</div> -->
</template>

<script>
export default {
  name: 'McvValidationErrors',
  props: {
    validationErrors: {
      type: Object,
      required: true,
    },
  },
  computed: {
    errorMessages() {
      if (this.validationErrors.detail) {
        // console.log('errors', this.validationErrors.detail)
        return this.validationErrors
      } else {
        // console.log('errors', this.validationErrors)

        return Object.keys(this.validationErrors).map((name) => {
          const messages = this.validationErrors[name].join(', ')
          return `${name} : ${messages}`
        })
      }
    },
  },
}
</script>

<style>
.error-messages {
  color: #b85c5c !important;
  font-weight: bold;
  /* font-family: 'Source Sans Pro', sans-serif; */
  font-size: 14px;
  line-height: 1.5;
}
</style>
