<template>
  <v-content>
    <v-app
      id="dashboard-view"
      >
      <core-filter />

      <core-toolbar />

      <core-drawer />

      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>

      <core-footer v-if="$route.name !== 'Maps'" />

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
  }
}
</script>

<style>

</style>
