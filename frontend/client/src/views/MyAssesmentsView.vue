<template>
  <div class="MyAssesments">
    <!-- <h1 align="left">Welcome {{ Name }} </h1> -->
<h1 align ="right">
  <button  @click="Dashboard()">Dashboard</button> 
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
        <label for="AssesmentName">Assesment Name</label>
            <input type="text" name="AssesmentName" v-model="AssesmentName" required>

            <br></br>
            <input type="file" accept=".csv" @change="handleFileUpload( $event )"/>
        <br>
           </br>
        <p><button name="AddAssesment" @click=AddAssesment()>  Add Assesment </button> </p>
        
          <p v-if="parsed"> Added Quiz as below </p>
        <table v-if="parsed" style="width: 100%;">
    <thead>
        <tr>
            <th v-for="(header, key) in content.meta.fields"
                v-bind:key="'header-'+key">
                {{ header }}
            </th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(row, rowKey) in content.data"
            v-bind:key="'row-'+rowKey">
                <td v-for="(column, columnKey) in content.meta.fields"
                    v-bind:key="'row-'+rowKey+'-column-'+columnKey">
                        {{ content.data[rowKey][column]  }}
                </td>
        </tr>
    </tbody>


    <h1>My Assesments </h1>
</table>

    <table>
      <thead>
        <tr>
          <th>Assesment Name</th>
          <th>Toppers</th>
          <th>Student Count</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="asses in AllAssesmentsUsers" :key="asses.assesment_id">
         
          <td>{{ asses.Name }} </td>
          <td>{{ asses.Toppers }}</td>
          <td>{{ asses.Student_Count  }}  </td>
          <td><button @click=CheckAllScores(asses.assesment_id,asses.Name)>  Check All Scores </button> </td>
          <td><button @click=ViewScoreStats(asses.assesment_id,asses.Name)>  View Stats </button> </td>
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
name: "MyAssesments",
data(){
      return {
          user_id :  sessionStorage.getItem("user_id"),
          Name: sessionStorage.getItem("Name"),
          Category: sessionStorage.getItem("Category"),
          isJunior: true,
          password: sessionStorage.getItem("password"),
          file: '',
          content: [],
          AssesmentName:'',
          AllAssesmentsUsers:{},
          parsed: false,
          assesment_id:'',
          dummy:'',
          ui:'',
          aspirants:'',
          scoreData:{'0-40':0,'40-50':0,'50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0},
          freq:[],
      }
  },
  async created()
  {
      this.content=[]
      return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/GetAssesmentsUser`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
          })
        .then((response) => response.json())
        .then((re_data) => {
          console.log(re_data);
          this.AllAssesmentsUsers=re_data;
  
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
  async AddAssesment(){
    console.log("Add Assesment");
    Papa.parse( this.file, {
        header: true,
        skipEmptyLines: true,
        complete: function( results ){
            this.content = results;
            console.log(this.content);
            console.log(results);
            this.parsed = true;
            try {
        console.log("Inside Add Assesment");
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/CreateAssesment`, {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ Name: this.AssesmentName , Quiz: [this.content.data] }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            console.log(register_data);
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
        }.bind(this)
    } );
   
    
  },
  async handleFileUpload( event ){
    this.file = event.target.files[0];
    this.parseFile();
    
},
async CheckAllScores(yu,ae)
{
  this.dummy = yu;
  sessionStorage.setItem("assesment_id_forAspirant",this.dummy);
  sessionStorage.setItem("AssName",ae);
  this.$router.push("/Assesment/CheckAllScores");

  },
async ViewScoreStats(yu,ae)
{
  this.dummy = yu;
  sessionStorage.setItem("assesment_id_forAspirant",this.dummy);
  sessionStorage.setItem("AssName",ae);
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
          let scores=[]
          for(let i=0;i<re_data.length;i++)
          {
            scores.push(re_data[i].aspirant_score);
          }        
          for (let i=0;i<scores.length;i++)
          {
            let s = parseInt(scores[i])
            if(s>90 && s<=100)
            {
              this.scoreData['90-100']=this.scoreData['90-100']+1
            }
            else if(s>80 && s<=90)
            {
              this.scoreData['80-90']=this.scoreData['80-90']+1 
            }
            else if(s>70 && s<=80)
            {
              this.scoreData['70-80']=this.scoreData['70-80']+1 
            }
            else if(s>60 && s<=70)
            {
              this.scoreData['60-70']=this.scoreData['60-70']+1 
            }
            else if(s>50 && s<=60)
            {
              this.scoreData['50-60']=this.scoreData['50-60']+1 
            }
            else if(s>40 && s<=50)
            {
              this.scoreData['40-50']=this.scoreData['40-50']+1 
            }
            else 
            {
              this.scoreData['0-40']=this.scoreData['0-40']+1 
            }
          }
         let values = Object.values(this.scoreData) ;
         console.log("Values are ");
         console.log(values);
         this.freq=values;
         sessionStorage.setItem("Freq",[this.freq]);
  console.log("Aspirants are");
  console.log(this.aspirants);
  console.log("Score Stats score");
this.$router.push("/Assesment/ViewScoreStats");
        })


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