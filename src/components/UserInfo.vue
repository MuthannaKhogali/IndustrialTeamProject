<script setup>
import {defineProps} from "vue";

const props = defineProps({
    userInfo : {
        name : String,
        accountNo : String,
        userLevel : Number,
        balance : String
    }
})
</script>

<template>
    <div class="userandmoney row">
        <!--user name, account id and level -->
        <div class="userinfo col-6">
            <!-- hardcoded some details for now-->
             <div class = "ps-2">
                <h1 class="username">{{ props.userInfo.name || "Name Unknown" }}</h1>
                <h6 class="accountID">AC:  {{ props.userInfo.accountNo || "Not Found" }}</h6>
                <h3 class="userlevel">Level {{ props.userInfo.userLevel || "Unknown" }}</h3>
             </div>
        </div>
        <!--user money with button which will take the user to transfer screen -->
        <div class="moneystuff col-6">
            <div class="logo">
            <img src="../assets/logo.png" width="60" height="60">
            </div>
            <h1 class = "me-2">£{{ props.userInfo.balance || "Unknown" }}</h1>
            <!-- app logo (used the logo which comes from vue.js for now)-->
        </div>
    </div>
</template>

<style scoped>
 /*this is the top section which has username, id, level, money and transfer button*/
.userandmoney {
  background-color: #FFFFFF;
  border-style:solid;
  border-width:0px;
  border-color:darkgray;
}

/*style for the app logo*/
.logo{
  width:50px;
  height:50px;
  float:right;
  margin:10px;
}

/*this is for the user details which are name id and level*/
.userinfo{
  font-size:25px;
  text-align:left;

}

/*style for the name of the user*/
.username{
  margin:10px 0px 0px 0px;
}

/*style for the account id number*/
.accountID{
  margin:2px 0px 0px 0px;
  color: rgb(123, 122, 122);
}

/*style for the user level*/
.userlevel{
  margin:0px 0px 10px 0px;
  font-size:20px;
}

/*style for the money and the tranfer button section*/
.moneystuff {
  margin-bottom:20px;
  text-align: right;
}

/*Tranfer button styles*/
button {
  background-color: #0F0A0A;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 30px;
}
</style>