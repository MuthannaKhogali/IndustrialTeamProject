<script setup>
import { ref } from 'vue'
import { useStore } from '@/store'
import { useRouter } from "vue-router"
// type objects gets all the things in store.transactions https://json-schema.org/understanding-json-schema/reference/object 
const props = defineProps({
  info: {
    type: Object,
    required: true,
  }
});

const store = useStore();
const router = useRouter();

//this was referenced https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
//reference for hour and minute if needed https://www.codu.co/articles/how-to-show-hours-and-minutes-only-with-tolocaletimestring-7dskbbzo 
function makeDate(d) {
  const options = { year: 'numeric', month: 'long', day: 'numeric'};
  return new Date(d).toLocaleDateString(undefined, options);
}

async function callInfo(){
  const result = await fetch("https://qmbank.uk/api/accounts/" + (props.info.is_outgoing ? props.info.recipient_id : props.info.sender_id))
  if (result.status === 200) {
    store.payeeInfo = await result.json();
    store.paymentInfo = props.info
    router.push({name : "transaction"})
  }
}

const colour = ref('#444444');

console.log(props.info.score)

if (props.info.score <= 0.3 ) {
      colour.value = "#8B0000"
  } else if (props.info.score > 0.3 && props.info.score < 0.7){
    colour.value = "#BA8E23"
  } else if (props.info.score >= 0.7){
    colour.value = "#2E6F40"
 }



</script>

<template>
  <div class="company card rounded-0">
    <div class="card-body">
      <div class="card-title">
        <h1>{{ props.info.is_outgoing ? props.info.recipient_name : props.info.sender_name || "Name Undefined" }}</h1>
      </div>
      <h2 :class="props.info.is_outgoing ? 'minus' : 'plus'">{{ props.info.is_outgoing ? '-' : '+' }}£{{ (props.info.amount / 100).toFixed(2) || 0 }}</h2>
      <h6>Exp: {{ props.info.experience || 0 }}</h6>
      <h6>{{ makeDate(props.info.date) || "Date Unknown" }}</h6>
      <h6>Reference: {{ props.info.reference || "No Reference" }}</h6>
      <span @click = "callInfo" >More Information</span>
    </div>
  </div>
</template>

<style scoped>
/*style for the company div, which displays transaction history companies*/
.company {
  font-size: 15px;
  background-color: #FFFFFF;
  margin-bottom: 5px;
  text-align: left;
  border-style: solid;
  border-width: 0px 0px 0px 35px;
  border-color: v-bind(colour);
  border-radius: 20px;
}

.minus {
  color: rgb(155, 0, 0);
}

.plus {
  color: rgb(0, 115, 0);
}

/* Link styling taken fromhttps://stackoverflow.com/questions/14070086/how-do-i-style-a-span-to-look-like-a-link-without-using-javascript */
span {
    color: #000000; /* Change this with links color*/
    cursor: pointer;
    text-decoration: underline;
}

span:hover {
    color: #444444; /* Change the value to with anchors hover color*/
}

</style>