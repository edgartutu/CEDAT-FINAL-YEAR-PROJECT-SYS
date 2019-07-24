<template>
	<div class="guestprogressreport">
		<navbar2/>
		<v-container >
			<v-card class="ma-3" v-for="proposal in proposals" :key="proposal.reg_no">
				<v-card-text class="px-12 my-6">
					<div class="font-weight-bold">{{proposal.reg_no}}</div>
					<div class="font-weight-bold">{{proposal.file}}</div>
				</v-card-text>
			</v-card>
		</v-container>
	</div>
	
</template>
<script>
import axios from 'axios';
export default {

	data(){
		return {
			proposals: [],
			email:''
		}
	},
	mounted(){
		 this.email=localStorage.getItem('user')
		axios.post('http://127.0.0.1:5000/reports',{'email':this.email}).then(response => {
                this.proposals = response.data
            })
	}
}
	
</script>