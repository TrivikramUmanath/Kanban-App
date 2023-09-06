<template>
  <div class="Dashboard">
    <h1 align="left">Welcome {{ first_name }} </h1>
<h1 align="right">
    <button       @click="ExportUser()">Export/</button>
    <button @click="Summary()">Summary/</button>
    <button @click="Logout()">Logout/</button>
</h1>
    <!-- <router-link to="/Logout">Logout/        </router-link> -->
    <br></br>
    <br></br>
    <br></br>
    <img alt="Vue logo" src="../assets/kanban_logo.jpeg" />
    <Login msg="Kanban App" />
    <br></br>
    <br></br>
    <br></br>

    <!-- :to="`/Dashboard/AddList/${List}`" -->

    <div class="tableContainer" >
  <center>
    <table>
              <!-- <thead>
                  <tr>
                      <th 
                          v-for="col in columns" 
                          :key="col.label" 
                          :style="{ width: col.width + 'px' }"
                      >
                          {{ col.label }}
                      </th>
                  </tr>
              </thead> -->
              <tbody>
                  <tr v-if="isPending">
                      <td :colspan="columns.length">
                          <placeholder-rows :rows="10"></placeholder-rows>
                      </td>
                  </tr>
                  <template v-else>

                      <tc v-for="(list, inde) in List" :key="inde">
                        <td>
                            <select class="form-control" id="format" v-on:change="changeRoute($event)"> 
                                  <option selected >  {{ list.Name }}  </option> 
                                  <option>Edit List</option> 
                                  <option >Delete List</option> 
                                </select>
      
                                <br>
                              </br>
                             {{ list.Description }}
                             <br></br>
                             <!-- <p> Index </p> -->
                             <!-- {{ inde }} -->
                             <!-- {{ y }} -->
                               <!-- {{ AllCards }} -->
                               <!-- {{ List[inde]["List_Id"] }} -->
                               
                               <!-- {{ AllCards[List[inde]["List_Id"]] }} -->
<!-- {{  }} -->
<tr v-for="(qt, op) in y" :key="qt">
                    
      {{ qt.List_Id }}
                    </tr> 

                       <tr v-for="(qt, op) in AllCards[List[inde]['List_Id']]" :key="qt">
                  
                    <td>  
                      <p>Title  </p>
                      <!-- {{ qt.Title }}  -->
                      <select class="form-control" id="format" v-on:change="CardOperation($event,qt.Card_Id)"> 
                                  <option selected  >  {{ qt.Title }}  </option> 
                                  <option>Edit Card</option> 
                                  <option >Delete Card</option> 
                                  <option>Export Card</option>
                                  <option>Mark as Completed</option>
                                </select>
                        <br>
                      </br>
                      
                      
                        <p>Content  </p>
                        {{ qt.Content }}
                  
                        <br>
                      </br>
                    
                     
                          <p>Deadline  </p>
                        {{ qt.Deadline }}
                        <br>
                      </br>
                      <p>Status  </p>
                        {{ qt.Status }}
                        </td>
                        </tr> 
                               <!-- {{ AllCards[List[inde]["List_Id"]][2] }}
                               {{ AllCards[List[inde]["List_Id"]][3] }} -->
                               <!-- <td v-for="(qt, op) in AllCards[List[inde]['List_Id']]" :key="op">
                                <p>1st</p>
                               {{ qt }}
                               <p> 2nd</p>
                               {{ op }}
                               {{ AllCards[List[inde]["List_Id"]] }} 
                               </td> -->
                               <!-- <p> Y</p> -->
               
                              <!-- {{ y }} -->
                               <!-- {{ y[0][0]["Card_Id"] }} -->
                             <!-- {{ y[1] }} -->
                            

<br> </br>
                          <center>
                          <tr>
                          
                                <button @click="AddCard(list.Name)">Add Card</button>

                              </tr>
                            </center>
                            <tr>
                            </tr>
                            <center>
                              <tr>
                                <button @click="ExportList(list.List_Id)">Export</button>
                              </tr>
                            </center>
                            </td>
                            <tr>
                
                            </tr>
               <tr>

               </tr>
               <tr>

               </tr>
  

                          <tc>
                
                          </tc>
                          <tc> </tc>
                          </tc>
                  </template>
              </tbody>
          </table>

  </center>
  <br> 
</br>
<br>
</br>
</div>
    <div class="control_wrapper">
  <ejs-listbox :dataSource='data'></ejs-listbox>
</div>


    <button class="btn btn-outline-dark"  >
      
            <router-link
              style="text-decoration: none"
              :to="`/Dashboard/AddList`">
              Add List
            </router-link>
          </button>

      <!-- {{ AllCards[u[0]["List_Id"]][u[0]["Card_Id"]] }}
      <br></br>
      {{ AllCards[u[1]["List_Id"]][u[1]["Card_Id"]] }}
          <ul>
             v-for="(value, index) in trackers" :key="index" -->
    <!-- <li v-for="(value, index) in AllCards" :key="index"> -->
      <!-- <li v-for="(a, b) in index" :key="b"> -->
      <!-- {{ b }} -->
        <!-- </li> -->
      <!-- <ul> -->
        <!-- <li v-for="card in cards">
          {{ card.Title }}
        </li> -->
      <!-- </ul> -->
    <!-- </li> -->
  <!-- </ul> --> 
          <!-- <table>
            <tbody>
              <tr v-for="cards in AllCards">
        {{ cards }} -->
 <!-- <tr v-for="c in card">
{{c }}
</tr> -->
<!-- </tr> -->
<!-- </tr>
            </tbody>
          </table> -->
          <!-- {{ et }} -->
  </div>
</template>




<script>
export default {
name: "Dashboard",
data(){
      return {
          id :  sessionStorage.getItem("id"),
          token : localStorage.getItem("token"),
          List: null,
          List_Id:null,
          Lists_Id:[],
          columns: [
          { label: 'List', width: 240 },
        
      ],
      AllLists:{},
      AllCards:{},
      temp:{},
      temp2:null,
      temp1:null,
      Titles:[],
      et:{},
      u:{},
      y:[],
      first_name:localStorage.getItem("First_Name")
      }
  },
  async created()
  {
    sessionStorage.removeItem("List Name");
    sessionStorage.removeItem("List_Id");
    sessionStorage.removeItem("Card_Name");
    sessionStorage.setItem("All Cards",0);
    
    fetch(
      `http://localhost:8000/api/${this.id}/getList`,
      {
      method: "GET",
      headers:{
        "Content-Type":"application/json",
                  "Authentication-Token": `${this.token}`,
      }}).then(function(res){
                  return res.json()
              }).then(data =>{
               this.List = data;
               for (let i = 0; i < data.length; i++) {
                // console.log(i);
                this.AllCards[data[i]["List_Id"]]={};
                // console.log(this.AllCards[data[i]["List_Id"]]);
                this.List_Id=data[i]["List_Id"];
                this.AllLists[data[i]["Name"]]=data[i]["List_Id"];
                // console.log("LIST NAMESS");
                // console.log(data[i]);
                this.Lists_Id.push(data[i]["List_Id"]);
       
                // Titles[data[i]["List_Id"]]="";
                try {
      fetch(`http://localhost:8000/api/${this.List_Id}/GetCards`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.token}`,
        }
        // ,body: JSON.stringify({  List_Id: this.List_Id }),
      })
        .then((resp) => {
          return resp.json();
        })
        .then(async (register_data) => {
          // console.log(register_data);
          // console.log("list id");
          // console.log(register_data[0]["List_Id"]);
          this.u= register_data;
          this.y.push(register_data);
          for (let j = 0; j < register_data.length; j++)
          {
          if(register_data[j]["List_Id"]!=0)
          {
            // this.y.push(register_data[j])
          this.AllCards[register_data[j]["List_Id"]][register_data[j]["Card_Id"]]=register_data[j];
          // const student2 = { register_data[0]["List_Id"] : register_data[0]};
          console.log("PRINTING");
          console.log(this.AllCards);
          console.log("QWE");
          console.log(this.AllCards[register_data[j]["List_Id"]][register_data[j]["Card_Id"]]);
          const temp1=register_data[j]["List_Id"];
       
          const temp2=register_data[j];
          // let temp={$temp1:temp2};
          // console.log("TEMP");
          // console.log(temp);
          let temp3 = sessionStorage.getItem("All Cards");
          // console.log("TEMP3");
          if (temp3==0)
          {
          sessionStorage.setItem('All Cards', JSON.stringify([temp2]));
          // sessionStorage.setItem('All Cards', JSON.stringify({'1':register_data[0]}));
          }
          else{
            const temp4 = JSON.parse(temp3);
            if (temp4.length==1)
            {
              const temp6=[temp4,temp2];
              sessionStorage.setItem('All Cards', JSON.stringify(temp6));
            }
            else{
            // let temp5 =[temp4,temp2];
            temp4.push([temp2]);
            sessionStorage.setItem('All Cards', JSON.stringify(temp4));
            }
            // let temp4 = JSON.parse(temp3);
            // let temp5 =[temp4,temp2];
            // sessionStorage.setItem('All Cards', JSON.stringify(temp5));
          }
          }
        }

          // sessionStorage.setItem("All Cards",register_data);
    //       console.log("BRING IT ON");
    // this.All_Cards[data[i]["List_Id"]] = JSON.parse(sessionStorage.getItem("All Cards"));
    // console.log(JSON.parse(sessionStorage.getItem('All Cards')));
    // sessionStorage.setItem("All Cards",0);

        })
        .catch((error) => {
          console.log(error);
        });
    } catch (error) {
      console.log("Coudln't fetch cards ", error);
    }
            
               }     
               const t = this.AllLists;
              //  console.log(t);
               sessionStorage.setItem("All Lists",JSON.stringify(t));
              //  const rt = this.AllCard;
              //  console.log("RT");
        // sessionStorage.setItem('All Cards 1', JSON.stringify(rt));

              //  console.log(this.AllCards);
               
          //      for (i = 0; i < this.List.length; i++) {
          //     this.AllCards[i.List_Id] = "Ji";
          // }
          // console.log("ALL CARDS")
          // console.log(this.AllCards)
          //      sessionStorage.setItem("All Cards",this.AllCards)
              })
              // console.log("E")
              // console.log(this.List);
              // console.log(this.AllCards);
   
console.log("WEE");
console.log("ALL CARDS");
console.log(this.AllCards);
console.log("Test");
console.log(this.AllCards[1][2]);
this.et = sessionStorage.getItem("All Cards");
console.log("RE");
console.log(this.et);
  },
  mounted(){
    console.log("Mounting")
  
      // fetch(
      // `http://localhost:8000/api/${this.id}/getList`,
      // {
      // method: "GET",
      // headers:{
      // 	"Content-Type":"application/json",
      //             "Authentication-Token": `${this.token}`,
      // }}).then(function(res){
      //             return res.json()
      //         }).then(data =>{
      //          this.List = data;
      //          console.log(data)
              
      //         })
      // console.log(this.List)
      // for (i = 0; i < this.test_data.length; i++) {
      //         console.log(this);  // <------ ... IT WORKS 
      //     }




      
  },
  methods:{
    async changeRoute(e) {
      console.log(e.target["firstElementChild"]["firstChild"]["data"]);
      sessionStorage.setItem("List Name",e.target["firstElementChild"]["firstChild"]["data"]);
      if(e.target.value=="Edit List" || e.target.value=="Delete List")
      {
    this.$router.push("/Dashboard/" + e.target.value);
      }
  },
  async AddCard(wdata){
    console.log("Adding card");
    console.log(wdata);
    sessionStorage.setItem("List_Name",wdata);
    this.$router.push("/Dashboard/Add Card");
  },
  async ExportList(w){
    console.log("Exporting List Data");
      fetch(`http://localhost:8000/Dashboard/${w}/ExportList`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.token}`}})
  }
,
  async CardOperation(e,r){
    console.log("Card Operation");
    console.log(e.target.value);
    console.log(e.target["firstElementChild"]["firstChild"]["data"]);
    sessionStorage.setItem("Card_Name",e.target["firstElementChild"]["firstChild"]["data"]);
      if(e.target.value=="Edit Card" || e.target.value=="Delete Card")
      {
    this.$router.push("/Dashboard/" + e.target.value);
      }
      if(e.target.value=="Export Card")
      {
        fetch(`http://localhost:8000/Dashboard/${r}/ExportCard`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.token}`}})
        }
        if(e.target.value=="Mark as Completed")
      {
        console.log("MARKED COMPLETED");
        fetch(`http://localhost:8000/api/${this.id}/${r}/EditCard`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
          body: JSON.stringify({  Status:"Completed" }),
        }).then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            this.$router.go();
          })
          .catch((error) => {
            console.log(error);
          })
        // let epoq=0;
        // setTimeout(function(){ alert("After 5 seconds!"); }, 5000);
        console.log("Reloading now");
        console.log("Reloaded");
      }                   
    // this.$router.push("/Dashboard/Add Card");
  },
  async ExportUser(){
    console.log("Exporting User Data");
      fetch(`http://localhost:8000/Dashboard/${this.id}/ExportUser`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Authentication-Token": `${this.token}`}})
  },
  async Logout(){
    console.log("Logging out");
    sessionStorage.removeItem("id")
    localStorage.removeItem("id")
    localStorage.removeItem("token")
    localStorage.removeItem("First_Name")
    this.$router.push("/");    
  },
  async Summary(){

    this.$router.push("/Summary");    
  }

  }
};
</script>
<style>

table, th, td ,tbody{
  border: 2px solid;
  border-spacing: 30px;
}
tc{
  border: 1px solid white;
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
