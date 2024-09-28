<script setup>
import UserInfo from '@/components/UserInfo.vue';
import {ref} from "vue";


const userInfo = { name: "Douglas Inglis", accountNo: "234232116415", userLevel: 10, balance: "17345.23" };

const PayeeData = ref({payeename : "", accountnumber : "", amount : "", reference : ""})

function CheckPayee(){
    console.log(PayeeData)
}
</script>

<template>
  <!-- whole page -->
  <div class="mainpage">

    <!-- top section which shows user data stuff -->
    <UserInfo :userInfo="userInfo"></UserInfo>

    <div class="inputsection">

        <!--                      FORM VERSION
        <form>
            <label for="payeename">Payee Name:</label><br>
            <input type="text" v-model = "PayeeData.payeename" id="payeename" name="payeename"><br>

            <label for="accountnumber">Account Number:</label><br>
            <input type="text" v-model = "PayeeData.accountnumber" id="accountnumber" name="accountnumber"><br>

            <label for="amount">Amount:</label><br>
            <input type="text" v-model = "PayeeData.amount" id="amount" name="amount"><br>

            <label for="reference">Reference:</label><br>
            <input type="text" v-model = "PayeeData.reference" id="reference" name="reference"><br>

            <div class="button-container">
            <button type="button" @click="CheckPayee" class="btn btn-dark">Check Payee</button>
            </div>
        </form>
        -->

        
        <!--https://getbootstrap.com/docs/4.0/components/input-group/-->
        <div class="input-group mb-3">
        <span class="input-group-text"></span>
        <input type="text" v-model = "PayeeData.payeename" class="form-control" placeholder="Payee Name">
        </div>

        <div class="input-group mb-3">
        <span class="input-group-text"></span>
        <input type="text" v-model = "PayeeData.accountnumber" class="form-control" placeholder="Account Number">
        </div>

        <div class="input-group mb-3">
        <span class="input-group-text"></span>
        <input type="number" v-model = "PayeeData.amount" class="form-control" placeholder="Amount">
        </div>

        <div class="input-group">
        <span class="input-group-text"></span>
        <input type="text" v-model = "PayeeData.reference" class="form-control" placeholder="Reference">
        <!--<input type="text" v-model = "PayeeData.reference" class="form-control" aria-label="Reference">-->
        </div>

        <!--https://getbootstrap.com/docs/4.0/components/buttons/-->
        <div class="payeeBtn">
        <div style= "margin-top:20px;" class="button-container">
          <router-link to="/transaction">
        <button type="button" @click="CheckPayee" class="btn btn-dark">Check Payee</button>
          </router-link>
        </div>
      </div>


    </div>
  </div>
</template>

<style scoped>
:global(body) {
  width: 100%;
  background-color: #E8E9EB;
}


.inputsection{
    margin-top:50px;
}

/* Main page styling */
.mainpage {
  font-family: "Outfit", sans-serif;
  font-optical-sizing: auto;
  font-weight: 200;
  font-style: normal;
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
}

</style>
