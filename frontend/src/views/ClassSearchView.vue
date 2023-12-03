<template>
  <div class="div">
    <div class="header">
      <router-link to="/home">Course Scheduler</router-link>
    </div>
    <h2>Enter the information for a course from the available courses to add/drop</h2>
    <div class="space2"></div>
    <div class="columns">
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
      <div v-else>
        <p>No courses available.</p>
      </div>
      <div class="columns">
      <form @submit.prevent="handleAddCourse">
        <div><input type="text" v-model="course_id" placeholder="Course ID"></div>
        <button type="submit">Add Course</button>
      </form>
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

  data() {
    return {
      courses: [],
      user_id: '',
      course_id: '',
      baseUrl: 'https://e6uyvie1q8.execute-api.us-east-1.amazonaws.com/Prod',
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
    async handleAddCourse() {
        try {
          const user_id = this.$store.state.username
          const requestData = {
            httpMethod: 'POST',
            body: JSON.stringify({
              user_id: user_id,
              course_id: this.course_id,
            }),
          };
  
          const response = await fetch(this.baseUrl + '/add_course', {
            method: 'POST',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
          });
          
          const responseBody = await response.json();
          const rep = JSON.parse(JSON.stringify(responseBody));
          if (rep.statusCode == 201) {
            window.alert(rep.body)
          } else {
            window.alert(rep.body)
          }
        
        } catch (error) {
          console.error('Error:', error);
          window.alert('Error: Failed to add course ' );
        }
      },
      async handleDropCourse() {
        try {
          const requestData = {
            httpMethod: 'DELETE',
            body: JSON.stringify({
              course_id: this.course_id,
              course_name: this.course_name,
            }),
          };
  
          const response = await fetch(this.baseUrl + '/deletecourse', {
            method: 'DELETE',
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData)
          });
          
          const responseBody = await response.json();
          const rep = JSON.parse(JSON.stringify(responseBody));
          if (rep.statusCode == 201) {
            window.alert(rep.body)
          } else {
            window.alert(rep.body)
          }
        
        } catch (error) {
          console.error('Error:', error);
          window.alert('Error: Course removal failed ' );
        }
      }
  },
};
</script>

<style>
.space2 {
  height: 100px;
}
.buttonsmall {
  width: 150px;
  height: 30px;
}
.columns {
    display: grid;
    grid-template-columns: repeat(2, 1fr); 
    gap: 20px; 
  }
  
.div {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: top;
  width: 100vw;
  height: 100vh;
  padding: 21px 20px 50px;
}

.header {
  color: #000;
  align-self: center;
  background-color: #7ba8ff;
  width: 634px;
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