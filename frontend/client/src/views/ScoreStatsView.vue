<template>
  <div class="ScoreStats">

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


              
    <div>
      <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
  </div>

  <p></p>
  <p></p>
  <br></br>
  </center>
</div>
</div>

</template>



<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
<script>

import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ['0-40','40-50','50-60','60-70','70-80','80-90','90-100'],
        datasets: [
          {
            label: 'Score Analysis',
            backgroundColor: 'rgba(75, 192, 192, 0.4)',
            data: sessionStorage.getItem("Freq").split(",")
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
      user_id :  sessionStorage.getItem("user_id"),
          Name: sessionStorage.getItem("Name"),
          Category: sessionStorage.getItem("Category"),
          isJunior: true,
          password: sessionStorage.getItem("password"),
          assesment_id: sessionStorage.getItem("Assesment_id"),
          aspirants:null,
          scoreData:{'0-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0},
  dummy:sessionStorage.getItem("assesment_id_forAspirant"),
  AssName:sessionStorage.getItem("AssName"),
  freq:JSON.stringify(sessionStorage.getItem("Freq"))
  }
},
  async created()
  {
    console.log("FREQUENCY IS");
    console.log(typeof( this.freq));
    console.log([1,2,3,4]);
  //     return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.dummy}/Aspirant`, {
  //           method: "GET",
  //           headers: {
  //             "Content-Type": "application/json;charset=utf-8",
  //           },
  //         })
  //       .then((response) => response.json())
  //       .then((re_data) => {
  //         console.log(re_data);
  //         this.aspirants=re_data;
  //         let scores=[]
  //         for(let i=0;i<re_data.length;i++)
  //         {
  //           scores.push(re_data[i].aspirant_score);
  //         }        
  //         for (let i=0;i<scores.length;i++)
  //         {
  //           let s = parseInt(scores[i])
  //           if(s>90 && s<=100)
  //           {
  //             this.scoreData['90-100']=this.scoreData['90-100']+1
  //           }
  //           else if(s>80 && s<=90)
  //           {
  //             this.scoreData['80-90']=this.scoreData['80-90']+1 
  //           }
  //           else if(s>70 && s<=80)
  //           {
  //             this.scoreData['70-80']=this.scoreData['70-80']+1 
  //           }
  //           else if(s>60 && s<=70)
  //           {
  //             this.scoreData['60-70']=this.scoreData['60-70']+1 
  //           }
  //           else if(s>50 && s<=60)
  //           {
  //             this.scoreData['50-60']=this.scoreData['50-60']+1 
  //           }
  //           else if(s>40 && s<=50)
  //           {
  //             this.scoreData['40-50']=this.scoreData['40-50']+1 
  //           }
  //           else 
  //           {
  //             this.scoreData['0-40']=this.scoreData['0-40']+1 
  //           }
  //         }
  //        let values = Object.values(this.scoreData) ;
  //        console.log("Values are ");
  //        console.log(values);
  //        this.freq=values;
  //        this.chartData["datasets"]["data"]=[0,0,0,1,0,0,1];
  //        console.log(this.chartData);
  // console.log("Aspirants are");
  // console.log(this.aspirants);
  //   console.log("Created");
  //       })
  },
  mounted(){
    console.log("Mounting");

    if(this.Category == "Junior")
    {
      this.isJunior = true;
    }  
    console.log(this.Junior);
    console.log(this.Category);
   
  //        this.chartData["datasets"]["data"]=[0,0,0,1,0,0,1];
  //        console.log(this.chartData);
  // console.log("Aspirants are");
  // console.log(this.aspirants);
  //   console.log("Created");
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