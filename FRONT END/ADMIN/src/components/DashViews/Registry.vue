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
          color="green"
          title="Registered Students"
        
        >  <v-data-table
            :headers="headers"
            :items="items.slice(0, 7)"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
             <td>{{ item.reg_no }}</td>
              <td>{{ item.student1 }}</td>
              <td>{{ item.email }}</td>
               <td>{{ item.reg_no2 }}</td>
                <td>{{ item.student2 }}</td>
                 <td>{{ item.email2 }}</td>
              
            </template>
          </v-data-table>
         
        </material-card>
      </v-flex>
      <v-flex
        md12
      >
        <material-card
          color="green"
          flat
          full-width
          title="Registered Lecturers"
         
        >
          <v-data-table
            :headers="header"
            :items="itemz.slice(0, 7)"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.email }}</td>
              <td>{{ item.contact }}</td>
              
            </template>
          </v-data-table>
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
        sortable: false,
        text: 'Reg_no',
        value: 'reg_no'
      },
      {
        sortable: false,
        text: 'Student1',
        value: 'student1'
      },
      {
        sortable: false,
        text: 'Contact',
        value: 'contact1'
      },
      {
        sortable: false,
        text: 'Reg_no1',
        value: 'reg_no1',
        
      },
      {
        sortable: false,
        text: 'Student2',
        value: 'student2',
       
      },
      {
        sortable: false,
        text: 'Contact2',
        value: 'contact2',
       
      },
      
    ],
        items: [],

     itemz: [],

    header: [
      {
        sortable: false,
        text: 'Name',
        value: 'name'
      },
      {
        sortable: false,
        text: 'Email',
        value: 'email'
      },
      {
        sortable: false,
        text: 'Contact',
        value: 'contact'
      }
      
    ],
        }),
        mounted() {
            axios.get("http://127.0.0.1:5000/allstudents").then(response => {
                this.items = response.data })

            axios.get("http://127.0.0.1:5000/allguest").then(response => {
                this.itemz = response.data })
        }
}
</script>
