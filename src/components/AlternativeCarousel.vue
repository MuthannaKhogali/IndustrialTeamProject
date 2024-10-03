<script setup>
import CarouselCard from "@/components/CarouselCard.vue";
import { useStore } from "@/store";

const props = defineProps({
    transaction: Boolean
})

const store = useStore();

</script>

<template>
    <div id="carouselExampleIndicators" class="carousel carousel-dark slide pb-3">
        <div class="carousel-inner">
            <div class="carousel-item" v-for="(info, index) in store.payeeInfo.alternatives" v-bind:key="info"
                v-bind:class="(index === 0 ? 'active' : '')">
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
