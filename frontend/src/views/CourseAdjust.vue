<template>
  <div class="div">
    <div class="space">
      <div class="header">
        <router-link to="/AdminHome">Course Scheduler</router-link>
      </div>
      <div class="container">
        <div class="data-section">
          <div class="course-list" v-if="courses && courses.length > 0">
            <div class="course" v-for="course in courses" :key="course.course_id">
              <div class="course-info">
                <p><strong>Course ID:</strong> {{ course.course_id }}</p>
                <p><strong>Course Name:</strong> {{ course.course_name }}</p>
                <p><strong>Total Seats:</strong> {{ course.total_seats }}</p>
                <p><strong>Taken Seats:</strong> {{ course.taken_seats }}</p>
              </div>
            </div>
          </div>
          <div v-else>
            <p>No courses available.</p>
          </div>
        </div>
        <div class="add-course">
          <a href="/AddCourse">
            <button>Add Course</button>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [], // Initialize courses as an empty array
    };
  },
  mounted() {
    this.fetchCourses(); // Call fetchCourses method when the component is mounted
  },
  methods: {
    async fetchCourses() {
      try {
        const response = await fetch('https://e6uyvie1q8.execute-api.us-east-1.amazonaws.com/Prod/courses');
        if (response.ok) {
          const data = await response.json();
          // Parse the stringified JSON if present in the response body
          const responseBody = typeof data.body === 'string' ? JSON.parse(data.body) : data.body;
          this.courses = responseBody || []; // Set courses data from the API response
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
/* Your existing styles */

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

.space {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 20px;
}

.data-section {
  flex: 1;
}

.course-list {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
}

.course {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  width: 250px;
}

.add-course {
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #7ba8ff;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #5f8be3;
}
</style>
