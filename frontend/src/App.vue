<template>
  <WeeklyCalendar/>
</template>

<script>
import WeeklyCalendar from './components/WeeklyCalendar.vue'
import ClassSearch from './components/ClassSearch.vue'

export default {
  name: 'App',
  components: {
    WeeklyCalendar
  }
}
</script>

<style>
#app {
  font-family: Roboto, Arial, sans-serif;
  margin-top: 20px;
}
</style>
