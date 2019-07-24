<template>
  <v-container>
  <v-layout column style="height: 30vh">       
    <v-flex md16 style="overflow: auto">
  <v-data-table class="fb-table-elem"
      :headers="headers"
      :items="items"
      hide-actions
      item-key="name"
      expand >
      <template slot="items" slot-scope="props" >          
        <tr @click="props.expanded = !props.expanded">
          <td class="datatable-cell-wrapper"><div>{{ props.item.reg_no }}</div></td>
          <td class="datatable-cell-wrapper"><div>{{ props.item.title }}</div></td>
          <td class="datatable-cell-wrapper"><div>{{ props.item.status}}</div></td>
          <td class="datatable-cell-wrapper"><div>{{ props.item.proposal_uploadfile }}</div></td>
          <td class="datatable-cell-wrapper">{{ props.item.student_pair }}</td>
          <td class="datatable-cell-wrapper">{{ props.item.supervisor }}</td>
          <td class="datatable-cell-wrapper">{{ props.item.email }}</td>
          <v-dialog
          v-model="dialog"
           width="600"
          >
            <template v-slot:activator="{ on }">
              <v-btn
                small 
                class="pink"
                v-on="on"
              >
              review
              </v-btn>
                </template>
                   <v-card>
                      <v-card-title
                      class="headline grey lighten-2"
                     primary-title
                      >
                      Concept Details
                    </v-card-title>
                            <v-card-text class="px-16">
                                <h4 class="font-weight-bold">Students</h4>
                                 <p>{{props.item.student1}}</p>
                                <p>{{props.item.reg_no}}</p>
                                 <p>{{props.item.student2}}</p>
                                 <p>{{props.item.reg_no2}}</p>
                                <h4 class="font-weight-bold">Title</h4>
                                <p>{{props.item.title}}</p>
                                <h4 class="font-weight-bold">Problem statment</h4>
                                <p>{{props.item.problem_statement}}</p>
                                <h4 class="font-weight-bold">Methodology</h4>
                                <p>{{props.item.methodology}}</p>
                                <h4 class="font-weight-bold">File</h4>
                                <p>{{props.item.file}}</p>
                                  <h4 class="font-weight-bold">Status</h4>
                                <p>{{props.item.status}}</p>
                                
                            </v-card-text>     
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                          <v-dialog
                          v-model="dialog"
                          width="200"
                          >
                            <!-- <template v-slot:activator="{ on }">
                              <v-btn
                              class="green"       
                                v-on="on"
                                @click="approve"
                              >
                                Approve
                              </v-btn>
                            </template> -->
                            <v-card>
                              <v-card-text>
                                <h4 style="color:green">Successfull</h4> 
                              </v-card-text>
                              <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-spacer></v-spacer>
                              </v-card-actions>
                            </v-card>
                          </v-dialog>
                          <v-spacer></v-spacer>
                          <v-dialog
                          v-model="dialog"
                          width="200"
                          >
                           <!-- <template v-slot:activator="{ on }">
                              <v-btn
                              class="red"       
                                v-on="on"
                                @click="rejected"
                              >
                               Reject
                              </v-btn>
                            </template> -->
                            <v-card>
                              <v-card-text>
                                <h4 style="color:red"> Rejected!</h4>
                                </v-card-text>
                                 <v-card-actions>
                                   <v-spacer></v-spacer>
                                   </v-card-actions>
                                   </v-card>
                                   </v-dialog>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
            
          </tr>
          
        </template>
        <template slot="expand" >
          <v-card flat>
            <v-card flat="flat" color="grey lighten-4">
              <v-container fluid="fluid" grid-list-xl="grid-list-xl">
                <v-layout row="row" wrap="wrap">
                  <v-flex >
                      <user/>
                    
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card>
          </v-card>
        </template>
      </v-data-table>
      </v-flex>
      </v-layout>
      </v-container>
</template>
<script>
import axios from 'axios'
import user from './UserProfile.vue'

  export default {
      components:{
          user

      },
    
    
    data(){
      return {

                proposals: {},
                supervisor: "",
                email: "",
                comment: "",
               

                

    
        
      headers: [
       
         { text: 'Reg_no', value: 'reg_no' },
        { text: 'Title', value: 'title' },
        { text: 'Student', value: 'student_pair' }, 
        { text: 'Supervisor', value: 'supervisor' }, 
        { text: 'file', value: 'proposal_uploadfile' },
       { text: 'Status', value: 'status' },
    
      
      ],
      items: [

       
      ]
      
    }
    
    },
  
  mounted() {
      this.prop();
            this.propsal();
           
            // this.intervalFetchData()
          
            
        },
  
      

  
       methods: {
         prop(){
            axios.get("http://127.0.0.1:5000/proposals").then(response => {
                this.items = response.data
            })

         },
          propsal(){
               axios.get("http://127.0.0.1:5000/pendingproposal").then(response => {
                this.proposals = response.data })
          },
            
        //     intervalFetchData: function () {
        //     setInterval(() => { 
        //         this.prop();
        //         this.propsal();
                
        //         }, 3000);    
        // },
         }
     
  }
</script>
Expandable Table