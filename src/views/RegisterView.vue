<script setup>
import { ref } from "vue";

const formData = ref({ name: String, money: String });

function register() {
  console.log(formData);
}
</script>

<template>
  <div class = "login-body">
    <div class="d-flex flex-column min-vh-100 min-vw-100">
      <div class="d-flex flex-grow-1 justify-content-center align-items-center">
        <div>
          <img src="../assets/logo.png" width="200" height="210" class="pb-3" />
          <h1>Register</h1>
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="name"
            placeholder="Name"
          /><br />
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="money"
            placeholder="Money, e.g. £500"
          /><br />
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
;
