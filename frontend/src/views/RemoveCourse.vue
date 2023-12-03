<template>
    <div class="div">
      <div class="space">
        <div class="header">
          <router-link to="/CourseAdjust">Go Back</router-link>
        </div>
        <div class="removecourse">
          <h1>Remove Course</h1>
          <div class="columns">
          <form @submit.prevent="handleRemoveCourse">
            <div><input type="text" v-model="course_id" placeholder="Course ID"></div>
            <div><input id="course_name" v-model="course_name" placeholder="Course Name"></div>
              <button type="submit">Remove Course</button>
          </form>
            </div>
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
  
<style >
    .columns {
    display: grid;
    grid-template-columns: repeat(2, 1fr); 
    gap: 20px;
  }
    .course-selector-container {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 32px 20px;
    font: 400 40px Inter, sans-serif;
  }
  .search-bar {
    width: 100%; 
    max-width: 400px; 
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 20px;
    }
  .div {
    background-color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100vw;
    height: 100vh;
    padding: 21px 20px 50px;
  }
  .space {
    display: flex;
    margin-bottom: 422px;
    width: 859px;
    max-width: 100%;
    flex-direction: column;
    align-items: center;
  }

  .div-3 {
    color: #000;
    max-width: 400px;
    background-color: #7ba8ff;
    justify-content: center;
    align-items: center;
    padding: 32px 20px;
    font: 400 48px Inter, sans-serif;
  }
  
  .removecourse {
    max-width: 100%;
    border-radius: 10px;
    align-self: center;
    margin-top: 115px;
    width: 600px;
    justify-content: center;
    align-items: center;
    padding: 20px;
    font: 400 32px Inter, sans-serif;
  }
  .search {
    align-items: center;
    justify-content: center;
  }
</style>