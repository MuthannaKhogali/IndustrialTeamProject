<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"

const accountNo = ref(undefined);
const router = useRouter();

function submit(){
    if (accountNo.value == 3) {
        router.push({path : "/"})
    }
}

function register(){
    router.push({path : "/register"})
}
</script>


<template>
    <div class="d-flex flex-column min-vh-100 min-vw-100">
        <div class="d-flex flex-grow-1 justify-content-center align-items-center">
            <div style = "color : #F3F9E3; font-family: 'Noto Sans', sans-serif;">
                <img src="../assets/logo.png" width="100" height="150" class="pb-5">
                    <h1 class = "text-light">Login</h1>
                    <input type="text" class = "rounded" v-model = "accountNo" placeholder="Account Number"/><br>
                    <input v-model="accountNo" placeholder="Account" class="rounded mb-3"><br>
                    <div @click="submit" class="btn btn-light mt-4">Go</div><br>
                    <div @click="register" class="btn btn-light mt-4">Register Account</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
:global(body) {
  background-color: #f8f8f8;
}
</style>