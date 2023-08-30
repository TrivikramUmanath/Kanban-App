<template>
    <div class="Assesments">
      <!-- <h1 align="left">Welcome {{ Name }} </h1> -->
  <h1 align ="right">
    <button  @click="Dashboard()">Dashboard</button> 
         <button  @click="MyThreads()">MyThreads/</button> 
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
            <h1> Assesments </h1>

  
      <table>
        <thead>
          <tr>
            <th>Assesment Name</th>
            <th>Toppers</th>
            <th>Student Count</th>
            <th>Attempt Quiz/View Score</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="asses in AllAssesments" :key="asses.assesment_id">
           
            <td>{{ asses.Name }} </td>
            <td>{{ asses.Toppers }}</td>
            <td>{{ asses.Student_Count  }}  </td>
         
    <td  v-if="unattempted.includes(asses.assesment_id)" ><button @click=AttemptQuiz(asses.assesment_id)> Attempt Quiz </button> </td>
    <td  v-if="attempted.includes(asses.assesment_id)" ><button @click=ViewScore(asses.assesment_id)>  View Score </button> </td>
    <td  v-if="asses.assesment_id == score_id" >  {{ score }} </td>
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
  import Papa from 'papaparse';
  import axios from 'axios';
  export default {
  name: "Assesments",
  data(){
        return {
            user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            password: sessionStorage.getItem("password"),
            file: '',
            content: [],
            content1:[],
            AssesmentName:'',
            AllAssesments:{},
            AllAspirants:{},
            parsed: false,
            assesment_id:'',
            unattempted:[],
            attempted:[],
            allAsses:[],
            Aspirant_Scores:{},
            ALLASS:{},
            score_id:'',
            score:''
        }
    },
    async created()
    {
        return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/getAllAssesments`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json;charset=utf-8",
              },
            })
          .then((response) => response.json())
          .then((re_data) => {
            console.log(re_data);
            this.AllAssesments=re_data;
            for (let i = 0; i < re_data.length; i++) {
                this.allAsses.push(re_data[i]["assesment_id"]);       
                this.ALLASS[re_data[i]["assesment_id"]]= re_data[i];  
                } 
        return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/Aspirant/getAllAspirantsUsers`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json;charset=utf-8",
              },
            })
          .then((response) => response.json())
          .then((re_data) => {
            console.log(re_data);
            this.AllAspirants=re_data;
            for (let i = 0; i < re_data.length; i++) {
            this.attempted.push(re_data[i]["assesment_id"]);  
            this.Aspirant_Scores[re_data[i]["assesment_id"]]=re_data[i]["aspirant_score"]; 
            } 
            // print("All");
            console.log("ALL");
            console.log(this.allAsses);
            console.log("Attempted");
            console.log(this.attempted);
            console.log("Unattempted");
            let A = this.allAsses;
            let B = this.attempted;
            let diff = A.filter(x => !B.includes(x));
            console.log("Set-Difference: " + diff);
            this.unattempted = diff;
            console.log(this.unattempted);
          })
          .catch((error) => console.log(error));
    
          })
          .catch((error) => console.log(error));

        
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
      this.$router.push("/MyAssesments");
    },
    async Logout(){
      console.log("Logging out");
      sessionStorage.removeItem("user_id");
      sessionStorage.removeItem("Name");
          sessionStorage.removeItem("Category");
          sessionStorage.removeItem("password");
          sessionStorage.removeItem("email");
          sessionStorage.clear();
      this.$router.push("/");    
    },
    async ViewScore(rop)
    {
      console.log(this.Aspirant_Scores[rop]);
      this.score_id=rop;
      this.score=this.Aspirant_Scores[rop]
      console.log("Inside score");      
    },
    async AttemptQuiz(to)
    {
      this.$router.push("/Assesment/AttemptQuiz");  
      sessionStorage.setItem("Assesment_id",to);
      console.log("Let's see");
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