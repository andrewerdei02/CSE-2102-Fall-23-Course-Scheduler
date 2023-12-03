<template>
  <div class="welcome-page">
    <div class="header">
      <router-link to="/">Return to Login</router-link>
    </div>
    <div class="welcome-container">
      <div class="welcome-header">
        <h1>Welcome, {{ $store.state.username }}!</h1>
      </div>
      <div class="link-container">
        <div class="class-link">
          <router-link to="/ClassSearch">Add/Drop Classes</router-link>
        </div>
        <div class="schedule-link">
          <router-link to="/ViewSchedule">View Your Schedule</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  beforeCreate() {
    const vm = this;
    console.log(vm.$store.state.username);
  },
};
</script>

<style>
.welcome-page {
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  align-self: flex-start;
  margin-bottom: 20px;
}

.welcome-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.welcome-header h1 {
  color: #000;
  font-size: 40px;
}

.link-container {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.class-link,
.schedule-link {
  margin: 0 10px;
}

.class-link a,
.schedule-link a {
  display: block;
  color: #000;
  background-color: #6d92dd;
  width: 250px;
  padding: 46px 20px;
  text-align: center;
  font: 400 35px Inter, sans-serif;
}
</style>
