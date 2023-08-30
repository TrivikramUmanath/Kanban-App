

<template>
    <div class="AddThread">
      <router-link to="/Dashboard">Dashboard </router-link> 
      <p> </p>
      <p> </p>
      <div class="box">
          <form @submit.prevent="AddThread">
  
            <label for="Title">Title</label>
            <br>
            </br>
  
            <input type="message" name="Title" v-model="Title" required>
  
            <br>
            </br>
      

  
            <label for="post_text">Post Message</label>
            <br>
        </br>
        <input type="message" name="post_text" v-model="post_text" required>
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
  name: "AddThread",
  data() {
    return {
      user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            thread_id:'',
            searchQuery: '',
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            email: sessionStorage.getItem("email"),
            password: sessionStorage.getItem("password"),
            AllPosts:null,
            temp:'',
            Annoynmous:false,
            thread_Name: '',
            
      message: 'Hello, Vue!'
    };
  },

  methods: {
    async AddThread() {
      console.log("Adding Thread");

 
      try {
        console.log("Inside ");
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/CreateThread`, {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ Title: this.Title }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            console.log("Response let's see");
            console.log(register_data);
            this.thread_id = register_data["thread_id"]
            try {
        console.log("Posting");
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.thread_id}/CreatePost`, {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ Post_Message: this.post_text,Annoynmous: "False"  , Poster_email: this.email, Poster_Name: this.Name }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
  
            this.$router.push("/Dashboard"); 
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
            // this.$router.push("/Dashboard"); 
            // this.$forceUpdate(); 
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