<script setup>
import UserInfo from "@/components/UserInfo.vue";
import AlternativeCarousel from "@/components/AlternativeCarousel.vue";
import { useStore } from "@/store";
import { useRouter } from "vue-router";
import { ref, computed } from "vue";

const store = useStore();
const router = useRouter();

const rag_score = computed(() => {
  return store.payeeInfo.is_company
    ? Math.floor((store.payeeInfo.company_rag_score / 3) * 10) + "%"
    : null;
});

const colour = computed(() => {
  if (store.payeeInfo.is_company) {
    const score = store.payeeInfo.company_rag_score / 3 / 10;
    if (score <= 0.3) {
      return "#8B0000";
    } else if (score > 0.3 && score < 0.7) {
      return "#BA8E23";
    } else if (score >= 0.7) {
      return "#2E6F40";
    }
  }
});

console.log("running");

//this was referenced https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
//reference for hour and minute if needed https://www.codu.co/articles/how-to-show-hours-and-minutes-only-with-tolocaletimestring-7dskbbzo
function makeDate(d) {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(d).toLocaleDateString(undefined, options);
}

async function makePayment() {
  console.log(JSON.stringify(store.paymentInfo));

  const response = await fetch(
    `https://qmbank.uk/api/accounts/${store.accountNo}/transactions`,
    {
      method: "POST",
      body: JSON.stringify(store.paymentInfo),
      headers: {
        "Content-Type": "application/json;",
      },
    }
  );

  if (response.status === 200) {
    let res = await fetch(`https://qmbank.uk/api/accounts/${store.accountNo}`);
    if (res.status === 200) {
      const transactionsResponse = await fetch(`https://qmbank.uk/api/accounts/${store.accountNo}/transactions`);
      if (transactionsResponse.status === 200) {
        store.transactions = await transactionsResponse.json();
      }
      store.accountInfo = await res.json();
      store.paymentInfo = null;
      router.push({ name: "home" });
    }
  }
}
</script>

<template>
  <div class="mainpage">
    <UserInfo></UserInfo>
    <div class="container-fluid">
      <div class="row">
        <div class="card mt-3 company rounded-0">
          
          <div class="card mt-3 mx-2">
            <div class="card-title ps-2 py-2">
              <h2>{{ store.payeeInfo.name }}</h2>
              <h6>AC: {{ store.payeeInfo.account_id }}</h6>
              <div v-if="store.paymentInfo.recipient_id">
                  <h6>Reference: {{ store.paymentInfo.reference }}</h6>
                  <div v-if="store.paymentInfo.is_outgoing !== undefined">
                    <h6>Date: {{ makeDate(store.paymentInfo.date) }}</h6>
                    <h4
                      :class="store.paymentInfo.is_outgoing ? 'minus' : 'plus'"
                    >
                      Amount: {{ store.paymentInfo.is_outgoing ? "-" : "+" }}£{{
                        store.paymentInfo.amount / 100
                      }}
                    </h4>
                  </div>
                  <div v-else>
                    <h4>Amount:£{{ store.paymentInfo.amount / 100 }}</h4>
                  </div>
              </div>
            </div>
            <div v-if="store.payeeInfo.is_company" class="mx-2">
              <h3>Environmental Score :</h3>
              <div class="container">
                <div
                  class="skill"
                  :style="{ 'background-color': colour, width: rag_score }"
                >
                  {{ rag_score }}
                </div>
              </div>
              <div class="ps-2">
                <ul class="list-group list-group-flush mt-3">
                  <li class="list-group-item">
                    Waste Management :
                    {{ store.payeeInfo.company_env_scores[0] }}
                  </li>
                  <li class="list-group-item">
                    Sustainability Practices :
                    {{ store.payeeInfo.company_env_scores[1] }}
                  </li>
                  <li class="list-group-item">
                    Carbon Emission: {{ store.payeeInfo.company_env_scores[2] }}
                  </li>
                </ul>
              </div>
              <h3 class="pt-3">Alternative Companies:</h3>
              <div class="px-3">
                <AlternativeCarousel
                  :transaction="
                    store.paymentInfo.is_outgoing === undefined ? true : false
                  "
                ></AlternativeCarousel>
              </div>
            </div>
          </div>
          <div class="mb-3">
            <button
              v-if="store.paymentInfo.is_outgoing === undefined"
              @click="makePayment"
              type="button"
              class="btn btn-success"
            >
              Make Payment
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.minus {
  color: rgb(155, 0, 0);
}

.plus {
  color: rgb(0, 115, 0);
}

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

/*style for the company div, which displays transaction history companies*/
.company {
  font-size: 15px;
  background-color: #ffffff;
  margin-bottom: 5px;
  text-align: left;
  border-style: solid;
  border-radius: 20px;
}

.main {
  background-color: #ffffff;
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
</style>
