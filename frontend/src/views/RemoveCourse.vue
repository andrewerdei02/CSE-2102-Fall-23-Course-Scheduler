<template>
  <div class="main-container">
    <div class="space">
      <div class="header2">
        <router-link to="/CourseAdjust">Go Back</router-link>
      </div>
      <div class="removecourse">
        <h1>Remove Course</h1>
        <form @submit.prevent="handleRemoveCourse" class="remove-form">
          <div class="columns">
            <div><input type="text" v-model="course_id" placeholder="Course ID" class="input-field"></div>
          </div>
          <button id="removebut" type="submit">Remove Course</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        course_id: '',
        course_name: '',
        baseUrl: 'https://e6uyvie1q8.execute-api.us-east-1.amazonaws.com/Prod'
      };
    },
    methods: {
      async handleRemoveCourse() {
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
    }
  };
</script>

<style>
.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.space {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header2 {
  color: #000;
  max-width: 400px;
  background-color: #7ba8ff;
  padding: 32px 20px;
  font: 400 48px Inter, sans-serif;
  margin-bottom: 20px;
}

.removecourse {
  max-width: 600px;
  border-radius: 10px;
  padding: 20px;
  font: 400 32px Inter, sans-serif;
  background-color: #fff;
}

.remove-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.columns {
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-field {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 20px;
}

#removebut {
  width: 100%;
  padding: 10px;
  font-size: 20px;
  border: none;
  border-radius: 5px;
  background-color: #7ba8ff;
  color: white;
  cursor: pointer;
}
</style>
