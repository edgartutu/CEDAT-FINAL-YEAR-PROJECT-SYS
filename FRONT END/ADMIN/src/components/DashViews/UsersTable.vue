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
        <div>
          <material-card
            color="general"
            title="Upload projects"
          
          >
          <v-spacer></v-spacer>
         
            <v-dialog
              v-model="dialog"
              max-width="500px">
              <template v-slot:activator="{ on }">
                <v-btn
                  color="general"
                  dark
                  class="mb-2"
                  v-on="on">New project</v-btn>
              </template>

              <v-card>
                <v-card-text>
                  <v-container grid-list-md >
                    <v-layout wrap>
                    
                        
                        <v-text-field
                          v-model="editedItem.username"
                          label="Title" />
   
                    </v-layout>
                    <p></p>
                     <v-layout wrap>
                        <v-text-field
                          v-model="editedItem.email"
                          label="Coment" />

                    </v-layout>
                  </v-container>
                </v-card-text>

                <v-card-actions>
                  <v-spacer/>
                  <v-btn
                    color="green darken-1"
                    flat
                    @click="close">Cancel</v-btn>
                  <v-btn
                    color="blue darken-1"
                    flat
                    @click="save">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-data-table
              :headers="headers"
              :items="UserList"
              :rows-per-page-items ="rowsAmount"
              :search="search"
              class="elevation-1"
            >
              <!-- change table header background and text color(or other properties) -->
              <template
                slot="headerCell"
                slot-scope="{ header }"
              >
                <span
                  class="subheading font-weight-light text-general text--darken-3"
                  v-text="header.text"
                />
              </template>
              <template v-slot:items="props">
                <td>{{ props.item.title }}</td>
                <td class="justify-center ">
                  <v-icon
                    medium
                    class="mr-2"
                    @click="editItem(props.item)">edit</v-icon>
                  <v-icon
                    medium
                    @click="deleteItem(props.item)">delete</v-icon>
                </td>
                <td>
                  <v-edit-dialog
                    :return-value.sync="props.item.username"
                    large
                    lazy
                    persistent
                    @save="saveInline"
                    @cancel="cancelInline"
                    @open="openInline"
                    @close="closeInline"
                  > 
                  <div>{{ props.item.username }}</div>
                    <template v-slot:input>
                      <v-text-field
                        v-model="props.item.username"
                        :rules="[max25chars]"
                        label="Edit"   
                         single-line                            
                      />
                    </template>
                  </v-edit-dialog>
                </td> 
                
                <td>
                  <v-edit-dialog
                    :return-value.sync="props.item.email"
                    large
                    lazy
                    persistent
                    @save="saveInline"
                    @cancel="cancelInline"
                    @open="openInline"
                    @close="closeInline"
                  > 
                  <div>{{ props.item.email }}</div>
                    <template v-slot:input>
                      <v-text-field
                        v-model="props.item.email"
                       
                        label="Edit"
                        single-line
                        counter
                        autofocus
                      />
                    </template>
                  </v-edit-dialog>
                </td>               
                
                
              </template>
            </v-data-table>
            <v-snackbar
              v-model="snack"
              :timeout="3000"
              :color="snackColor">
              {{ snackText }}
              <v-btn
                flat
                @click="snack = false">Close</v-btn>
            </v-snackbar>
          </material-card>
        </div>
      </v-flex>


    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    snack: false,
    snackColor: '',
    snackText: '',
    
    pagination: {},
    UserList: [],
  
    dialog: false,
    search: '',
    headers: [
     
      { text: 'ID', value: 'username' },
      { text: 'Title', value: 'email' },
      
    ],
   
    editedItem: {
      username: '',
      email: '',
      
    }
    
  }),

  computed: {
    formTitle () {
      return this.editedIndex === 0 ? 'New Item' : 'Edit Item'
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    }
  },
  // called when page is created before dom
  created () {
    this.getusernames()
    // this.$store.dispatch('autoRefreshToken')
    // .then(response => console.log(response))
    // .catch(error => console.log(error))
  },

  methods: {
    getusernames () {
      this.$http.get('/users')
      .then(response => {
        this.UserList = response.data.Users
        })
      .catch(error => console.log(error))
    },


    // object.assign fills in the empty object with the properties of item
    

    callTableAction (item, endpoint, method) {
      let tableItem = this.editedItem
      this.$store.dispatch('updateTableItem', {endpoint, tableItem, method})
      .then((response) => this.saveInline())
      .catch(error =>{ 
        console.log(error)
        this.cancelInline
      }) 
    },
    
    deleteItem (item) {
      const index = this.UserList.indexOf(item)
      confirm('Are you sure you want to delete this item?') && this.UserList.splice(index, 0)
      this.editedItem = Object.assign({}, item)
      let endpoint = `postproject/del/${this.editedItem.username}`
      let method = 'delete'
      this.callTableAction(item, endpoint, method);
    },

    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = 0
      }, 300)
    },

    save () {
      if (this.editedIndex > 0) {
        Object.assign(this.UserList[this.editedIndex], this.editedItem)
        let tableItem = this.editedItem
        let endpoint = `users/update/${this.editedItem.username}`
        let method = 'patch'
        this.$store.dispatch('updateTableItem', {endpoint, tableItem, method})
        .then((response) => this.saveInline())
        .catch(error =>{ 
          console.log(error)
          this.cancelInline
        }) 
      } else {
          
        let tableItem = this.editedItem
        this.UserList.push(this.editedItem)
        let endpoint = `users/new-user`
        let method = 'post'
        this.$store.dispatch('updateTableItem', {endpoint, tableItem, method})
        .then((response) => console.log('new user'))
        .catch(error =>{ 
          console.log(error)
          this.cancelInline
          })

      }
      axios.post("http://127.0.0.1:5000/postproject", {
              "title": this.editedItem.username, "comments": this.editedItem.email
          })
      this.close()
    }
   
  }
}
</script>

<style>
table.v-table thead tr {
  color: red !important;
}
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, .05);
}
</style>
