<template>
    <div class="div">
      <div class="space">
        <div class="header">
            <router-link to="/home">Course Scheduler</router-link>
        </div>
        <div class="addcourse">
            <form @submit.prevent="handleAddCourse">
                    <h1>Add Course</h1>
                    <div><input type="text" v-model="course_id" placeholder="Course ID"></div>
                    <div><input id="course_name" v-model="course_name" placeholder="Course Name"></div>
                    <div><input id="total_seats" v-model="total_seats" placeholder="Total Seats"></div>
                    <button type="submit">Create Course</button>
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
        // function to handle login functionality
        async handleAddCourse() {
            try {
                // get data from login form
                const requestData = {
                    httpMethod: 'POST',
                    body: JSON.stringify({
                        course_id: this.course_id,
                        course_name: this.course_name,
                        total_seats: this.total_seats,
                    }),
                };
                
                // await response from api gateway / lambda function
                const response = await fetch(this.baseUrl + '/createcourse', {
                    method: 'POST',
                    mode: 'no-cors',
                    body: JSON.stringify(requestData),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                // respond accordingly
                const responseBody = await response.json();
                const rep = JSON.parse(JSON.stringify(responseBody));
                if (rep.statusCode == 200) {
                    this.$loggedin = true;
                    this.$router.push({name: 'AdminHome'});

                } else {
                    window.alert(rep.body);
                }

            } catch (error) {
                console.error('Error:', error);
                window.alert('Error: Course creation failed' + error + "   " + this.response.json);
            }
        }
    }
};

// waits for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    // get container, and button elements
    const container = document.getElementById('container');
    const createBtn = document.getElementById('create');

    // click event listeners for buttons
    createBtn.addEventListener('click', () => {
        // add active class to container
        container.classList.add("active");
    });

});
</script>


<style >
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
  
  .addcourse {
    max-width: 100%;
    border-radius: 10px;
    align-self: center;
    margin-top: 115px;
    width: 522px;
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