<template>
 
    <div class="MessageRecord"> 
       <h1 align ="right">
           <button  @click="MyAccount()">My Account</button> 
           <button  @click="Dashboard()">Dashboard</button> 
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
         <table>
           <thead>
             <tr>
               <th>Sender</th>
               <th>Message</th>
               <th>TimeStamp</th>
             </tr>
           </thead>
           <tbody>
             <tr v-for="sms in AllMessages" :key="sms.message_id">
              
               <td>{{ sms.Message_Sender }}</td>
               <td>{{ sms.Content }} </td>
               <td>{{ sms.Message_Date_Time }} </td>
             </tr>
           </tbody>
         </table>
         <br>
       </br>
         <input type="text" v-model="sms_text" name="sms_text" placeholder="Type Message" />
   <br>
   </br>
   
   <p><button name="AddPost" @click=AddMessage()>  Add Message </button> </p>
   
    
        
       </center>
       </div>
     
       </div>
     </template>
     
     
     
     <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
     <script>
     export default {
     name: "MessageRecords",
     data(){
           return {
               user_id :  sessionStorage.getItem("user_id"),
               Name: sessionStorage.getItem("Name"),
               connection_id: sessionStorage.getItem("connection_id"),
               searchQuery: '',
               Category: sessionStorage.getItem("Category"),
               isJunior: true,
               email: sessionStorage.getItem("email"),
               password: sessionStorage.getItem("password"),
               AllPosts:null,
               AllMessages:{},
               temp:'',
               Annoynmous:false,
               thread_Name: sessionStorage.getItem("Thread Name"),
               post_text:'',
         message: 'Hello, Vue!'
           }
       },
       async created()
       {
         return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.connection_id}/getMessages`, {
               method: "GET",
               headers: {
                 "Content-Type": "application/json;charset=utf-8",
               },
             })
           .then((response) => response.json())
           .then((re_data) => {
               console.log("All Messages");
             console.log(re_data);
             this.AllMessages=re_data;
     
           })
           .catch((error) => console.log(error));
       },
       mounted(){
         console.log("Mounting");
       },
       methods:{
         async MyAccount(){
         console.log("Logging out");
        //  sessionStorage.removeItem("user_id")
        //  sessionStorage.removeItem("Name")
         this.$router.push("/MyAccount");    
       },
       async Dashboard()
       {
           this.$router.push("/Dashboard");
       },
       async Summary(){
  
  this.$router.push("/Summary");    
},
       async AddMessage(id){
         try {
           console.log("Inside REG");
           fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.connection_id}/CreateMessage`, {
             method: "POST",
             headers: {
               'Access-Control-Allow-Origin': '*',
          'Content-type': 'application/json',
             },
             body: JSON.stringify({ Content: this.sms_text, Message_Sender: this.Name }),
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