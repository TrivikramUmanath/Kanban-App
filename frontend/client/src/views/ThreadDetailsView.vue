<template>
 
 <div class="ThreadDetails"> 
    <h1 align ="right">
        <button  @click="MyAccount()">My Account</button> 
        <button  @click="Dashboard()">Dashboard</button> 
    <button v-if="Category == 'Junior'" @click="Assesments()">Assesments/</button>
    <button v-else @click="MyAssesments()">My Assesments/</button> 
      <button @click="Logout()">Logout/</button>
  
  </h1>
  
      <img alt="Vue logo" src="../assets/Placement_Logo.jpg" />
      <Login msg="Placement Portal" />
    
  <br>
  
  </br>
  <br>
  </br>
  
  <br>
  </br>
  <p> {{ thread_Name  }}             </p>
      <div id="app">
        <center>
      <table>
        <thead>
          <tr>
            <th>Post_Message</th>
            <th>TimeStamp</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="post in AllPosts" :key="post.post_id">
           
            <td>{{ post.Post_Message }}</td>
            <td>{{ post.Post_Date_Time }} </td>
            <td v-if="post.Annoynmous == 'False'">   {{ post.Poster_Name }}     </td>
            <td v-else>   Annoynmous     </td>
          </tr>
        </tbody>
      </table>
      <br>
    </br>
      <input type="text" v-model="post_text" name="post_text" placeholder="post_text" />
<br>
</br>

<p><button name="AddPost" @click=AddPost()>  Add Post </button> </p>

    
<label for="checkbox" v-if="Category != 'POD'">Annoynmous</label>
<input type="checkbox" id="Annoynmous" v-model="Annoynmous" />
  </p>
     
    </center>
    </div>
  
    </div>
  </template>
  
  
  
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script>
  export default {
  name: "ThreadDetails",
  data(){
        return {
            user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            thread_id: sessionStorage.getItem("thread_id"),
            searchQuery: '',
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            email: sessionStorage.getItem("email"),
            password: sessionStorage.getItem("password"),
            AllPosts:null,
            temp:'',
            Annoynmous:false,
            thread_Name: sessionStorage.getItem("Thread Name"),
            post_text:'',
      message: 'Hello, Vue!'
        }
    },
    async created()
    {
      return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.thread_id}/getPosts`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
          })
        .then((response) => response.json())
        .then((re_data) => {
            console.log("All Posts");
          console.log(re_data);
          this.AllPosts=re_data;
  
        })
        .catch((error) => console.log(error));
    },
    mounted(){
      console.log("Mounting");
    },
    methods:{
      async MyAccount(){
      console.log("Logging out");
      sessionStorage.removeItem("user_id")
      sessionStorage.removeItem("Name")
      this.$router.push("/MyAccount");    
    },
    async Dashboard()
    {
        this.$router.push("/Dashboard");
    }
    ,
    async AddPost(id){
      console.log("ThreadDetails");
      sessionStorage.setItem("Thread_id",id);
      if(this.Annoynmous == true)
      {
        this.temp = "True";
      }
      else 
      {
        this.temp = "False";
      }
      console.log("Anoynmous?");
      console.log(this.emp);
      try {
        console.log("Inside REG");
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.thread_id}/CreatePost`, {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ Post_Message: this.post_text, Annoynmous: this.temp, Poster_email: this.email, Poster_Name: this.Name }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            location.reload();
  
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
    
    },
    async Logout(){
        console.log("Logging out");
    sessionStorage.removeItem("user_id")
    sessionStorage.removeItem("Name")
        sessionStorage.removeItem("Category",this.Category);
        sessionStorage.removeItem("password",this.password);
        sessionStorage.removeItem("email",this.email);
    this.$router.push("/");  
    },
    async Summary(){
  
      this.$router.push("/Summary");    
    },
    computed: {
      filteredThread() {
        return this.AllThreads.filter(thread =>
          thread.Title.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    }
    }
  };
  </script>
  <style>
  
  table {
        border-collapse: collapse;
        width: 100%;
      }
      
      th, td {
        border: none;
        padding: 8px;
        text-align: center;
      }
  
  button {
    background: none!important;
    border: none;
    padding: 0!important;
    /*optional*/
    font-family: arial, sans-serif;
    /*input has OS specific font-family*/
    color: #069;
    text-decoration: underline;
    cursor: pointer;
  }
  </style>