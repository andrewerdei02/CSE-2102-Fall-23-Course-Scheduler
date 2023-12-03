<template>
  <div class="main-container">
    <div class="space">
      <div class="header">
        <router-link to="/CourseAdjust">Go Back</router-link>
      </div>
      <div class="addcourse">
        <form @submit.prevent="handleAddCourse" class="add-form">
          <h1>Add Course</h1>
          <div><input type="text" v-model="course_id" placeholder="Course ID" class="input-field"></div>
          <div><input id="course_name" v-model="course_name" placeholder="Course Name" class="input-field"></div>
          <div><input id="total_seats" v-model="total_seats" placeholder="Total Seats" class="input-field"></div>
          <button id="create" type="submit">Create Course</button>
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
      total_seats: '',
      baseUrl: 'https://e6uyvie1q8.execute-api.us-east-1.amazonaws.com/Prod'
    };
  },
  methods: {
    async handleAddCourse() {
      try {
        const requestData = {
          httpMethod: 'POST',
          body: JSON.stringify({
            course_id: this.course_id,
            course_name: this.course_name,
            total_seats: this.total_seats,
          }),
        };

        const response = await fetch(this.baseUrl + '/createcourse', {
          method: 'POST',
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
        window.alert('Error: Course creation failed');
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

.header {
  color: #000;
  max-width: 400px;
  background-color: #7ba8ff;
  padding: 32px 20px;
  font: 400 48px Inter, sans-serif;
  margin-bottom: 20px;
}

.addcourse {
  max-width: 522px;
  border-radius: 10px;
  padding: 20px;
  font: 400 32px Inter, sans-serif;
  background-color: #fff;
}

.add-form {
  display: flex;
  flex-direction: column;
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

#create {
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
