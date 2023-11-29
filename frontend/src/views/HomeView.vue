<template>
    <div>
        <div class="homepage-container">
            <div class="one">Add/Drop Classes</div>
            <div class="two">View Schedule</div>
        </div>
    </div>
</template>

<script>
//For later ;)
</script>

<style >
    .header-container {
        top: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #000000;
        background-color: rgb(34, 75, 165);
    }

    .homepage-container {
        display: grid;
        justify-content: center;
        align-items: center;
        grid-template-columns: repeat(2, 200px);
        row-gap: 40px;
        column-gap: 100px;
        grid-auto-rows: minmax(100px, auto);
    }

    .home {
        text-align: center;
        justify-content: center;
        align-items: center;
        width: 30%;
        height: 50px;
        margin-bottom: 20px;
        font-size: 50px;
        border: 1px solid #000000;
        border-radius: 5px;
        background-color: #5f9fe4;
        padding: 5px;
    }

    .one {
        grid-column: 1; 
        grid-row: 1;
        width: 250px;
        height: 90px;
        text-align: center;
        justify-content: center;
        border: 2px solid #000000;
        border-radius: 5px;
        background-color: #eeeeee;
    }

    .two {
        width: 250px;
        height: 90px;
        text-align: center;
        justify-content: center;
        grid-column: 2;
        grid-row: 1;
        border: 2px solid #000000;
        border-radius: 5px;
        background-color: #eeeeee;
    }
</style>