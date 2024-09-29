<script setup>
const props = defineProps({
    info: {
        colour: String,
        score: Number,
        name: String,
        accountNo: String
    },
    transaction: Boolean
})

// const percentage = props.info.score * 10 + "%"
const percentage = props.info.score * 10 + "%"

console.log(percentage)
</script>

<template>
    <div class="company card rounded-0 px-4 bg-light">
        <div class="card-body">
            <div class="card-title">
                <h1>{{ info.name }}</h1>
                <h6>AC: 123456789</h6>
                <div class="container">
                    <div class="skill" :style="{ 'background-color': props.info.colour, 'width': percentage }">{{
                        props.info.score }}</div>
                </div>
                <div class="mt-3">
                    <button type="button" class="btn" v-bind:class="(transaction ? 'btn-success' : 'btn-primary')">{{
                        transaction ? "Change Payee" : "More Info" }}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/*This is taken from https://www.geeksforgeeks.org/how-to-create-a-progress-bar-using-html-and-css/ */
.container {
    background-color: rgb(192, 192, 192);
    width: 100%;
    border-radius: 15px;
    padding: 0%
}

.skill {
    color: white;
    padding: 1%;
    text-align: right;
    font-size: 20px;
    border-radius: 15px;
}
</style>