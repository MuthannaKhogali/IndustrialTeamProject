<script setup>
import UserInfo from '@/components/UserInfo.vue';
import router from '@/router';
import { ref } from "vue";
import { useStore } from "@/store";

const store = useStore();


// this is the data taken from the forms entered by the user
const PayeeData = ref({  recipient_id: "", amount: "", reference: "" })

// this is the message which will be displayed if the request fails
const message = ref("");

// this is a function which takes the user to the transaction page if request is successful
function goToTransactionPage() 
{
  router.push({ path: "/transaction" });
}

// this function is used when the check payee button is pressed. it sends the data stored in PayeeData to the api to
// see if the payee can be found. if its successful, the user is taken to the transaction page
async function CheckPayee() 
{
  console.log(PayeeData) // console msg just to check if form works

  // this checks if the user entered the account number, the amount and the reference
  if ( !PayeeData.value.recipient_id || !PayeeData.value.amount || !PayeeData.value.reference)
  {
    message.value = "Please enter all pieces of information!"; // shows message if the required fields have not been filled in by user
    return;
  }

  PayeeData.value.amount = PayeeData.value.amount * 100
  // if the required data has been entered by the user, proceeds with the post request
  let response = await fetch(`https://qmbank.uk/api/accounts/${PayeeData.value.recipient_id}`)

  if (response.status == 200) // if the request is successful...
  {  
    const data = await response.json();
    
    if(data) // if found...
    {
      store.payeeInfo = data;
      store.paymentInfo = PayeeData;
    }

    goToTransactionPage(); // take the user to the transaction page
  } 
  
  else 
  {
    message.value = "Payee Not Found!"; // displays error message if the payee is not found
  }
}

</script>

<template>
  <!-- whole page -->
  <div class="mainpage">

    <!-- top section which shows user data stuff -->
    <UserInfo/>

    <div class="inputsection">

      <!--https://getbootstrap.com/docs/4.0/components/input-group/-->

      <div class="input-group mb-3">
        <span class="input-group-text"></span>
        <input type="text" v-model="PayeeData.recipient_id" class="form-control" placeholder="Account Number" required>
      </div>

      <div class="input-group mb-3">
        <span class="input-group-text"></span>
        <input type="number" v-model="PayeeData.amount" class="form-control" placeholder="Amount" required>
      </div>

      <div class="input-group">
        <span class="input-group-text"></span>
        <input type="text" v-model="PayeeData.reference" class="form-control" placeholder="Reference">
        <!--<input type="text" v-model = "PayeeData.reference" class="form-control" aria-label="Reference">-->
      </div>

      <!--https://getbootstrap.com/docs/4.0/components/buttons/-->
      <div class="payeeBtn">
        <div style="margin-top:20px;" class="button-container">
            <button type="button" @click="CheckPayee" class="btn btn-dark">Check Payee</button>
        </div>
      </div>

      <div>{{ message }}</div> <!-- message which is displayed if the user is not found -->

    </div>
  </div>
</template>

<style scoped>
:global(body) {
  width: 100%;
  background-color: #E8E9EB;
}


.inputsection {
  margin-top: 50px;
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
