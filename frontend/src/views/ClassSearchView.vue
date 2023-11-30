<template>
    <div class="div">
      <div class="space">
        <div class="header">
            <router-link to="/home">Course Scheduler</router-link>
        </div>
        <div class="div-4">
            <input type="text" placeholder="Search for a course" class="search-bar"/>
        </div>
      </div>
    </div>
  </template>

<script>
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
  
  .div-4 {
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
  
  </style>