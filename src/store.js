import { defineStore } from "pinia";
import { ref } from "vue";

export const useStore = defineStore("store", () => {
  const accountNo = ref(null);
  const accountInfo = ref(null);
  const payeeInfo = ref(null);
  const paymentInfo = ref(null);
  const transactions = ref(null);

  return {
    accountNo,
    accountInfo,
    payeeInfo,
    paymentInfo,
    transactions
  };
});
