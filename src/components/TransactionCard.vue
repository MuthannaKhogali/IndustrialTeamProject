<script setup>
import { ref } from 'vue'

// type objects gets all the things in store.transactions https://json-schema.org/understanding-json-schema/reference/object 
const props = defineProps({
  info: {
    type: Object,
    required: true,
  }
});

//this was referenced https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
//reference for hour and minute if needed https://www.codu.co/articles/how-to-show-hours-and-minutes-only-with-tolocaletimestring-7dskbbzo 
function makeDate(d) {
  const options = { year: 'numeric', month: 'long', day: 'numeric'};
  return new Date(d).toLocaleDateString(undefined, options);
}

const colour = ref('grey');

console.log(props.info.score)

if (props.info.score <= 0.3 ) {
      colour.value = "red"
  } else if (props.info.score > 0.3 && props.info.score < 0.7){
    colour.value = "orange"
  } else if (props.info.score >= 0.7){
    colour.value = "green"
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
      <RouterLink to="/moreinfo" class="card-link">More Information</RouterLink>
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

</style>