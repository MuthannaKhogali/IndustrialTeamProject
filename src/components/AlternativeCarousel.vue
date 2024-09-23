<script setup>
import CarouselCard from "@/components/CarouselCard.vue"

const alternatives = [
    {
        colour: "#306E36",
        score: 7.5,
        name : "Good Company",
        accountNo : "23495945"
    },
    {
        colour: "#306E36",
        score: 8,
        name : "Great Company",
        accountNo : "23495945"
    }    
]


</script>

<template>
    <div id="carouselExampleIndicators" class="carousel slide py-3">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <CarouselCard :info="alternatives[0]"></CarouselCard>
            </div>
            <div class="carousel-item">
                <h1>HELLO 2</h1>
            </div>
            <div class="carousel-item">
                <h1>HELLO 3</h1>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

