<script setup>
import UserInfo from "@/components/UserInfo.vue";
import TransactionCard from "@/components/TransactionCard.vue";
import { useStore } from "@/store";

const store = useStore();

//Runs a the page loads getting all the users transactions in an array
(async () => {
  let transactions = await fetch(
    "https://qmbank.uk/api/accounts/" + store.accountNo + "/transactions"
  );
  if (transactions.status === 200) {
    store.transactions = await transactions.json();
  } else {
    store.transactions = null;
  }
})();
</script>

<template>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
  <!--whole page-->
  <div class="mainpage">
    <!--top section which shows user data stuff -->
    <div class="mb-2">
      <UserInfo />
    </div>
    <!-- this is the transaction history section which will display recent payments -->
    <div class="container-fluid">
      <div class="row">
        <!--Loops through all transactions pulled from the API feeds the data into transaction cards-->
        <div
          class="transactionhistory"
          v-bind:key="info"
          v-for="info in store.transactions"
        >
          <TransactionCard :info="info"></TransactionCard>
        </div>
      </div>
    </div>
  </div>

  <!-- floating button is taken from https://codepen.io/androidcss/pen/yOopGp -->
  <RouterLink to="/payeedetails" class="float">
    <i class="fa fa-plus my-float"></i>
  </RouterLink>
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
  padding-left: 0;
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
