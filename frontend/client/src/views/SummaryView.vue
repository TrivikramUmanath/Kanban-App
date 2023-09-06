<template>
    <div>
        <h1>Dashboard</h1>
    <router-link to="/Dashboard">Home/</router-link>
    <button @click="Logout()">Logout/</button>
<br></br>
<br></br>
    <div class="tableContainer" >
  <center>
    <table>

              <tbody>
                  <tr v-if="isPending">
                      <td :colspan="columns.length">
                          <placeholder-rows :rows="10"></placeholder-rows>
                      </td>
                  </tr>
                  <template v-else>
          
                      <tc v-for="list in List_Names" >
                        <td>
                            <select class="form-control" id="format" v-on:change="changeRoute($event)"> 
                                  <option selected >  {{ list }}  </option> 
                                </select>
                                <br>
                            </br>
                            <p>Completed Tasks:  
                            {{ Tasks[list]["Completed"] }}
                          </p>
                            <p>Pending Tasks:  
                            {{ Tasks[list]["Pending"] }}
                          </p>
                          <p>Passed Deadlines:  
                            {{ Tasks[list]["Passed Deadline"] }}
                          </p>
                            
                              <Bar
    :chart-options="chartOptions"
    :chart-data=BarData[list]
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
                            </td>
                            </tc>
                </template>
            
                </tbody>
    </table>
    </center>

    </div>
 
    </div>
  </template>
  
  <script>

import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ],
      },
      chartOptions: {
        responsive: true
      },
            id:sessionStorage.getItem("id"),
            token:localStorage.getItem("token"),
            AllLists:JSON.parse(sessionStorage.getItem("All Lists")),
            AllCards:JSON.parse(sessionStorage.getItem("All Cards")),
            Tasks:{},
            List_Names:[],
            Images:"",
            TR:{},
            BarData:{},
        }
      },
      async created(){
            console.log(this.AllLists) ;
            this.List_Names= Object.keys(this.AllLists);
            console.log("ALL CARD");
            console.log(this.chartData.labels);
            let r = Object.values(this.AllCards);
            let k=Object.keys(this.AllCards);
            let e={};
            let finale={};
            for (const [key, value] of Object.entries(this.AllLists)) {
          console.log(key, value);
          finale[key]={"labels":[],datasets:[]};
          e[key]={"Completed":0,"Pending":0,"Deadlines":[],"Passed Deadline":0};
          // this.Tr[key]={};
          // this.Tr[key]={"Completed":0,"Pending":0};
            console.log(e);
  
            let deadli=[];
            let ty=[];
          for (let j = 0; j < k.length; j++)
          {
            let t={};
           
              try{
              console.log(r[j][0]["Title"]);
              t=r[j][0];
              }
              catch{
                console.log(r[j]["Title"]);
                t=r[j];
              }
              if (value==t["List_Id"])
              {
                console.log("HELLO");
                if (t["Status"]=="Completed")
                {
                    e[key]["Completed"]=e[key]["Completed"]+1;
                    console.log(t["Deadline"])
                }
                else{
                  e[key]["Pending"]=e[key]["Pending"]+1;
                  deadli.push(t["Deadline"]);
                  ty.push(new Date(t["Deadline"]))
                }
              }
          }
          console.log("Pending Dates for List"+value);
          console.log(deadli);
          console.log("Pending Dates for TY"+value);
          console.log(ty);
         
          ty.sort((date1, date2) => new Date(date1).setHours(0, 0, 0, 0) - new Date(date2).setHours(0, 0, 0, 0));
          // deadli.sort(function(a,b){return a.getDate() - b.getDate()});
          console.log("Sorted Pending Dates for TY"+value);
          console.log(ty);
          // e[key]["Deadlines"]=ty;
          // finale[key]["labels"]=ty;
          const map = {};
          const convert=[];
          let Deadline_Passed=0;
          var current_time = new Date();
          console.log("CURRENT TIME");
          console.log(current_time);
          for(let p = 0; p < ty.length; p++){
      map[ty[p]] = (map[ty[p]] || 0) + 1;
      
      if(current_time>ty[p])
      {
        Deadline_Passed=Deadline_Passed+1;
      }
      convert.push(ty[p].toDateString());

              }
              console.log("FREQUENCY")
              console.log(Deadline_Passed);
              // console.log(Object.values(map));
              let u=[];
              for (const [key, value] of Object.entries(map)) {
              console.log(value);
             u.push(value);
             console.log(u);
        }
        console.log("u")
        console.log(u);
        let unique = convert.filter((item, i, ar) => ar.indexOf(item) === i);
                  // e[key]["Deadlines"]=convert;
          // finale[key]["labels"]=convert;
          // console.log(convert);
          e[key]["Deadlines"]=unique;
          finale[key]["labels"]=unique;
          e[key]["Passed Deadline"]=Deadline_Passed;
          console.log(unique);
        finale[key]["datasets"]=[{ "data":u,"barPercentage": 1,
        "maxBarThickness": 20,
        "minBarLength": 2,"backgroundColor":"Blue"}];
      }
 
        
        console.log("FINAL E");
        console.log(finale);
        this.Tasks=e;
        console.log(this.Tasks);
        this.BarData=finale;

          //   for (let j = 0; j < k.length; j++)
          // {
          //   for(let h=0;h<this.List_Names.length;h++)
          //   {
          //     let t={}
          //     try{
          //     console.log(r[j][0]["Title"]);
          //     t=r[j][0];
          //     }
          //     catch{
          //       console.log(r[j]["Title"]);
          //       t=r[j];
          //     }
          //     // if (this.AllLists[h]==t["List_Id"])
          //     // {
          //     // this.Tr[this.List_Names[h]]={"Completed":0,"Pending":0}
          //     // if (t["Status"]=="Completed")
          //     // {
          //     //   this.Tr[this.List_Names[h]]["Completed"]= this.Tr[this.List_Names[h]]["Completed"]+1;
          //     // }
          //     // else{
          //     //   this.Tr[this.List_Names[h]]["Pending"]= this.Tr[this.List_Names[h]]["Pending"]+1;
          //     // }
          //     // }
          //   }
            
          // }
   

      //           fetch(`http://localhost:8000/${this.id}/SummaryStats`, {
      //   method: "GET",
      //   headers: {
      //     "Content-Type": "application/json;charset=utf-8",
      //     "Authentication-Token": `${this.token}`,
      //   }
      //   // ,body: JSON.stringify({  List_Id: this.List_Id }),
      // }).then(function(response) {
      //           console.log("HELLOR");
      //           console.log(response);

			// 	return response.json()
			// }).then(function(rdata) {
      //           console.log("FOUND STATS");
      //           console.log(rdata);
      //           this.Tr=rdata;
      //           console.log(rdata.image_encoded);
      //           this.Images=rdata.image_encoded; 
      //           console.log("THIS IMAGE");
      //           console.log(this.Images);
  
			// })

      }
    };
  </script>