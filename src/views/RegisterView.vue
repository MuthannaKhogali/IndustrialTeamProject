<script setup>
import {ref} from "vue";

const formData = ref({accountNo : String, name : String, money : String})

function register(){
    console.log(formData)
}
</script>

<template>
    <div class="d-flex flex-column min-vh-100 min-vw-100">
        <div class="d-flex flex-grow-1 justify-content-center align-items-center">
            <div style = "color : #F3F9E3">
                    <img src="https://placehold.jp/60x60.png" alt="Placeholder" class="pb-5">
                    <h1 class = "text-light">Register</h1>
                    <input v-model="name" placeholder="Name" class="rounded mb-3"><br>
                    <input v-model="accountNo" placeholder="Account Number" class="rounded mb-3"><br>
                    <input v-model="money" placeholder="Money, eg £500" class="rounded mb-3"><br>
                    <div @click="register" class="btn btn-light mt-4">Register Account</div>
            </div>
        </div>
    </div>
</template>