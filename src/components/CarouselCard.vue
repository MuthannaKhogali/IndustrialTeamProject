<script setup>
import { ref } from "vue";
import { useStore } from "@/store"
import { useRouter } from "vue-router"

const props = defineProps({
  info: Object,
  transaction: Boolean,
});

const rag_score = props.info.company_rag_score / 3;
// const percentage = props.info.score * 10 + "%"
const percentage = Math.floor(rag_score * 10) + "%";

const colour = ref("#00000");

const store = useStore();
const router =  useRouter();

if (rag_score / 10 <= 0.3) {
  colour.value = "#8B0000";
} else if (rag_score / 10 > 0.3 && rag_score / 10 < 0.7) {
  colour.value = "#BA8E23";
} else if (rag_score / 10 >= 0.7) {
  colour.value = "#2E6F40";
}

async function swapPayee(transaction){
    const result = await fetch("https://qmbank.uk/api/accounts/" + props.info.account_id)
    if (result.status === 200) {
        store.payeeInfo = await result.json();
        if (transaction) {
            store.paymentInfo.recipient_id = store.payeeInfo.account_id;
        } else {
            store.paymentInfo.recipient_id = null
        }
        router.push({path : "/transaction"});
    }
}

console.log(percentage);
</script>

<template>
  <div class="company card rounded-0 px-4 bg-light">
    <div class="card-body">
      <div class="card-title">
        <h1>{{ info.name }}</h1>
        <h6>AC: {{ info.account_id }}</h6>
        <div class="container">
          <div
            class="skill"
            :style="{ 'background-color': colour, width: percentage }"
          >
            {{ percentage }}
          </div>
        </div>
        <div class="mt-3 d-flex justify-content-center">
          <button
            v-if = "transaction"
            type="button"
            class="btn btn-success"
            @click="swapPayee(transaction)"
          >
            Change Payee
          </button>
          <button v-else type = "button" class = "btn btn-primary" @click = "swapPayee(transaction)">More Info</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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
