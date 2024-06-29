<template>
  <div>
    <RandomCity />
  </div>
</template>

<script>
import RandomCity from './components/RandomCity.vue'

export default {
  name: 'App',
  components: {
    RandomCity,
  },
}
</script>

<style>
@import '~bootstrap/dist/css/bootstrap.css';
@import '~bootstrap-vue/dist/bootstrap-vue.css';
</style>
