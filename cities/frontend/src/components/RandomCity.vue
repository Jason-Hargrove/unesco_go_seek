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
      try {
        const response = await fetch('/random/')
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        this.city = await response.json()
      } catch (error) {
        console.error('Error fetching random city:', error)
      }
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
