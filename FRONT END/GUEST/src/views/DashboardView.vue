<template>
  <v-content>
    <v-app
      id="dashboard-view"
      class="green lighten-4"
      >
      <v-container >
       <v-card class="rounded-card" >
      <core-filter />

      <core-toolbar />

     

      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>

      <core-footer v-if="$route.name !== 'Maps'" />
        
      </v-card>
      </v-container>

    </v-app>
  </v-content>
</template>

<script>
export default {
  name: 'DashboardView',
  
  metaInfo () {
    return {
      title: 'FYP'
    }
  },
  
}
</script>

<style>
 .rounded-card{
    border-radius:50px;
}

</style>
