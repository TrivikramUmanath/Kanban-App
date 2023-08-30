<template>
  <div class="SummaryView">

<h1 align ="right">
  <button  @click="Dashboard()">Dashboard</button> 
  <button  @click="MyAccount()">My Account</button> 
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

    <div id="app">

      <center>
    <table>
<p>Top Topics</p>
      <thead>
        <tr>
          <th>Thread Name</th>
          <th>Thread Count</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="thread in TopTopics" :key="thread.thread_id">
         
          <td>{{ thread.Title }} </td>
          <td>{{ thread.Thread_count  }}  </td>
        </tr>
      </tbody>
      <p>Top Assesments</p>
      <thead>
        <tr>
          <th>Assesments Name</th>
          <th>Student Count</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="thread in TopAsses" :key="thread.assesment_id">
         
          <td>{{ thread.Name }} </td>
          <td>{{ thread.Student_Count  }}  </td>
        </tr>
      </tbody>
      <p>Top Contributors</p>
      <thead>
        <tr>
          <th>User Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="thread in TopContri" :key="thread.post_id">
         
          <td>{{ thread.Poster_Name }} </td>
          <!-- <td>{{ thread.Thread_count  }}  </td> -->
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
name: "SummaryView",
data(){
      return {
          user_id :  sessionStorage.getItem("user_id"),
          Name: sessionStorage.getItem("Name"),
          TopContri:null,
          TopAsses:null,
          TopTopics:null,
          Category: sessionStorage.getItem("Category"),
          isJunior: true,
          password: sessionStorage.getItem("password")
      }
  },
  async created()
  {
    
 
    console.log("LET'S START WITH CONTRI");
    return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/TopContri`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
        })
      .then((response) => response.json())
      .then((re_data) => {
        console.log(re_data);
      this.TopContri = re_data;

        console.log("LET'S START WITH ASSES");
      return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/TopAsses`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
        })
      .then((response) => response.json())
      .then((re_data) => {
        console.log(re_data);
        this.TopAsses=re_data;

        console.log("LET'S START WITH Topics");
      return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/TopTopics`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
        })
      .then((response) => response.json())
      .then((re_data) => {
        console.log(re_data);
        this.TopTopics=re_data;

      })
      .catch((error) => console.log(error));

      })
      .catch((error) => console.log(error));





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
  async Dashboard()
       {
           this.$router.push("/Dashboard");
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