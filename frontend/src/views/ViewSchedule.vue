<template>
  <div class="div">
    <div class="header">
      <router-link to="/home">Course Scheduler</router-link>
    </div>
    <div class="user-input">
      <input v-model="userId" type="text" placeholder="Enter Username" />
      <button @click="fetchUserCourses">Submit</button>
    </div>
    <div class="course-list">
      <div v-if="courses && courses.length > 0" class="grid-container">
        <div v-for="course in courses" :key="course.course_id" class="course">
          <div class="course-info">
            <p><strong>Course ID:</strong> {{ course.course_id }}</p>
            <p><strong>Course Name:</strong> {{ course.course_name }}</p>
            <p><strong>Total Seats:</strong> {{ course.total_seats }}</p>
            <p><strong>Taken Seats:</strong> {{ course.taken_seats }}</p>
          </div>
        </div>
      </div>
      <div v-else-if="coursesFetched">
        <p>No courses available for the provided username.</p>
      </div>
      <div v-else>
        <p>Please enter your username to view your classes!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userId: '',
      courses: [],
      coursesFetched: false
    };
  },
  methods: {
    async fetchUserCourses() {
      try {
        // check if form is left blank
        if (this.userId.trim() === '') {
          window.alert('Please don\'t leave form blank');
          return;
        }
        const requestData = {
          httpMethod: 'POST',
          body: JSON.stringify({
            user_id: this.userId
          }),
        };

        const response = await fetch('https://lk4nwfjgt6.execute-api.us-east-1.amazonaws.com/Prod/view_schedule', {
          method: 'POST',
          body: JSON.stringify(requestData),
        });
        
        const responseData = await response.json();
        const responseBody = JSON.parse(responseData.body);

        if (response.ok) {
          if (Array.isArray(responseBody)) {
            this.courses = responseBody;
            this.coursesFetched = true;
          } else {
            window.alert(responseBody);
            this.coursesFetched = false;
          }
        } else {
          window.alert(responseBody);
          this.coursesFetched = false;
        }
      } catch (error) {
        console.error('Error fetching courses:', error);
        this.courses = [];
        this.coursesFetched = false;
      }
    }
  }
};
</script>

<style>
/* Your existing styles */
</style>
