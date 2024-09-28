<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const formData = ref({ name: "", starting_balance: "" });

const router = useRouter();

async function register() {
  //console.log(formData.value.name)

  let response = await fetch("https://qmbank.uk/api/accounts", {
    method: "POST",
    body: {
      name: "Lowrie",
      starting_balance: 323,
    },
    headers: {
      "Content-Type": "application/json;",
    },
  });

  if (response.status != 200) {
    return;
  } else {
    console.log(await response.json());
  }

  login();
}

function login() {
  router.push({ path: "/login" });
}
</script>

<template>
  <div class="login-body">
    <div class="d-flex flex-column min-vh-100 min-vw-100">
      <div class="d-flex flex-grow-1 justify-content-center align-items-center">
        <div>
          <img src="../assets/logo.png" width="200" height="210" class="pb-3" />
          <h1>Register</h1>
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="formData.name"
            placeholder="Name"
          /><br />
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="formData.starting_balance"
            placeholder="Money, e.g. £500"
          /><br />
          <div
            @click="register"
            class="btn mt-4 border border-3 border-dark shadow-sm"
            style="background-color: #306e36"
          >
            Register Account
          </div><br />
          <div
            @click="login"
            class="btn mt-4 border border-3 border-dark shadow-sm"
            style="background-color: #306e36"
          >
            Have an account?
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
;
