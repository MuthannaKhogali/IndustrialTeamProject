<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "@/store";

const store = useStore();

const router = useRouter();

const message = ref("");

async function submit() {
  message.value = "";
  // let result = await fetch("https://qmbank.uk/api/accounts/" + (store.accountInfo?.no ?? ""));
  let result = await fetch("https://qmbank.uk/api/accounts/" + store.accountNo);
  if (result.status == 200) {
    store.accountInfo = await result.json();
    router.push("home");
  } else {
    message.value = "The account number does not exist!";
  }
}

function register() {
  router.push({ path: "/register" });
}
</script>

<template>
  <div class="login-body">
    <div class="d-flex flex-column min-vh-100 min-vw-100">
      <div class="d-flex flex-grow-1 justify-content-center align-items-center">
        <div>
          <img src="../assets/logo.png" width="200" height="210" class="pb-3" />
          <h1>Login</h1>
          <form @submit.prevent="submit">
            <input
              type="text"
              class="rounded border-dark shadow-sm border-3"
              style="background-color: #7fb284"
              v-model="store.accountNo"
              placeholder="Account Number"
            />
            <br />
            <div>{{ message }}</div>
            <button
              type="submit"
              class="btn mt-4 border border-3 border-dark shadow-sm"
              style="background-color: #306e36"
            >
              Go
            </button>
          </form>
          <div
            @click="register"
            class="btn mt-4 border border-3 border-dark shadow-sm"
            style="background-color: #306e36"
          >
            Register Account
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-body {
  height: 100vh;
  background-color: #306e36;
  font-family: "Outfit", sans-serif;
  font-optical-sizing: auto;
  font-weight: 200;
  font-style: normal;
  color: black;
}
</style>
