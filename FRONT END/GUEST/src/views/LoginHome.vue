<!-- This is the file that will render any external pages you do not want inside the dash, like login form-->
<template>
  <v-app
    id="login-home"
    class="green lighten-4">
    <v-container
    fill-height
    fluid
    grid-list-xl
    >
    <h2   class="teal--text">FINAL YEAR PROJECT SYSTEM</h2>
     
      <v-spacer></v-spacer>
    <transition mode="out-in">
      
      
      <router-view/>
     
    </transition>

     </v-container>

  </v-app>
</template>

<script>
export default {
}
</script>

<style>
</style>
