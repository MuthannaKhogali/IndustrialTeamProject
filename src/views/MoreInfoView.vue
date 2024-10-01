<script setup>
import UserInfo from "@/components/UserInfo.vue"
import AlternativeCarousel from "@/components/AlternativeCarousel.vue"

const userInfo = { name: "Douglas Inglis", accountNo: "234232116415", userLevel: 8, balance: "17345.23" }

const compInfo = { name: "Evil Corp LTD", accountNo: "32538934425", score: 2.5, colour: "#DB2B39" }

const percentage = compInfo.score * 10 + "%"
</script>




<template>
    <div class="mainpage">
        <UserInfo :userInfo="userInfo"></UserInfo>

        <div class="row">
            <div class="card my-4 company rounded-0">
                <div class="card-title ps-2">
                    <h1>{{ compInfo.name }}</h1>
                    <h6>AC: {{ compInfo.accountNo }}</h6>
                </div>
                <div class="mx-2">
                    <h3>Environmental Score : </h3>
                    <div class="container">
                        <div class="skill" id="info-main">{{ compInfo.score }}</div>
                    </div>
                    <div class="ps-2">
                        <h6>Waste Management : 23</h6>
                        <h6>Sustainability Practices : 43</h6>
                        <h6>Carbon Emission: 59</h6>
                    </div>
                    <h3 class="pt-3">Alternative Companies:</h3>
                    <div class="px-3">
                        <AlternativeCarousel :transaction="false"></AlternativeCarousel>
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
    background-color: #FFFFFF;
    margin-bottom: 5px;
    text-align: left;
    border-style: solid;
    border-radius: 20px;
}

.main {
    background-color: #FFFFFF;
}

/*This is taken from https://www.geeksforgeeks.org/how-to-create-a-progress-bar-using-html-and-css/ */
.container {
    background-color: rgb(192, 192, 192);
    width: 100%;
    border-radius: 15px;
    padding: 0%
}

.skill {
    color: white;
    padding: 1%;
    text-align: right;
    font-size: 20px;
    border-radius: 15px;
}

#info-main {
    background-color: v-bind("compInfo.colour");
    width: v-bind("percentage");
}
</style>