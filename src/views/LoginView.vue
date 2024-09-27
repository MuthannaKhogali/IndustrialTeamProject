<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router"

const accountNo = ref(undefined);
const router = useRouter();

async function submit(){
    let result = await fetch("https://qmbank.uk/api/accounts/" + accountNo.value)

    if (result.status == 200){
        result = await result.json()

        router.push({name : "home", params : {"accountNo" : result.account_id}})


    } else {
        console.log("Login Failed")
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
                    <div @click="submit" class="btn btn-light mt-4">Go</div><br>
                    <div @click="register" class="btn btn-light mt-4">Register Account</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>