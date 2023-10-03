<template>
    <div>
        <div class="days-of-week">
            <div class="day-of-week">Monday</div>
            <div class="day-of-week">Tuesday</div>
            <div class="day-of-week">Wednesday</div>
            <div class="day-of-week">Thursday</div>
            <div class="day-of-week">Friday</div>
        </div>
    </div>

</template>

<script>
// Add script here
</script>

<style>
    .days-of-week {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin-left: 200px;
        margin-right: 200px;
        margin-top: 100px;
    }

    .day-of-week {
        font-size: 24px;
        font-weight: bold;
    }
</style>