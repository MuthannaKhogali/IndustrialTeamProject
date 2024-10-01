<script setup>

// type objects gets all the things in store.transactions
const props = defineProps({
  info: {
    type: Object,
    required: true,
  }
});

</script>

<template>
  <div class="company card rounded-0">
    <div class="card-body">
      <div class="card-title">
        <h1>{{ props.info.recipient_name || "Name Undefined" }}</h1>
      </div>
      <h2>£{{ props.info.amount / 100 || 0 }}</h2>
      <h6>Exp: {{ props.info.score || 0 }}</h6>
      <h6>{{ props.info.date || "Date Unknown" }}</h6>
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
  border-color: v-bind("info.colour");
  border-radius: 20px;
}
</style>