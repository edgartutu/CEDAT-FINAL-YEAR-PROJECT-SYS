<template>
  <v-container
    fill-height
    fluid
  >
    <v-layout
      justify-center
      align-center
    >
    <v-flex
          md12>
      
        <material-card
          color="red"
          title="Projects"  
        >
            <v-container >
			<form action="/">
				<v-text-field label="Reg No" placeholder="Reg No" v-model="reg_no"></v-text-field>
				<v-text-field label="Comment" placeholder="Comment" v-model="body"></v-text-field>
				<v-btn class="green" @click="submit">Submit</v-btn>
			</form>
		</v-container> 
          </material-card>
           </v-flex>  
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return{
      
      
        proposals:{},
        reg_no: '',
        body:'',
        
    }
  },

  methods: {
    submit(){
      axios.post('http://127.0.0.1:5000/progresscomment',{reg_no:this.reg_no,body:this.body}).then(window.location.reload())
      this.$forceUpdate();
    }

  },
    
 
}

</script>

<style lang="scss">
  .tim-note {
    bottom: 10px;
    color: #c0c1c2;
    display: block;
    font-weight: 400;
    font-size: 13px;
    line-height: 13px;
    left: 0;
    margin-left: 20px;
    width: 260px;
  }
</style>
