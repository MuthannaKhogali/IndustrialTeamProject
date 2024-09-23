<script setup>
import UserInfo from "@/components/UserInfo.vue"
import AlternativeCarousel from "@/components/AlternativeCarousel.vue"

const userInfo = {name : "Douglas Inglis", accountNo : "234232116415", userLevel : 17, balance : "17345.23"}
</script>




<template>
<div class = "mainpage">
    <UserInfo :userInfo = "userInfo"></UserInfo>

    <div class = "card my-4 company rounded-0">
        <div class = "card-title ps-2">
            <h1>Evil Corp LTD</h1>
            <h6>AC: 2174901072</h6>
            <h6>Fuel</h6>
        </div>
        <div class = "card-body">
            <h3>Environmental Score : </h3>
            <div class="container"> 
                <div class="skill html" id = "info-main">2.5</div>
            </div> 
            <AlternativeCarousel></AlternativeCarousel>
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
  background-color: #FFFFFF;
  margin-bottom: 5px;
  text-align:left;
  border-style:solid;
  border-radius: 20px;
}

.main{
    background-color: #FFFFFF;
}

/*This is taken from https://www.geeksforgeeks.org/how-to-create-a-progress-bar-using-html-and-css/ */
.container { 
    background-color: rgb(192, 192, 192); 
    width: 100%; 
    border-radius: 15px; 
    padding : 0%
} 
  
.skill { 
    color: white;
    padding: 1%; 
    text-align: right; 
    font-size: 20px; 
    border-radius: 15px; 
} 

#info-main {
    background-color: v-bind("info.colour"); 
    width: v-bind("info.score"); 
}
</style>