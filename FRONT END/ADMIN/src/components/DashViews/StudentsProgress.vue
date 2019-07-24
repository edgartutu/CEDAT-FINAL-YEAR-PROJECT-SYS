<template>

    <v-container  fill-height
    fluid
    grid-list-xl>
      <v-layout justify-center
      wrap>
      <v-flex  md8 >

         <material-card>
        
        
            
          <v-text-field
            v-model="search"
            append-icon="search"
            label="Search"
            single-line
            hide-details>
            </v-text-field><br>
             <v-spacer></v-spacer>
            <v-card v-for="(item,index) in items" :key="item.datestamp">
                 <v-card-slide class="px-12">
                     <h4 class="font-weight-bold">Student</h4>
                    <div>
                        {{item.reg_no}}
                    </div>
                    <h4 class="font-weight-bold">Progress Report</h4>
                    <div>
                        {{item.files}}
                    </div>
                    <div>
                        <v-btn class="green" @click="pendingfiles(index)">Download</v-btn>
                    </div>
                     <h4 class="font-weight-bold">Submit date</h4>
                      <div>
                        {{item.datestamp}}
                    </div>
                    <v-divider class="my-3"></v-divider>
                </v-card-slide>
            </v-card>
           
         </material-card>
      </v-flex>
      </v-layout>
    </v-container>
 
</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
                items: [],
                reg_no: "",
            }
        },
        mounted() {
            axios.get("http://127.0.0.1:5000/allprogressreports").then(response => {
                this.items = response.data })
        },
        methods: {
            pendingfiles(index) {
                axios.post("http://127.0.0.1:5000/progressfiles", {
                    "reg_no": this.items[index].reg_no
                }).then(response => {
                    console.log(response.data)
                })

            }
        }
}
</script>