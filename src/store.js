import { defineStore } from "pinia";
import { ref } from "vue";

export const useStore = defineStore("store", () => {
  const accountNo = ref(null);
  const accountInfo = ref(null);

  return {
    accountNo,
    accountInfo,
  };
});
