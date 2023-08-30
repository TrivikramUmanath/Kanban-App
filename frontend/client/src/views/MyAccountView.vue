<template>
 
    <div class="MyAccount"> 
        <h1>My Profile </h1>
       <h1 align ="right">
           <button  @click="Dashboard()">Dashboard</button> 
       <button v-if="Category == 'Junior'" @click="Assesments()">Assesments/</button>
       <button v-else @click="MyAssesments()">My Assesments/</button> 
       <button  @click="MyThreads()">MyThreads/</button> 
       <button v-if="Category == 'POD'" @click="Summary()">SummaryStats/</button>
         <button @click="Logout()">Logout/</button>
     
     </h1>
     
         <img alt="Vue logo" src="../assets/Placement_Logo.jpg" />
         <Login msg="Placement Portal" />
       
     <br>
     
     </br>
     <br>
     </br>

  <label for="users">Select a User:         </label>
  <select id="users" v-model="selectedUser">
    <option value="">Select an option</option>
    <option v-for="user in AllUsers" :key="user.user_id" :value="user.user_id">{{ user.Name }}</option>
  </select>
  <p v-if="connectionStatus == 'Request Sent' "> {{ connectionStatus }}</p>
<p> </p>
<button @click="SendConnection()">SendConnection</button>
<p> </p>
<p> </p>
<p> </p>
     <input type="text" v-model="req" name="req" placeholder="Request Message" />
<br>
</br>
<p></p>
     <br>
    </br>
     <br>
     </br>

     <p> Name {{ Name }}  </p>
     <p> User Type {{ Category }}  </p>
     <br></br>
     <br></br>

         <div id="app">
           <center>
            <p> Message Requests </p>
         <table>
           <thead>
             <tr>
               <th>From </th>
               <th>Message</th>
             </tr>

           </thead>
           <tbody>
             <tr v-for="connection in AllConnections" :key="connection.connection_id">
               <td  v-if="connection.Approval_Status == 'Not Responded'">{{ connection.Sender_Name }}</td>
               <td  v-if="connection.Approval_Status == 'Not Responded'">{{ connection.Request }} </td>
               <td   v-if='connection.Approval_Status == "Not Responded"'>     
                <button  @click="AcceptRequest(connection.connection_id)">Accept </button>
  <br></br> 
         <button @click="RejectRequest(connection.connection_id)">Reject       </button>  
     </td>

             </tr>
           </tbody>
        </table>
         <br>
       </br>
       <p> Active Connections </p>
         <table>
           <thead>
             <tr>
               <th>Names</th>

             </tr>

           </thead>
           <tbody>
             <tr v-for="connection in AllConnections" :key="connection.connection_id">
               <td v-if="connection.Approval_Status == 'Accept'">
                <button @click="ViewConnection(connection.connection_id)">{{ connection.Sender_Name }}     </button>
            </td>
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
     name: "MyAccount",
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
               AllConnections:null,
               temp:'',
               selectedUser:'',
               Annoynmous:false,
               thread_Name: sessionStorage.getItem("Thread Name"),
               req:'',
               connection_id:'',
               connectionStatus:'',
               selectedOption: null,
               AllUsers:{},
    options: [
      { id: 1, name: 'Accept' },
      { id: 2, name: 'Reject' }
    ],
         message: 'Hello, Vue!'
           }
       },
       async created()
       {
         return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/getConnections`, {
               method: "GET",
               headers: {
                 "Content-Type": "application/json;charset=utf-8",
               },
             })
           .then((response) => response.json())
           .then((re_data) => {
               console.log("All Connections");
             console.log(re_data);
             this.AllConnections=re_data;
     
           })
           .catch((error) => console.log(error));
        console.log("Yes");



       },
       mounted(){
         console.log("Mounting");
         return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/getUsers`, {
               method: "GET",
               headers: {
                 "Content-Type": "application/json;charset=utf-8",
               },
             })
           .then((response) => response.json())
           .then((re_data) => {
               console.log("All Users");
             console.log(re_data);
             this.AllUsers=re_data;

           })
           .catch((error) => console.log(error));
        console.log("Yes");
       },
       methods:{
       async Dashboard()
       {
        
           this.$router.push("/Dashboard");
       },
       async Summary(){
  
  this.$router.push("/Summary");    
},
       
       async SendConnection(){
         console.log("Sending Connection");
         try {
           console.log(this.req);
           fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/CreateConnection`, {
             method: "POST",
             headers: {
               'Access-Control-Allow-Origin': '*',
          'Content-type': 'application/json',
             },
             body: JSON.stringify({ Sender_Name: this.Name, receiver_id: this.selectedUser, sender_id: this.user_id ,Request: this.req }),
           })
             .then((resp) => {
               return resp.json();
             })
             .then(async (register_data) => {
                this.connectionStatus="Request Sent";
             })
             .catch((error) => {
               console.log(error);
             });
         } catch (error) {
           console.log("Unsuccessful Save ", error);
         }
       
       },
       async MyThreads()
       {
        this.$router.push("/MyThreads");
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
       async ViewConnection(n){
        sessionStorage.setItem("connection_id",n);
     this.$router.push("/MyAccounts/MessageRecords");    
   },
   async RejectRequest(id)
   {
   try
       {
        this.connection_id = id;
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/Connection/${this.connection_id}`, {
             method: "PUT",
             headers: {
               'Access-Control-Allow-Origin': '*',
          'Content-type': 'application/json',
             },
             body: JSON.stringify({  Approval_Status: "Reject" }),
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
         }catch (error) {
           console.log("Unsuccessful Save ", error);
         }
        },
        async AcceptRequest(id)
        {
       try
       {
        this.connection_id = id;
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/Connection/${this.connection_id}`, {
             method: "PUT",
             headers: {
               'Access-Control-Allow-Origin': '*',
          'Content-type': 'application/json',
             },
             body: JSON.stringify({  Approval_Status: "Accept" }),
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
         }catch (error) {
           console.log("Unsuccessful Save ", error);
         }
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