<template>
    <div class="div">
      <div class="space">
        <div class="header">
            <router-link to="/AdminHome">Course Scheduler</router-link>
        </div>
        <div class="div-4">
            <table striped hover :items="items"></table>
                
        </div>
      </div>
    </div>
  </template>
  
<script>
    export default {
        data() {
        return {
            items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
        }
    }
}
</script>
  
  
  <style>
  .header {
    color: #000;
    align-self: center;
    background-color: #7ba8ff;
    width: 634px;
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