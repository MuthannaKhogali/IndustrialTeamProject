<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const accountNo = ref(undefined);
const router = useRouter();

async function submit() {
  let result = await fetch("https://qmbank.uk/api/accounts/" + accountNo.value);

  if (result.status == 200) {
    result = await result.json();

    router.push({ name: "home", params: { accountNo: result.account_id } });
  } else {
    console.log("Login Failed");
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
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="accountNo"
            placeholder="Account Number"
          /><br />
          <div
            @click="submit"
            class="btn mt-4 border border-3 border-dark shadow-sm"
            style="background-color: #306e36"
          >
            Go
          </div>
          <br />
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
  color : black;
}
</style>
