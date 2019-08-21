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
               <div>{{proposal.title}}
                 
               </div>
            </template>
                <v-card-text class="px-16">
                  <div class="text-centre">
                      <v-dialog
                        v-model="dialog"
                        width="500"
                      >
                        <template v-slot:activator="{ on }">
                          <v-btn
                            color="teal"
                            dark
                            v-on="on"
                            style="float:right"
                          >
                            To Review
                          </v-btn>
                        </template>

                        <v-card>

                          <v-card-text>
                           <v-autocomplete
                            :items="components"
                            filled
                            chips
                            color="blue-grey lighten-2"
                            label="Supervisor"
                            item-text="email"
                            item-value="email"
                            v-model="email"
                    >
                        <template v-slot:selection="data">
                          <v-chip
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            
                          >
                           
                            {{ data.item.email }}
                          </v-chip>
                        </template>
                        <template v-slot:item="data">
                          <template v-if="typeof data.item !== 'object'">
                            <v-list-item-content v-text="data.item"></v-list-item-content>
                          </template>
                          <template v-else>
                           
                            <v-list-item-content>
                              <v-list-item-title v-html="data.item.email"></v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </template>
                      </v-autocomplete>
                           
                          <v-text-field multi-line="true" label="Comment" placeholder="comment" v-model="review_comment"></v-text-field>
                           
                          </v-card-text>

                          <v-divider></v-divider>

                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                              color="primary"
                              text
                              
                              @click="review(index)"
                            >
                              Submit
                            </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                    </div>
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
                    <h4 class="font-weight-bold">Status</h4>
                    <div>{{proposal.status}}</div>
                    <p></p>
                    <h4 class="font-weight-bold">Reviewer Comment</h4>
                    <div>{{proposal.review_comment}}</div>
                    <p></p>
                    
                    <!-- <v-spacer></v-spacer> -->

                    <v-autocomplete
                            :items="components"
                            filled
                            chips
                            color="blue-grey lighten-2"
                            label=" Main Supervisor"
                            item-text="name"
                            item-value="name"
                            v-model="supervisor"
                    >
                        <template v-slot:selection="data">
                          <v-chip
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            
                          >
                           
                            {{ data.item.name }}
                          </v-chip>
                        </template>
                        <template v-slot:item="data">
                          <template v-if="typeof data.item !== 'object'">
                            <v-list-item-content v-text="data.item"></v-list-item-content>
                          </template>
                          <template v-else>
                           
                            <v-list-item-content>
                              <v-list-item-title v-html="data.item.name"></v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </template>
                      </v-autocomplete>


                      <v-autocomplete
                            :items="components"
                            filled
                            chips
                            color="blue-grey lighten-2"
                            label=" Co Supervisor"
                            item-text="name"
                            item-value="name"
                            v-model="cosupervisor"
                    >
                        <template v-slot:selection="data">
                          <v-chip
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            
                          >
                           
                            {{ data.item.name }}
                          </v-chip>
                        </template>
                        <template v-slot:item="data">
                          <template v-if="typeof data.item !== 'object'">
                            <v-list-item-content v-text="data.item"></v-list-item-content>
                          </template>
                          <template v-else>
                           
                            <v-list-item-content>
                              <v-list-item-title v-html="data.item.name"></v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </template>
                      </v-autocomplete>
    
                      <v-text-field label="Field Supervisor" placeholder="Field Supervisor (optional)" v-model="extsupervisor"></v-text-field>
                       <v-autocomplete
                            :items="components"
                            filled
                            chips
                            color="blue-grey lighten-2"
                            label=" Email"
                            item-text="email"
                            item-value="email"
                            v-model="email2"
                    >
                        <template v-slot:selection="data">
                          <v-chip
                            v-bind="data.attrs"
                            :input-value="data.selected"
                            
                          >
                           
                            {{ data.item.email }}
                          </v-chip>
                        </template>
                        <template v-slot:item="data">
                          <template v-if="typeof data.item !== 'object'">
                            <v-list-item-content v-text="data.item"></v-list-item-content>
                          </template>
                          <template v-else>
                           
                            <v-list-item-content>
                              <v-list-item-title v-html="data.item.email"></v-list-item-title>
                            </v-list-item-content>
                          </template>
                        </template>
                      </v-autocomplete>

                  
                    <v-text-field multi-line="true" label="Comment" placeholder="Comment" v-model="comment"></v-text-field>
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
                cosupervisor:"",
                extsupervisor:"",
                email: "",
                comment: "",
                name:"",
                email2:"",
                
                review_comment:"",
                pending: null,
                link: null,
                dialog: false,
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
          remove (item) {
        const index = this.components.indexOf(item.name)
        if (index >= 0) this.components.splice(index, 1)
      },
          propsal(){
               axios.get("http://127.0.0.1:5000/pendingproposal").then(response => {
                this.proposals = response.data })
          },
          review(index){
            axios.post("http://127.0.0.1:5000/review", {
                    "reg_no": this.proposals[index].reg_no, "review_email": this.email,
                    "comment": this.review_comment
                }).then(this.dialog=false)

          },
            approve(index) {
                axios.post("http://127.0.0.1:5000/approve", {
                    "reg_no": this.proposals[index].reg_no, "supervisor": this.supervisor, "email": this.email2,
                    "comment": this.comment, "status": "Approved","cosupervisor":this.cosupervisor,
                    "extsupervisor":this.extsupervisor,
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
       
          
        }
     
    
   
}
</script>
