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
      <v-flex  md12>
        <material-card  
        >
        <v-card-text>
              <v-flex
               md12
              >
              <v-spacer></v-spacer>
              <div class="text-xs-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          color="purple"
          dark
          v-on="on"
        >
         New Projects
        </v-btn>
      </template>
      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
         Add Project
        </v-card-title>

        <v-card-text action="/dashboard/user-tables">
         
              <v-layout wrap>
            <v-text-field
              label="Title" v-model="title"/>
                    </v-layout>
                    <p></p>
                     <v-layout wrap>
                        <v-text-field multi-line="true"
                          label="Coment"  v-model="comments"/>

                    </v-layout>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="save"
            
          >
            Submit
          </v-btn>
           <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
             @click="dialog = false"
          >
            Exit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
            <v-container>
  <v-layout column style="height: 40vh">       
    <v-flex md14 style="overflow: auto">
              <v-data-table
              :headers="headers"
              :items="items"
              hide-actions>
              <template
                slot="headerCell"
                slot-scope="{ header }"
              >
                <span
                  class="subheading font-weight-light text-success text--darken-3"
                  v-text="header.text"
                />
              </template>
              <template
                slot="items"
                slot-scope="{ item }"
              >
                <td>{{ item.ref_no }}</td>
                  <td>{{ item.title }}</td>
                  <td>{{ item.comments}}</td>
                  <td>{{ item.date_submit}}</td>
      
              </template>
            </v-data-table>
            </v-flex>
            </v-layout>
            </v-container>
        
        </v-flex>
      
      </v-card-text>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
    export default {
        data () {
          return {
        dialog: false,
        ref_no:'',
        title: '',
        comments: '',

              
            headers: [
                {
                    sortable: false,
                    text: 'Reference Number',
                    value: 'name'
                },
                {
                    sortable: false,
                    text: 'Title',
                    value: 'name'
                },
                {
                    sortable: false,
                    text: 'Comment',
                    value: 'country'
                  },
                {
                    sortable: false,
                    text: 'Date Submitted',
                    value: 'name'
                }
            ],
            items: [],
             
                   
      
    }

          },
        mounted() {
             axios.get("http://127.0.0.1:5000/adminviewprojects").then(response => {
                this.items = response.data
            })
        },
        methods:{

        
           save(){
             axios.post("http://127.0.0.1:5000/postproject", {
              "title": this.title, "comments": this.comments
          }).then(window.location.reload())

           },
           

        }
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
