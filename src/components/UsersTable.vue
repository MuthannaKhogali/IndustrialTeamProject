<script setup>
const result = await fetch("https://qmbank.uk/api/leaderboard")

const leaderboard = await result.json();



</script>

<template>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Level</th>
        <th scope="col">Experience</th>
        <th scope="col">🔥</th>
      </tr>
    </thead>
    <tbody v-for="(info, index) in leaderboard">
      <tr>
        <th scope="row">{{index + 1 }}</th>
        <td>{{ info.name }}</td>
        <td>{{ info.level }}</td>
        <td>{{ info.experience }}</td>
        <td>{{ info.streak }}</td>
      </tr>
    </tbody>
  </table>
</template>
