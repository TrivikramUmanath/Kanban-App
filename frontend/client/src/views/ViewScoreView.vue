<template>
    <div class="ViewScore">

  <h1 align ="right">
    <button  @click="Dashboard()">Dashboard</button> 
    <button  @click="MyAssesments()">MyAssesments/</button>
         <button  @click="MyThreads()">MyThreads/</button> 
         <button v-if="Category == 'POD'" @click="Summary()">SummaryStats/</button>
           <button @click="Logout()">Logout/</button>
  
  </h1>
  
  
    
  
      <img alt="Vue logo" src="../assets/Placement_Logo.jpg" />
      <Login msg="Placement Portal" />
    
  <br>
  
  </br>
  <p><button name="Refresh" @click=Refresh()>  Refresh </button> </p>
  <br>
  </br>
  
      <div id="app">
  
        <center>
            <h2> {{ AssName }} </h2>
            <table>
        <thead>
          <tr>
            <th>Student Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="asp in aspirants" :key="asp.aspirant_id">
           
            <td>{{ asp.aspirant_name }}</td>
            <td>{{ asp.aspirant_score }} </td>
          </tr>
        </tbody>
      </table>


    <p></p>
    <p></p>
    <br></br>
    </center>
    </div>
  
    </div>
  
  </template>
  
  
  
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script>
  
  export default {
  name: "ViewScore",
  data(){
        return {
            user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            password: sessionStorage.getItem("password"),
            assesment_id: sessionStorage.getItem("Assesment_id"),
            aspirants:null,
    dummy:sessionStorage.getItem("assesment_id_forAspirant"),
    AssName:sessionStorage.getItem("AssName")
        }
    },
    async created()
    {
        return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.dummy}/Aspirant`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json;charset=utf-8",
              },
            })
          .then((response) => response.json())
          .then((re_data) => {
            console.log(re_data);
            this.aspirants=re_data;
          }
          )
    console.log("Aspirants are");
    console.log(this.aspirants);
        
      console.log("Created");
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
      console.log("Logging out");
      sessionStorage.removeItem("user_id")
      sessionStorage.removeItem("Name")
      this.$router.push("/MyAccount");    
    },
    async Dashboard()
         {
             this.$router.push("/Dashboard");
         },
         async MyThreads()
         {
          this.$router.push("/MyThreads");
         },
    async Refresh()
    {
      console.log("Reloading");
      location.reload();
    },
    async Logout(){
      console.log("Logging out");
      sessionStorage.removeItem("user_id");
      sessionStorage.removeItem("Name");
      sessionStorage.removeItem("Assesment_id");
          sessionStorage.removeItem("Category");
          sessionStorage.removeItem("password");
          sessionStorage.removeItem("email");
          sessionStorage.clear();
          this.$router.push("/");    
    },
    async Summary(){
  
  this.$router.push("/Summary");    
},
    async MyAssesments()
  {
    this.$router.push("/MyAssesments");  
  },
    
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