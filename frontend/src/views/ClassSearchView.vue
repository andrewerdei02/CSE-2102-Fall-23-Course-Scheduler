<template>
    <div class="course-selector-container">
        <div class="course-selector">
            <h2 class="title">Course Selector</h2>
            <input type="text" v-model="search" placeholder="Search for a course" class="search-bar"/>
        </div>
    </div>
  </template>

<script>
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