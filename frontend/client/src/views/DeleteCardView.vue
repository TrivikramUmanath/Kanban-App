
  

<template>
    <div class="body">
      <router-link to="/Dashboard">Dashboard </router-link> 
      <br>
      </br>
      <br>
    </br>
      <div class="box">
        <center>
          <form @submit.prevent="DeleteCard">
  
            <label for="Title">Title</label>
            <p> {{ Title }}   </p>
            <br> 
            </br>
            <label for="Content">Content</label>
  
  <p> {{ Content }}  </p>
            <br>
           </br>
           <label for="Deadline">Deadline</label>
  
  <p> {{ Deadline }}  </p>
  <br>
</br>
<label for="Status">Status</label>
  
  <p> {{ Status }}  </p>
  <br></br>
  
        
                <button type="submit">Delete</button>
        
            
          </form>
        </center>
  
      </div>
  </div>
  </template>
  
  <script>
  export default {
  name: "DeleteCard",
  data() {
    return {
    Title :sessionStorage.getItem("Card_Name"),
    Content :"",
    Status: "",
    Deaadline: "",
    id : sessionStorage.getItem("id"),
    card_id : null,
    token : localStorage.getItem("token"),
    card:null,
    };
  },
  async created() {
    return fetch(`http://localhost:8000/api/${this.id}/${this.Title}/getCard`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
        })
      .then((response) => response.json())
      .then((re_data) => {

        this.card = re_data;
        this.card_id = re_data["Card_Id"];
        this.Title = re_data["Title"];
        this.Content = re_data["Content"];
        this.Status = re_data["Status"];
        this.Deadline = re_data["Deadline"];
        console.log(re_data);
      })
      .catch((error) => console.log(this.Title));
    },
    methods: {
    async DeleteCard() {
      try {
        fetch(`http://localhost:8000/api/${this.id}/${this.card_id}/DeleteCard`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          }
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            sessionStorage.removeItem("Card_Name");
            this.$router.push('/Dashboard');
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Delete ", error);
      }
    }
  },
  };
  </script>
  
  
  
  <style scoped></style>