<template>
    <div class="div">
      <div class="div-2">
        <div class="header">
            <router-link to="/home">Course Scheduler</router-link>
        </div>
        <div class="div-4">
          <div class="div-5">
            <div class="column"><div class="cal">
                <router-link to="/home">Calendar</router-link>
            </div></div>
            <div class="column-2"><div class="class">
                <router-link to="/ClassSearch">Class Search</router-link>
            </div></div>
          </div>
        </div>
        <div class="div-8">
          <div class="div-9">
            <div class="column"><div class="div-10"></div></div>
            <div class="column-3"><div class="div-11"></div></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  
  <style>
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
  .div-2 {
    display: flex;
    margin-bottom: 300px;
    width: 859px;
    max-width: 100%;
    flex-direction: column;
    align-items: center;
  }
  
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

  .cal {
    color: #000;
    background-color: #d9d9d9;
    flex-grow: 1;
    justify-content: center;
    align-items: center;
    width: 300px;
    padding: 46px 20px;
    font: 400 40px Inter, sans-serif;
  }
  
  .class {
    color: #000;
    background-color: #d9d9d9;
    flex-grow: 1;
    justify-content: center;
    align-items: center;
    width: 300px;
    padding: 46px 20px;
    font: 400 40px Inter, sans-serif;
  }

  .div-4 {
    align-self: center;
    margin-top: 211px;
  }

  .div-5 {
    gap: 20px;
    display: flex;
  }

  .column {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 50%;
    margin-left: 0px;
  }
  
  .column-2 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 50%;
    margin-left: 20px;
  }

  .div-8 {
    align-self: stretch;
    margin-top: 53px;
  }
  
  .div-9 {
    gap: 20px;
    display: flex;
  }
  
  .div-10 {
    background-color: #d9d9d9;
    display: flex;
    width: 100%;
    height: 128px;
    flex-direction: column;
    flex: 1;
  }
  
  .column-3 {
    display: flex;
    flex-direction: column;
    line-height: normal;
    width: 50%;
    margin-left: 20px;
  }
  
  .div-11 {
    background-color: #d9d9d9;
    display: flex;
    width: 100%;
    height: 128px;
    flex-direction: column;
    flex: 1;
  }
  
  </style>