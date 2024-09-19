<template>

  <!--whole page-->
  <div class="mainpage">

    <!--top section which shows user data stuff -->
    <div class="userandmoney">
      <!--user name, account id and level -->
      <div class="userinfo">
        <h1>Name Surname</h1>
        <h3>AC: 12079310237</h3>
        <p>Level 17</p>
      </div>

      <!--user money with button which will take the user to transfer screen -->
      <div class="moneystuff">
        <h1>Available Balance: £1,000,000</h1>
        <router-link to="/transaction">
          <button>Transfer</button>
        </router-link>
      </div>
    </div>


    <!-- this is the transaction history section which will display recent payments -->
     <!-- hardcoded some companies for now-->
    <div class="transactionhistory">
      <div class="company">
        <h1>The Evil Company</h1>
        <h2>amount: £10</h2>
        <h3>Exp: 5</h3>
        <h4>Paid on Dec 26</h4>
      </div>

      <div class="company">
        <h1>The Not As Evil Company</h1>
        <h2>amount: £60</h2>
        <h3>Exp: 20</h3>
        <h4>Paid on Dec 26</h4>
      </div>

      <div class="company">
        <h1>The Good Company</h1>
        <h2>amount: £150</h2>
        <h3>Exp: 50</h3>
        <h4>Paid on Dec 25</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
}
</script>

<style scoped>

.mainpage {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
}

.userandmoney {
  flex: 0 0 40%; 
  background-color: gray;
}

.userinfo{
 text-align:left; 
}

.moneystuff {
  text-align:center;
}

.transactionhistory {
  flex: 1;
  background-color: #f0f0f0;
  overflow-y: auto;
  padding: 10px;
}

button {
  margin-top: 20px;
}

.company {
  font-size: 15px;
  background-color: darkgray;
  margin-bottom: 10px;
  padding: 10px;
  text-align:left;
}
</style>
