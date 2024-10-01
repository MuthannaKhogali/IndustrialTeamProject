<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const formData = ref({ name: "", starting_balance: "" });

const accountNo = ref(null)

const router = useRouter();

async function register() {
  console.log(formData.value.name);

  let response = await fetch("https://qmbank.uk/api/accounts", {
    method: "POST",
    body: JSON.stringify({
      name: formData.value.name,
      starting_balance: Math.ceil(formData.value.starting_balance * 100)
    }),
    headers: {
      "Content-Type": "application/json;",
    },
  });

  if (response.status != 200) {
    return;
  } else {
    let data = await response.json();
    
    accountNo.value = data.account_no
    console.log(data)

    console.log(accountNo.value)
  }

  //goToLoginPage();
}

function goToLoginPage() {
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
          <div class = "card border border-3 border-dark shadow-sm mb-2" v-if="accountNo" style="background-color: #7fb284">
            <div class = "card-body"><h6>Your account no is: {{ accountNo }}</h6><h6>Remember this to <RouterLink to="/login">login</RouterLink></h6></div>
          </div>
          <input
            type="text"
            class="rounded border-dark shadow-sm border-3"
            style="background-color: #7fb284"
            v-model="formData.name"
            placeholder="Name"
          /><br />
          <input
            type="number"
            class="mt-2 rounded border-dark shadow-sm border-3"
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
          </div>
          <br />
          <div
            @click="goToLoginPage"
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
