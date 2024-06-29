<template>
  <div class="random-city">
    <button @click="fetchRandomCity" class="btn btn-primary">
      Get Random City
    </button>
    <div v-if="city">
      <h3>{{ city.name }}</h3>
      <p>{{ city.country }}</p>
      <p>{{ city.specialization }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      city: null,
    }
  },
  methods: {
    async fetchRandomCity() {
      const response = await fetch('/cities/random/')
      this.city = await response.json()
    },
  },
}
</script>

<style scoped>
.random-city {
  text-align: center;
  margin-top: 20px;
}
</style>
