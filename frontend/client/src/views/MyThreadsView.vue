<template>
    <div class="MyThreads">
      <h1 align="left">Welcome {{ Name }} </h1>
  <h1 align ="right">
    <button  @click="MyAccount()">My Account</button> 
    <button v-if="Category == 'Junior'" @click="Assesments()">Assesments/</button>
    <button v-else @click="MyAssesments()">My Assesments/</button> 
    <button v-if="Category == 'POD'" @click="Summary()">SummaryStats/</button>
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
  
      <div id="app">
  
        <center>
          <p><button name="AddThread" @click=AddThread()>  Add Thread </button> </p>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>TimeStamp</th>
            <th>Post Count</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="thread in AllThreadsUser" :key="thread.thread_id">
           
            <td>{{ thread.thread_id }} </td>
            <td><button @click=ThreadDetails(thread.thread_id,thread.Title)>  {{ thread.Title }}   </button> </td>
            <td>{{ thread.Thread_Map }}</td>
            <td>{{ thread.Thread_count  }}  </td>
          </tr>
        </tbody>
      </table>
      <br>
    </br>
  
    </center>
    </div>
  
    </div>
  
  </template>
  
  
  
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script>
  export default {
  name: "MyThreads",
  data(){
        return {
            user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            AllThreadsUser:null,
            searchQuery: '',
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            password: sessionStorage.getItem("password"),
            thread_id:null,
      message: 'Hello, Vue!'
        }
    },
    async created()
    {
      
   
      sessionStorage.setItem("All Threads",0);
      return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/getThreadsUser`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
          })
        .then((response) => response.json())
        .then((re_data) => {
          console.log(re_data);
          this.AllThreadsUser=re_data;
  
        })
        .catch((error) => console.log(error));
    },
    mounted(){
      console.log("Mounting");
  
      if(this.Category == "Junior")
      {
        this.isJunior = true;
      }  
      console.log(this.Junior);
      console.log(this.Category);
    },
    methods:{
      async MyAccount(){
      console.log("Going to My Account Page");
      this.$router.push("/MyAccount");    
    },
    async ThreadDetails(id,ro){
      console.log("ThreadDetails");
      sessionStorage.setItem("thread_id",id);
      sessionStorage.setItem("Thread Name",ro);
      this.$router.push("/Dashboard/ThreadDetails");    
    },
    async AddThread(){
      console.log("Add Thread");
      this.$router.push("/Dashboard/AddThread");    
    },
    async MyAssesments()
    {
      this.$router.push("/Dashboard/MyAssesments");  
    },
    async Assesments()
    {
      this.$router.push("/Dashboard/Assesments");  
    }
    ,
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
        return this.AllThreadsUsers.filter(thread =>
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