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
                     <h4 class="font-weight-bold mx-3">Student</h4>
                    <div class="mx-3">
                        {{item.reg_no}}
                    </div>
                    <h4 class="font-weight-bold mx-3 " >Progress Report</h4>
                    <div class="mx-3">
                        {{item.files}}
                    </div>
                    <div class="mx-3">
                        <v-btn class="green" @click="pendingfiles(index)">Download</v-btn>
                    </div>
                     <h4 class="font-weight-bold mx-3">Submit date</h4>
                      <div class="mx-3">
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
             forceFileDownload(response){
            const url = window.URL.createObjectURL(new Blob([response.data]))
             const link = document.createElement('a')
             link.href = url
             link.setAttribute('download', 'file.pdf') //or any other extension
             document.body.appendChild(link)
            link.click()
    },
            pendingfiles(index) {
                axios.post("http://127.0.0.1:5000/progressfiles", {
                    "reg_no": this.items[index].reg_no
                }).then(response => {
        this.forceFileDownload(response)
                })

            }
        }
}
</script>