<template>
  <div class="div">
    <div class="header">
      <router-link to="/AdminHome">Course Scheduler</router-link>
    </div>
    <div class="add-remove-buttons">
      <div class="add-course">
        <router-link to="/AddCourse">
          <button>Add Course</button>
        </router-link>
      </div>
      <div class="remove-course">
        <router-link to="/RemoveCourse">
          <button>Remove Course</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
</script>

<style>
.header {
  color: #000;
  align-self: center;
  background-color: #7ba8ff;
  width: 634px;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 32px 20px;
  font: 400 40px Inter, sans-serif;
}

.add-remove-buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 20px;
}

.add-course,
.remove-course {
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #ff7b7b;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #9c1414;
}
</style>
