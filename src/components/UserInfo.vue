<script setup>
import { useRouter, useRoute } from "vue-router";
import { useStore } from "@/store";

const store = useStore();
const router = useRouter();
const route = useRoute();

const showHome = route.name === "home";
const showBack = route.name === "score" || route.name === "payeedetails" || route.name === "transaction" || route.name === "moreinfo";

function logout() {
  router.push({ path: "/login" });
}

function score() {
  router.push({ path: "/score" });
}

function back() {
  router.go(-1);
}
</script>

<template>
  <div class="userandmoney row">
    <!--user name, account id and level -->
    <div class="userinfo col-6">
      <!-- hardcoded some details for now-->
      <div class="ps-2">
        <h1 class="username">{{ store.accountInfo.name || "Name Unknown" }}</h1>
        <h6 class="accountID">
          AC: {{ store.accountInfo.account_id || "Not Found" }}
        </h6>
        <h3 v-if="store.accountInfo.level !== undefined" class="userlevel">
          Level {{ store.accountInfo.level }}
        </h3>
        <div @click="score" class="btn btn-primary" v-if="showHome">
          About Level
        </div>
        <div @click="back" class="btn btn-primary mb-3" v-if="showBack">Back</div>
      </div>
    </div>
    <!--user money with button which will take the user to transfer screen -->
    <div class="moneystuff col-6 d-flex flex-column">
      <div class="logo ms-auto">
        <img src="../assets/logo.png" width="60" height="60" />
      </div>
      <h1 class="me-2">
        £{{
          store.accountInfo.balance !== undefined
            ? store.accountInfo.balance
            : "Unknown"
        }}
      </h1>
      <div class="logout">
        <div @click="logout" class="btn btn-danger" v-if="showHome">
          Log Out
        </div>
      </div>
    </div>
    <div class="container">
      <div v-if="store.accountInfo.level !== undefined" class="skill" id="user-scores"></div>
    </div>
  </div>
</template>

<style scoped>
/*this is the top section which has username, id, level, money and transfer button*/
.userandmoney {
  background-color: #ffffff;
  border-style: solid;
  border-width: 0px;
  border-color: darkgray;
}

/*style for the app logo*/
.logo {
  width: 50px;
  height: 50px;
  float: right;
  margin: 10px;
}

/*this is for the user details which are name id and level*/
.userinfo {
  font-size: 25px;
  text-align: left;
}

/*style for the name of the user*/
.username {
  margin: 10px 0px 0px 0px;
}

/*style for the account id number*/
.accountID {
  margin: 2px 0px 0px 0px;
  color: rgb(123, 122, 122);
}

/*style for the user level*/
.userlevel {
  margin: 0px 0px 10px 0px;
  font-size: 20px;
}

/*style for the money and the tranfer button section*/
.moneystuff {
  margin-bottom: 20px;
  text-align: right;
}

.logout {
  padding-right: 5px;
  text-align: right;
}

/*This is taken from https://www.geeksforgeeks.org/how-to-create-a-progress-bar-using-html-and-css/ */
.container {
  background-color: rgb(192, 192, 192);
  width: 100%;
  border-radius: 15px;
  padding: 0%;
}

.skill {
  color: white;
  padding: 1%;
  text-align: right;
  font-size: 20px;
  border-radius: 15px;
}

#user-scores {
  background-color: #306e36;
  width: 80%;
}

/*Tranfer button styles*/
.payeeBtn {
  background-color: #0f0a0a;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 30px;
}
</style>
