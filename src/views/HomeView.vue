<script setup>
import UserInfo from "@/components/UserInfo.vue";
import TransactionCard from "@/components/TransactionCard.vue";
import { ref } from "vue";
import { useRoute } from "vue-router";

const info = ref({});
const userInfo = ref({});

(async () => {
  const accountNo = useRoute().params.accountNo;
  let result = await fetch("https://qmbank.uk/api/accounts/" + accountNo);
  info.value = await result.json();

  userInfo.value = {
    name: info.value.name,
    account_id: info.value.account_id,
    balance: info.value.balance,
    level: info.value.company_rag_score,
  };
})();

//info.is_company ? userInfo["level"] = info["company_rag_score"] : userInfo["level"] = info["level"];

//console.log(userInfo.value);

const transactionArray = [
  {
    name: "Evil Corp LTD",
    amount: 50,
    experience: 5,
    date: "Paid on Dec 26",
    colour: "#DB2B39",
  },
  {
    name: "Mid Corp LTD",
    amount: 100,
    experience: 10,
    date: "Paid on Dec 26",
    colour: "#F3A712",
  },
  {
    name: "Good Corp LTD",
    amount: 200,
    experience: 20,
    date: "Paid on Dec 26",
    colour: "#306E36",
  },
];
</script>

<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
  <!--whole page-->
  <div class="mainpage">
    <!--top section which shows user data stuff -->
    <UserInfo :userInfo="userInfo"></UserInfo>

    <!-- this is the transaction history section which will display recent payments -->
    <!-- hardcoded some companies for now-->

    <div class="row">
      <div
        class="transactionhistory"
        v-bind:key="info"
        v-for="info in transactionArray"
      >
        <TransactionCard :info="info"></TransactionCard>
      </div>
    </div>
  </div>

  <!-- floating button is taken from https://codepen.io/androidcss/pen/yOopGp -->
  <a href="http://localhost:8080/#/payeedetails" class="float">
    <i class="fa fa-plus my-float"></i>
  </a>
</template>

<style scoped>
/*mainpage is the whole page */
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

/*this is the remaining 60% section which has the history of transactions*/
.transactionhistory {
  background-color: white;
  margin: 10px 0px 10px 0px;
}

.float {
  position: fixed;
  width: 60px;
  height: 60px;
  bottom: 40px;
  right: 40px;
  background-color: #306e36;
  color: #fff;
  border-radius: 50px;
  text-align: center;
  box-shadow: 2px 2px 3px #999;
}

.my-float {
  margin-top: 22px;
}
</style>
