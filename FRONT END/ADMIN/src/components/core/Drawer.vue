<template>
  <v-navigation-drawer
  
    id="app-drawer"
    v-model="inputValue"
    app
    dark
    floating
    persistent
    mobile-break-point="991"
    width="260"
    class="purple darken-4"
  >
    <v-img
      :src="image"
      height="100%"
    >
      <v-layout
        class="fill-height"
        tag="v-list"
        column
        
      >
        <v-list-tile avatar>
          <v-list-tile-avatar
            color="grey"
          >
            <v-img
              :src="logo"
              height="64"
              contain
            />
          </v-list-tile-avatar>
          <v-list-tile-title class="title">
            Projects
          </v-list-tile-title>
        </v-list-tile>
        <v-divider/>
        <v-list-tile
          
          v-if="responsive"
        >
          <v-text-field
            class="purple-input search-input"
            label="Search..."
            color="grey"
          />
        </v-list-tile>
        <v-list-tile
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          flat small
          avatar
          class="v-list-item"

        >
          <v-list-tile-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-title
          
            v-text="link.text"
            
          />
        </v-list-tile>
      </v-layout>
    </v-img>
  </v-navigation-drawer>
</template>

<script>
// Utilities
import {
  mapMutations,
  mapState
} from 'vuex'

export default {
  data: () => ({
    logo: require('@/assets/img/redditicon.png'),
    links: [
      {
        to: '/dashboard',
        icon: 'mdi-view-dashboard',
        text: 'Dashboard'
      },
      {
        to: '/dashboard/user-profile',
        icon: 'mdi-account',
        text: 'Pending Proposals'
      },
      {
        to: '/dashboard/table-list',
        icon: 'mdi-clipboard-outline',
        text: 'Approved Proposals'
      },
      {
        to: '/dashboard/user-tables',
        icon: 'mdi-table-edit',
        text: 'Upload projects'
      },
      {
        to: '/dashboard/typography',
        icon: 'mdi-format-font',
        text: 'View projects'
      },
      {
        to: '/dashboard/rejected',
        icon: 'folder',
        text: 'Rejected Proposal'
      },
       {
        to: '/dashboard/registry',
        icon: 'folder',
        text: 'Registry'
      },
      {
        to: '/dashboard/progress',
        icon: 'folder',
        text: 'Students Progress'
      },
     /* {
        to: '/dashboard/notifications',
        icon: 'mdi-bell',
        text: 'Notifications'
      },*/

       {
        to: '/dashboard/messages',
        icon: 'message',
        text: 'Messages'
      }
    ],
    responsive: false
  }),
  computed: {
    ...mapState('app', ['image', 'color']),
        inputValue: {
      get () {
        return this.$store.state.app.drawer
      },
      set (val) {
        this.setDrawer(val)
      }
    },
    items () {
      return this.$t('Layout.View.items')
    }
  },
  mounted () {
    this.onResponsiveInverted()
    window.addEventListener('resize', this.onResponsiveInverted)
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.onResponsiveInverted)
  },
  methods: {
    ...mapMutations('app', ['setDrawer', 'toggleDrawer']),
    onResponsiveInverted () {
      if (window.innerWidth < 991) {
        this.responsive = true
      } else {
        this.responsive = false
      }
    }
  }
}
</script>

<style lang="scss">
  #app-drawer {
    .v-list__tile {
      border-radius: 4px;
      height: 40px;
      margin-top: 2px;

      &--buy {
        margin-top: auto;
        margin-bottom: 17px;
      }
    }

    .v-image__image--contain {
      top: 9px;
      height: 40%;
    }

    .search-input {
      margin-bottom: 30px !important;
      padding-left: 15px;
      padding-right: 15px;
    }
  }
</style>
