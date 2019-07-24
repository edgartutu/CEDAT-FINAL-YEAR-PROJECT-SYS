<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    >
      <v-flex  xs12
        md12 >
         
        
          <v-form >  
          
            <v-expansion-panel popout>
              <v-expansion-panel-content v-for="(proposal,index) in proposals" :key="proposal.supervisor">
                <template v-slot:header>
               <div>{{proposal.title}}</div>
            </template>
                  <v-card-text class="px-16">
                     <h4 class="font-weight-bold">Students</h4>
                    <div >{{proposal.reg_no}}</div>
                     <h4 class="font-weight-bold">Title</h4>
                    <div>{{proposal.title}}</div>
                    <h4 class="font-weight-bold">Problem statment</h4>
                    <div>{{proposal.problem_statement}}</div>
                     <h4 class="font-weight-bold">Methodology</h4>
                    <div>{{proposal.methodology}}</div>
                      <h4 class="font-weight-bold">File</h4>
                    <div>{{proposal.proposal_uploadfile}}</div>
                    <p>
                        <v-btn class="green" @click="pendingfiles(index)">Download</v-btn>
                    </p>
                    <h4 class="font-weight-bold">status</h4>
                    <div>{{proposal.status}}</div>
                    <h4 class="font-weight-bold">Supervisors</h4>
                     <div>{{proposal.supervisor}}</div>
                     <h4 class="font-weight-bold">Comment</h4>
                     <div>{{proposal.commet}}</div>
                   
                  </v-card-text>
          
              </v-expansion-panel-content>
            </v-expansion-panel>
      
    
          </v-form>
        
      </v-flex>
      <v-flex
        xs12
        md4
      >
        
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
    data () {
      return {
        proposals: [],
        email:''
      }  
    },

    mounted(){
      this.email=localStorage.getItem('user')
      axios.post('http://127.0.0.1:5000/viewproposals',{'email':this.email}).then(response => {
                this.proposals = response.data
                
            })
    },
     
        methods: {
            pendingfiles(index) {
                axios.post("http://127.0.0.1:5000/pendingfiles2", {
                    "reg_no": this.proposals[index].reg_no
                  }).then(response => {
                 this.forceFileDownload(response)
                })

            },
            forceFileDownload(response){
            const url = window.URL.createObjectURL(new Blob([response.data]))
             const link = document.createElement('a')
             link.href = url
             link.setAttribute('download', 'file.pdf','file.docx') //or any other extension
             document.body.appendChild(link)
            link.click()
    },
        }
     
    
   
}
</script>
