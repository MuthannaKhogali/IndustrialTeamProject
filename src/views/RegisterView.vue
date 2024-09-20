<script setup>
import {ref} from "vue";

const formData = ref({accountNo : undefined, firstname : undefined, secondname : undefined,  money : undefined})

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
                    <input type="text" v-model = "formData.accountNo" placeholder="Account Number"></input><br>
                    <input type="text" v-model = "formData.firstname" placeholder="First Name"></input><br>
                    <input type="text" v-model = "formData.secondname" placeholder="Second Name"></input><br>
                    <input type="text" v-model = "formData.money" placeholder="e.g. £500"></input><br>
                    <div @click="register" class="btn btn-light mt-4">Register Account</div>
            </div>
        </div>
    </div>
</template>