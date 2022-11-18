
  

<template>
     
    <div class="body">
      <router-link to="/Dashboard">Dashboard        </router-link> 
      <br>
      </br>
      <br>
    </br>
      <div class="box">
        <center>
          <form @submit.prevent="EditList">
  
            <label for="name">Name</label>
            <br>
            </br>
  
            <input type="message" name="Name" v-model="Name"  required>
  
            <br> 
            </br>
      
  
            <!-- <label for="Description">Description</label>
            <input type="" name="password" v-model="password" required> -->
  
            <label for="description">Description</label>
            <br>
        </br>
        <!-- <p style="white-space: pre-line;">{{ message }}</p> -->
        <input type="message" name="description"   v-model="description" required>
        <!-- <textarea v-model="description" placeholder="Description" name="description">
        </textarea> -->
            <br>
            </br>
            <br>
           </br>
  
       
                <button type="submit">Save</button>
     
            
          </form>
        </center>
  
      </div>
  </div>
  </template>

  <script>
  export default {
  name: "Editist",
  data() {
    return {
    Name :sessionStorage.getItem("List Name"),
    description :"",
    id : sessionStorage.getItem("id"),
    list_id : null,
    token : localStorage.getItem("token"),
    list:null
    };
  },
  async created() {
    return fetch(`http://localhost:8000/api/${this.id}/${this.Name}/getList`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
        })
      .then((response) => response.json())
      .then((re_data) => {
        this.list = re_data;
        this.description = re_data["Description"]
        this.list_id = re_data["List_Id"];
        console.log(re_data);
      })
      .catch((error) => console.log(this.Name));
    },
    methods: {
    async EditList() {
      try {
        fetch(`http://localhost:8000/api/${this.id}/${this.list_id}/EditList`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
          body: JSON.stringify({ Name: this.Name, Description: this.description }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            sessionStorage.removeItem("List Name")
            this.$router.push('/Dashboard');
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
    }
},
};
</script>

  
  
  <style scoped></style>