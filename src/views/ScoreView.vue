<script setup>
import UserInfo from "@/components/UserInfo.vue";
import UsersTable from "@/components/UsersTable.vue";
import { useStore } from "@/store";

const store = useStore();
console.log(store.accountInfo.level)


</script>

<template>
  <div class="mainpage">
    <UserInfo :userInfo="{
      name: 'User',
      account_id: '2834502',
      balance: 2342324,
    }" />
    <div class ="container-fluid">
    <div class="row">
      <div class="card py-3 mt-4 company rounded-0">
        <div class="card-title ps-2">
          <h1>Your Level:</h1>
        </div>
        <div class="mx-2">
          <div class="container">
            <div class="skill" id="info-main">80/100 EXP</div>
          </div>
          <div class="px-2">
            <div class="row py-2">
              <div class="col-4 text-start">
                <h6>Level {{ store.accountInfo.level }}</h6>
              </div>
              <div class="col-4 text-center">
                <h6></h6>
              </div>
              <div class="col-4 text-end">
                <h6>Level {{ store.accountInfo.level + 1 }}</h6>
              </div>
            </div>
          </div>
          <div class="row">
            <div>
              <h1>Streak:<span style = "color : #ffb02e">🔥{{ store.accountInfo.streak }}</span></h1>
              <p>Streaks are built by making multiple eco-friendly transactions in a row</p>
            </div>
          </div>
          <div class="row">
          </div>
          <div class="row px-3">
            <Suspense>
              <UsersTable />
            </Suspense>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
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

@keyframes progressAnimation {
  from {
    width: 40%;
  }

  to {
    width: 80%;
  }
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

#info-main {
  background-color: green;
  width: 80%;
  animation: progressAnimation 3s;
}
</style>
;
