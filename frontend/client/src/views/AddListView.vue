

<template>
    <div class="body">
      <router-link to="/Dashboard">Dashboard </router-link> 
      <div class="box">
          <form @submit.prevent="AddList">
  
            <label for="name">Name</label>
            <br>
            </br>
  
            <input type="message" name="name" v-model="name" required>
  
            <br>
            </br>
      
  
            <!-- <label for="Description">Description</label>
            <input type="" name="password" v-model="password" required> -->
  
            <label for="description">Description</label>
            <br>
        </br>
        <!-- <p style="white-space: pre-line;">{{ message }}</p> -->
        <input type="message" name="description" v-model="description" required>
        <!-- <textarea v-model="description" placeholder="Description" name="description">
        </textarea> -->
            <br>
            </br>
            <br>
           </br>
  
            <center>
                <button type="submit">Save</button>
            </center>
            
          </form>
  
  
      </div>
  </div>
  </template>
  
  <script>
  export default {
  name: "AddList",
  data() {
    return {
    //   email: "",
    //   password: "",
    name :"",
    description :"",
    id : sessionStorage.getItem("id"),
    token : localStorage.getItem("token")
    };
  },

  methods: {
    async AddList() {
      try {
        fetch(`http://localhost:8000/api/${this.id}/AddList`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
          body: JSON.stringify({ Name: this.name, Description: this.description }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
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