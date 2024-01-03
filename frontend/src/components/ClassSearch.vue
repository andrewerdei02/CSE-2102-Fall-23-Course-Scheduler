<template>
    <div class="course-selector-container">
        <div class="course-selector">
            <h2 class="title">Course Selector</h2>
            <input type="text" v-model="search" placeholder="Search for a course" class="search-bar"/>
        <table border="1px">
            <tr>
                <td>Class Name</td>
                <td>Professor</td>
            </tr>
            <tr v-for="item in filteredClasses" :key="item.className" @click="showCourseDetails(item)" style="cursor: pointer;">
                <td>{{ item.className }}</td>
                <td>{{ item.professor }}</td>
            </tr>
        </table>

        <div v-if="selectedCourse">
            <h3>Selected Course Details</h3>
            <p><strong>Class Name:</strong> {{ selectedCourse.className }}</p>
            <p><strong>Professor:</strong> {{ selectedCourse.professor }}</p>
            <p>More Info</p>
            <!-- Add more details as needed -->
        </div>
        </div>
    </div>
</template>

  <script>
   export default{
    name: 'ClassSearch',
    data(){
        return {
            post: [],
            search: '',
            selectedCourse: null
        }
    },
    methods: {
      async getResult(){
        const response = await fetch('https://rxyqf233x8.execute-api.us-east-1.amazonaws.com/prod2/classes')
        const data = await response.json()
        this.post = data.classes
        console.log(data.classes)
      },
      showCourseDetails(course) {
        this.selectedCourse = course;
      },
    },
    mounted(){
        this.getResult()
    },
    computed: {
        filteredClasses() {
        const query = this.search.toLowerCase();
        return this.post.filter(
            (post) => post.className.toLowerCase().includes(query)); 
    }
  }
   }
  </script>
  
<style >
    .course-selector-container {
    display: flex;
    justify-content: center;
    align-items: flex-start; 
    min-height: 100vh;
    padding: 20px; 
    }

    .title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 24px;
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
</style>
