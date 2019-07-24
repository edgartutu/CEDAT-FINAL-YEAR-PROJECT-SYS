<template>

  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    
    <v-layout
      justify-center
      wrap
      
    >
      <v-flex 
      md12>
        <materila-card
        
          >

         <v-card class="indigo lighten-5">
          
            <v-expansion-panel popout>
              <v-expansion-panel-content v-for="(proposal,index) in proposals" :key="proposal.reg_no">
                <template v-slot:header>
               <div>{{proposal.title}}</div>
            </template>
                <v-card-text class="px-16">
                    <h4 class="font-weight-bold">Students</h4>
                    <div>{{proposal.student1}}</div>
                    <div>{{proposal.reg_no}}</div>
                    <div>{{proposal.student2}}</div>
                    <div>{{proposal.reg_no2}}</div>
                    <h4 class="font-weight-bold">Title</h4>
                    <div>{{proposal.title}}</div>
                    <h4 class="font-weight-bold">Problem statment</h4>
                    <div>{{proposal.problem_statement}}</div>
                    <h4 class="font-weight-bold">Methodology</h4>
                    <div>{{proposal.methodology}}</div>
                    <h4 class="font-weight-bold">File</h4>
                    <div>{{proposal.proposal_uploadfile}}</div>
                    <p></p>
                    <v-btn class="green" @click="pendingfiles(index)">Download</v-btn>
                    <p></p>
                    <div>{{proposal.status}}</div>
                    <p></p>
                    <v-text-field label="Supervisor" placeholder="Supervisor" v-model="supervisor"></v-text-field>
                     <v-autocomplete
                        label="Email"
                        v-model="email"
                        v-for="item in components" :key="item.email"
                         :items="item.email"     
                      >{{item.email}}</v-autocomplete>
                    <v-text-field label="Comment" placeholder="Comment" v-model="comment"></v-text-field>
                    <v-btn class="green" @click="approve(index)">Approve</v-btn><v-spacer></v-spacer>
                    <v-btn class="red" @click="rejected(index)">Reject</v-btn>
                </v-card-text>
                <v-spacer></v-spacer>
                
          
              </v-expansion-panel-content>
            </v-expansion-panel>
      
      </v-card>
       
        </materila-card>
      </v-flex>
    </v-layout>
  </v-container>

</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
                proposals: {},
                supervisor: "",
                email: "",
                comment: "",
                pending: null,
                link: null,
                components:[
                  
                ]

            }
        },
        mounted() {
           this.propsal();
            this. approve();
            this.rejected();
            // this.intervalFetchData();
           
        },
        created(){
           axios.get("http://127.0.0.1:5000/allguest").then(response => {
                this.components = response.data })

        },
        methods: {
          propsal(){
               axios.get("http://127.0.0.1:5000/pendingproposal").then(response => {
                this.proposals = response.data })
          },
            approve(index) {
                axios.post("http://127.0.0.1:5000/approve", {
                    "reg_no": this.proposals[index].reg_no, "supervisor": this.supervisor, "email": this.email,
                    "comment": this.comment, "status": "Approved"
                }).then(window.location.reload())
            },
            rejected(index) {
                axios.post("http://127.0.0.1:5000/approve", {
                    "reg_no": this.proposals[index].reg_no,
                    "comment": this.comment, "status": "Rejected"
                }).then(window.location.reload())
            },
            forceFileDownload(response){
            const url = window.URL.createObjectURL(new Blob([response.data]))
             const link = document.createElement('a')
             link.href = url
             link.setAttribute('download', 'file.pdf') //or any other extension
             document.body.appendChild(link)
            link.click()
    },
            pendingfiles(index) {
                axios.post("http://127.0.0.1:5000/pendingfiles", {
                    "reg_no": this.proposals[index].reg_no
                }).then(response => {
        this.forceFileDownload(response)
                })

            },
        //     intervalFetchData: function () {
        //     setInterval(() => {    
        //         this.propsal();
        //         this. approve();
        //         this.rejected();

        //         }, 1000);    
        // }
          
        }
     
    
   
}
</script>
