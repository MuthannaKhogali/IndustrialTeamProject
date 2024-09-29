<script setup>
import CarouselCard from "@/components/CarouselCard.vue"

const props = defineProps({
    transaction: Boolean
})

const alternatives = [
    {
        colour: "#F3A712",
        score: 5,
        name: "OK Company",
        accountNo: "23495945",
        active: false
    },
    {
        colour: "#306E36",
        score: 8,
        name: "Great Company",
        accountNo: "23495945",
        active: true
    }
]


</script>

<template>
    <div id="carouselExampleIndicators" class="carousel carousel-dark slide pb-3">
        <div class="carousel-inner">
            <div class="carousel-item" v-for="info in alternatives" v-bind:key="info.name"
                v-bind:class="(info.active ? 'active' : '')">
                <CarouselCard :info="info" :transaction="props.transaction"></CarouselCard>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
            data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>
