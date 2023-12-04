<template>
  <div class="container1">
    <div class="home-button-container">
      <button @click="$router.push('/home')">Back to Home</button>
    </div>
    <div class="content">
      <div class="user-input">
        <input v-model="userId" type="text" placeholder="Enter Username" class="larger-input" />
        <button @click="fetchUserCourses">Submit</button>
      </div>
      <div class="course-list" v-if="coursesFetched || (courses && courses.length > 0)">
        <div v-if="courses && courses.length > 0" class="grid-container">
          <div v-for="course in courses" :key="course.course_id" class="course">
            <div class="course-info">
              <p><strong>Course ID:</strong> {{ course.course_id }}</p>
              <p><strong>Course Name:</strong> {{ course.course_name }}</p>
              <p v-if="course.professor_name"><strong>Professor:</strong> {{ course.professor_name }}</p> 
              <p v-if="course.days_of_week"><strong>Days of Week:</strong> {{ course.days_of_week }}</p> 
              <p v-if="course.class_time"><strong>Class Time:</strong> {{ course.class_time }}</p>
            </div>
          </div>
        </div>
        <div v-else>
          <p>No courses available for the provided username.</p>
        </div>
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
        if (this.userId.trim() === '') {
          window.alert("Please don't leave form blank");
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
.home-button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px; 
}

.home-button-container button {
    background-color: #7ba8ff;
    color: #000;
    font-family: Inter, sans-serif;
    font-size: 40px;
    font-weight: 400;
    padding: 32px 20px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    text-decoration: underline;
    transition: background-color 0.3s ease-in-out;
    width: 600px;
    height: 100px;
}

.container1 {
  text-align: center;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.user-input {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.larger-input {
  width: 300px;
  height: 30px; 
  margin-bottom: 10px; 
}

button {
  width: 150px;
  margin-bottom: 40px; 
}
</style>
