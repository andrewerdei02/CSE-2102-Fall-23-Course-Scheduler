<template>
  <div class="div">
    <div class="header">
      <router-link to="/AdminHome">Return to Home</router-link>
    </div>
    <div class="course-list">
      <div v-if="courses && courses.length > 0" class="grid-container">
        <div v-for="course in courses" :key="course.course_id" class="course">
          <div class="course-info">
            <p><strong>Course ID:</strong> {{ course.course_id }}</p>
            <p><strong>Course Name:</strong> {{ course.course_name }}</p>
            <p v-if="course.professor_name"><strong>Professor:</strong> {{ course.professor_name }}</p> 
            <p v-if="course.days_of_week"><strong>Days of Week:</strong> {{ course.days_of_week }}</p> 
            <p v-if="course.class_time"><strong>Class Time:</strong> {{ course.class_time }}</p>
            <p><strong>Total Seats:</strong> {{ course.total_seats }}</p>
            <p><strong>Taken Seats:</strong> {{ course.taken_seats }}</p> 
          </div>
        </div>
      </div>
      <div v-else>
        <p>No courses available.</p>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      courses: [],
    };
  },
  mounted() {
    this.fetchCourses();
  },
  methods: {
    async fetchCourses() {
      try {
        const response = await fetch('https://e6uyvie1q8.execute-api.us-east-1.amazonaws.com/Prod/courses');
        if (response.ok) {
          const data = await response.json();
          const responseBody = typeof data.body === 'string' ? JSON.parse(data.body) : data.body;
          this.courses = responseBody || [];
        } else {
          console.error('Error fetching courses:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    },
  },
};
</script>
  
  
<style>
.div {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  padding: 21px 20px 50px;
}

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

.course-list {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, minmax(200px, 1fr));
  gap: 5px;
}

.course {
  border: 1px solid #ccc;
  padding: 16px;
  border-radius: 8px;
  background-color: #fff;
}

</style>
  