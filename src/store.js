import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useStore = defineStore('store', () => {
  const accountNo = ref(null)

  return {
    accountNo,
  }
})
