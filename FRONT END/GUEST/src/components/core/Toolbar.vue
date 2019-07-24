<template>
	 <v-card class="rounded-card" mobile-break-point="50" >
	<v-toolbar   id="core-toolbar" class="teal" style="background: #424242;" flat prominent >
		<div class="v-toolbar-title">
			<v-toolbar-title class="font-weight-light text-general">
				
				
			</v-toolbar-title>
		</div>

		<v-spacer/>
		<v-toolbar-items  class="hidden-sm-and-down"> 
			
			
		<v-list-tile
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          :active-class="color"
        
          
        >
          <v-list-tile-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-action-text 
		  class="white--text"
            v-text="link.text"
          />
        </v-list-tile>
		
		</v-toolbar-items>

		<v-menu class="hidden-md-and-up">
        <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
        <v-list  >
          <v-list-tile v-for="(link, i) in links" :key="i" :to="link.to" >
            <v-list-tile-content >
              <v-list-tile-title >{{ link.text }}</v-list-tile-title>
             </v-list-tile-content>
          </v-list-tile>   
        </v-list>
      </v-menu>
			

			<v-flex align-center layout py-2>
				<v-text-field
					v-if="responsiveInput"
					class="mr-4 mt-2 purple-input"
					label="Search..."
					hide-details
					color="purple"
				/>
				
				<v-menu bottom left content-class offset-y transition="slide-y-transition">
					<router-link
						v-ripple
						slot="activator"
						class="toolbar-items"
						to="/dashboard/notifications"
					>
						
					</router-link>
					<v-card>
						<v-list dense>
							<v-list-tile v-for="notification in notifications" :key="notification" @click="onClick">
								<v-list-tile-title v-text="notification"/>
							</v-list-tile>
						</v-list>
					</v-card>
				</v-menu>
				
				<v-icon class="toolbar-items" color @click="logout">mdi-power</v-icon>
				
			</v-flex>
		
	</v-toolbar>
	</v-card>
</template>

<script>
	import { mapMutations, mapGetters } from "vuex";

	export default {
		data: () => ({
			 logo: require('@/assets/img/redditicon.png'),
    links: [
      {
        to: '/dashboard',
      
        text: 'Dashboard'
	  },
	   {
        to: '/dashboard/messages',
    
        text: 'Approved  projects'
      },
      {
        to: '/dashboard/user-profile',
   
        text: 'Assigned Proposals'
      },
     
      {
        to: '/dashboard/user-tables',
    
        text: 'Upload projects'
      },
      {
        to: '/dashboard/typography',
        
        text: 'Progress comments'
      },
      {
        to: '/dashboard/rejected',
     
        text: 'Progress Report'
      },
      
	],
	
    responsive: false,
			notifications: [
				"Mike, Thanos is coming",
				"5 new avengers joined the team",
				"You're now friends with Capt",
				"Another Notification",
				"Another One - Dj Khalid voice"
			],
			title: "final year roject platform",
			responsive: false,
			responsiveInput: false,
			


		}),

		computed: {
			...mapGetters(["authorized"])
		},

		watch: {
			$route(val) {
				this.title = val.meta.name;
			}
		},

		mounted() {
			this.onResponsiveInverted();
			window.addEventListener("resize", this.onResponsiveInverted);
		},
		beforeDestroy() {
			window.removeEventListener("resize", this.onResponsiveInverted);
		},

		methods: {
			...mapMutations("app", ["setDrawer", "toggleDrawer"]),
			onClickBtn() {
				this.setDrawer(!this.$store.state.app.drawer);
			},
			onClick() {
				//
			},
			onResponsiveInverted() {
				if (window.innerWidth < 991) {
					this.responsive = true;
					this.responsiveInput = false;
				} else {
					this.responsive = false;
					this.responsiveInput = true;
				}
			},
			logout: function() {
				this.$store.dispatch("logout").then(() => {
					this.$router.push("/");
				});
			},

		}
	};
</script>

<style>
	 .rounded-card{
    border-radius:50px;
}

	#core-toolbar a {
		text-decoration: none;
	}
</style>
