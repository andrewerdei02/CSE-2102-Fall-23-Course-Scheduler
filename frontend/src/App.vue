<template>
  <HomePage/>
</template>

<script>
import WeeklyCalendar from './components/WeeklyCalendar.vue'
import ClassSearch from './components/ClassSearch.vue'
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Roboto, Arial, sans-serif;
  margin-top: 20px;
}
</style>
