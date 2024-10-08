import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import TransactionView from "@/views/TransactionView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import PayeeDetails from "@/views/PayeeDetails.vue";
import ScoreView from "@/views/ScoreView.vue";
import { useStore } from "@/store";

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/transaction",
    name: "transaction",
    component: TransactionView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/payeedetails",
    name: "payeedetails",
    component: PayeeDetails,
  },
  {
    path: "/score",
    name: "score",
    component: ScoreView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

function isAuthenticated() {
  const store = useStore();

  return store.accountNo === store.accountInfo?.account_id;
}

router.beforeEach(async (to) => {
  if (
    !isAuthenticated() &&
    // Avoid an infinite redirect
    to.name !== "login" &&
    to.name !== "register"
  ) {
    // redirect the user to the login page
    return { name: "login" };
  }
});

export default router;
