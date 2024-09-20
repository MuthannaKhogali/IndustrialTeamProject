<template>

  <!--whole page-->
  <div class="mainpage">

    <!--top section which shows user data stuff -->
    <div class="userandmoney">
      <!--user name, account id and level -->
      <div class="userinfo">

        <!-- app logo (used the logo which comes from vue.js for now)-->
        <div class="logo">
          <img src="../assets/logo.png" width="50" height="50">
        </div>

        <!-- hardcoded some details for now-->
        <h1 class="username">Name Surname</h1>
        <h2 class="accountID">AC: 12079310237</h2>
        <h3 class="userlevel">Level 17</h3>
      </div>

      <!--user money with button which will take the user to transfer screen -->
      <div class="moneystuff">
        <h1>Balance: £1,000,000</h1>
        <router-link to="/transaction">
          <button>Transfer</button>
        </router-link>
      </div>
    </div>


    <!-- this is the transaction history section which will display recent payments -->
     <!-- hardcoded some companies for now-->

    <div class = "col">
      <div class="transactionhistory">
      <div class="company card rounded-0">
        <div class = "card-body">
          <div class = "card-title">
            <h1>The Evil Company</h1>
          </div>
          <h2>amount: £10</h2>
          <h3>Exp: 5</h3>
          <h4>Paid on Dec 26</h4>
        </div>
      </div>
      <div class="company card rounded-0">
        <div class = "card-body">
          <div class = "card-title">
            <h1>The Evil Company</h1>
          </div>
          <h2>amount: £10</h2>
          <h3>Exp: 5</h3>
          <h4>Paid on Dec 26</h4>
        </div>
      </div>

      <div class="company card rounded-0">
        <div class = "card-body">
          <div class = "card-title">
            <h1>The Evil Company</h1>
          </div>
          <h2>amount: £10</h2>
          <h3>Exp: 5</h3>
          <h4>Paid on Dec 26</h4>
        </div>
      </div>

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

:global(body) {
  background-color: #E8E9EB;
}

/*mainpage is the whole page */
.mainpage {
  font-family: "Roboto Slab", serif;
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
}

/*this is the top section which has username, id, level, money and transfer button*/
.userandmoney {
  background-color: #FFFFFF;
  border-style:solid;
  border-width:1px;
  border-color:darkgray;
}

/*style for the app logo*/
.logo{
  width:50px;
  height:50px;
  float:right;
  margin:10px;
}

/*this is for the user details which are name id and level*/
.userinfo{
  font-size:25px;
  text-align:left;
  border-style:solid;
  border-width:1px;
  border-color:darkgray;
}

/*style for the name of the user*/
.username{
  margin:0px 0px 0px 0px;
}

/*style for the account id number*/
.accountID{
  margin:10px 0px 0px 0px;
  font-size:25px;
}

/*style for the user level*/
.userlevel{
  margin:10px 0px 10px 0px;
  color:blue;
  font-size:20px;
}

/*style for the money and the tranfer button section*/
.moneystuff {
  margin-bottom:20px;
}

/*Tranfer button styles*/
button {
  background-color: #0F0A0A;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 30px;
}

/*this is the remaining 60% section which has the history of transactions*/
.transactionhistory {
  background-color: white;
  margin: 10px 0px 10px 0px;
}

/*style for the company div, which displays transaction history companies*/
.company {
  font-size: 15px;
  background-color: #FFFFFF;
  margin-bottom: 10px;
  text-align:left;
  border-style:solid;
  border-width: 2px 2px 2px 35px;
  border-color:#306E36;
  border-radius: 20px;
}

</style>
