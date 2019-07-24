<template>
<v-card class="rounded-card">
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
        md14
      >

        <material-card 
        >
          <v-btn
            color="green darken-3"
            dark
            class="mb-2" >Excel</v-btn>
            <v-layout column style="height: 100vh">       
            <v-flex  style="overflow: auto">   
          <v-data-table
            :headers="headers"
            :items="items"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text-general text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
             <td>{{ item.reg_no }}</td>
              <td>{{ item.title }}</td>
              <td>{{ item.problem_statement }}</td>
               <td>{{ item.abstract }}</td>
                <td>{{ item.proposal_uploadfile }}</td>
                 <td>{{ item.status }}</td>
            </template>
          </v-data-table>
          </v-flex>
          </v-layout>
        </material-card>
      </v-flex>

     
    </v-layout>
  </v-container>
  </v-card>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    headers: [
      {
        sortable: true,
        text: 'Reg No',
        value: 'reg_no'
      },
      {
        sortable: true,
        text: 'Title',
        value: 'title'
      },
      {
        sortable: false,
        text: 'Problem Statment',
        value: 'problem_statment'
      },
      {
        sortable: false,
        text: 'Abstract',
        value: 'abstract',
      },
      {
        sortable: false,
        text: 'File',
        value: 'file',
      },
      {
        sortable: false,
        text: 'Status',
        value: 'status',
      },

        ],
        items: []

        }),
        mounted() {
          
            axios.get("http://127.0.0.1:5000/approved").then(response => {
                this.items = response.data
            })

             
            

          
            },
}
</script>
<style >
   .rounded-card{
    border-radius:50px;
}
  
</style>
