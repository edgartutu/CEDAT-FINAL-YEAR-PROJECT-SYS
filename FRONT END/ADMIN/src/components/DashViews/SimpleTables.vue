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
        md12
      >

        <material-card 
        >
          <export-excel :data="items">
            <div class="green--text">Export to Excel</div>
            <img src="@/assets/img/512.png" style="width:40px;height:40px">
          </export-excel>
            <v-layout column style="height: 50vh">       
            <v-flex md12 style="overflow: auto">   
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
            <template slot="items"
                      slot-scope="{ item,index }">
                <td>{{ item.id }}</td>
                <td>{{ item.reg_no }}</td>
                <td>{{ item.title }}</td>
                <td >{{ item.problem_statement }}</td>
                <td >{{ item.methodology }}</td>
                <td>{{ item.proposal_uploadfile }}</td>
                 <td>{{ item.supervisor }}</td>
                 <td>{{ item.cosupervisor }}</td>
                 <td>{{ item.extsupervisor }}</td>
                <td>{{ item.status }}</td>
                <v-btn class="flat green" @click="download(index)">Download</v-btn>
            </template>
          </v-data-table>
          </v-flex>
          </v-layout>
        </material-card>
      </v-flex>

     
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
      headers: [
      {
        sortable: true,
        text: 'Project Id',
        value: 'id'
      },
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
        text: 'Problem__________________________Statment',
        value: 'problem_statment'
      },
      {
        sortable: false,
        text: 'Proposal_________________________________Methodology ',
        value: 'methodology',
        width:"1000px",
        fixed:true,
      },
      {
        sortable: false,
        text: 'File',
        value: 'file',
      },
      {
        sortable: false,
        text: 'Main Supervisor',
        value: 'supervisor',
      },
      {
        sortable: false,
        text: 'Co Supervisor',
        value: 'cosupervisor',
      },
       {
        sortable: false,
        text: 'Field Supervisor',
        value: 'extsupervisor',
      },
      {
        sortable: false,
        text: 'Status',
        value: 'status',
      },

        ],
        items: [],
        reg_no: '',

        }),
        mounted() {
          
            axios.get("http://127.0.0.1:5000/approved").then(response => {
                this.items = response.data
            })
          
        },
        methods: {
            exportdb() {
                axios.post("http://127.0.0.1:5000/excelexport").then(response => {
                    console.log(response)
                })
            },
             forceFileDownload(response){
            const url = window.URL.createObjectURL(new Blob([response.data]))
             const link = document.createElement('a')
             link.href = url
             link.setAttribute('download', 'file.pdf') //or any other extension
             document.body.appendChild(link)
            link.click()
    },
            download(index) {
                this.reg_no = this.items[index].reg_no
                axios.post("http://127.0.0.1:5000/pendingfiles", {'reg_no':this.reg_no}).then(response => {
        this.forceFileDownload(response)
                })
            }
        }
}
</script>
