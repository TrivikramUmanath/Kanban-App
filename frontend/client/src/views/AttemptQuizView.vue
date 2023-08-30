<template>
    <div class="AttemptQuiz">

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
            <h2> {{ AssesmentName }} </h2>

    <div v-for="(question, index) in questions" :key="index">
      <p>Question {{ index+1  }} {{ question.text }}</p>
      <label v-for="(option, optionIndex) in question.options" :key="optionIndex">
        <input
          type="radio"
          :name="'question_' + index"
          :value="option"
          v-model="selectedAnswers[index]"
        >
        {{ option }}
      </label>
    </div>
    <p></p>
    <p></p>
    <br></br>
    <button @click="submit()">Submit</button>
    </center>
    </div>
  
    </div>
  
  </template>
  
  
  
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script>
  import Papa from 'papaparse';
  import axios from 'axios';
  export default {
  name: "AttemptQuiz",
  data(){
        return {
            user_id :  sessionStorage.getItem("user_id"),
            Name: sessionStorage.getItem("Name"),
            Category: sessionStorage.getItem("Category"),
            isJunior: true,
            password: sessionStorage.getItem("password"),
            assesment_id: sessionStorage.getItem("Assesment_id"),
            AssesmentName:'',
            asses:'',
            score_id:'',
            score:'',
            questions: [],
    correctValues:[],
    selectedAnswers: [],
        }
    },
    async created()
    {
        console.log(this.assesment_id);
        return fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/Assesment/${this.assesment_id}`, {
              method: "GET",
              headers: {
                "Content-Type": "application/json;charset=utf-8",
              },
            })
          .then((response) => response.json())
          .then((re_data) => {
            // console.log(re_data);
            this.asses=re_data;
            this.AssesmentName=this.asses[0]["Name"];
    
            let fullquiz=this.asses[0]["Quiz"];
            let newtemp=fullquiz.split("/");
            let first = newtemp.shift();
            let last = newtemp.pop();
            first= first.slice(2,first.length-16);
            let firstq=''
            firstq=first.split("?")[0].split(".")[1].slice(4).concat("?")
            console.log(firstq)
            let options =[]
            options=first.split("?")[1].split(".")
            console.log(options)
            console.log("OPTIONS ARE");
            let finalop=[];
            for(let i=1;i<5;i++)
            {
                let y=options[i].split(",")[0].slice(4)
                finalop.push(y.slice(0,y.length-1))
            }
            let correctop= options[5].split(",")[0].slice(2);
            correctop= correctop.slice(2,correctop.length-1);
            console.log(finalop);
            this.questions.push({"text":firstq,"options":finalop});
            console.log("Correct Option");
            console.log(correctop);
            this.correctValues.push(correctop);

            let A = [];
            console.log("Rest of the elements are");
            // console.log(newtemp);
            for (let i = 0; i < newtemp.length; i++) {
                let oq = newtemp[i].slice(5,newtemp[i].length-16);
                A.push(oq);
            }
            let dumy='';
            for(let i=0;i<A.length;i++)
            {
                
            dumy=A[i].split("?")[0].split(".")[1].slice(4).concat("?")
            console.log(dumy);
            options =[]
            options=A[i].split("?")[1].split(".")
            console.log(options)
            console.log("OPTIONS ARE");
            finalop=[];
            for(let i=1;i<5;i++)
            {
                let y=options[i].split(",")[0].slice(4)
                finalop.push(y.slice(0,y.length-1))
            }
            correctop= options[5].split(",")[0].slice(2);
            correctop= correctop.slice(2,correctop.length-1);
            console.log(finalop);
            this.questions.push({"text":dumy,"options":finalop});
            console.log("Correct Option");
            console.log(correctop);
            this.correctValues.push(correctop);
            }
            // console.log(A[0]);
            // console.log(A[1]);
            last=last.slice(5,last.length-19);
            let lastq=''
            lastq=last.split("?")[0].split(".")[1].slice(4).concat("?")
            console.log(lastq)

            options =[]
            options=last.split("?")[1].split(".")
            console.log(options)
            console.log("OPTIONS ARE");
            finalop=[];
            for(let i=1;i<5;i++)
            {
                let y=options[i].split(",")[0].slice(4)
                finalop.push(y.slice(0,y.length-1))
            }
            correctop= options[5].split(",")[0].slice(2);
            correctop= correctop.slice(2,correctop.length-1);
            console.log(finalop);
            this.questions.push({"text":lastq,"options":finalop});
            console.log("Correct Option");
            console.log(correctop);
            this.correctValues.push(correctop);
            // const arrayOfDictionaries = JSON.parse(this.asses[0]["Quiz"]);
            // console.log(arrayOfDictionaries);
            // console.log(fullquiz[0]);
            // console.log(fullquiz.length);
            // for (let i = 0; i < fullquiz.length; i++) {
            //     let optionlist=[]
            //     optionlist.push(fullquiz[i]["Option 1"]);
            //     optionlist.push(fullquiz[i]["Option 2"]);
            //     optionlist.push(fullquiz[i]["Option 3"]);
            //     optionlist.push(fullquiz[i]["Option 4"]);
            //     let question=fullquiz[i]["Question"];
            //     console.log(question);
            //     console.log(optionlist);
                // this.questions.push({"text":fullquiz["Question"],"options":optionlist});
                // this.correctValues.push(re_data[0]["Quiz"][i]["Correct Option"]); 
                // } 
    
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
    },
    async Summary(){
  
  this.$router.push("/Summary");    
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
    submit() {
      console.log('Selected Answers:', this.selectedAnswers);
      let B = this.selectedAnswers;
      let A = this.correctValues;
      let total = A.length
      let diff = A.filter(x => !B.includes(x));
      console.log("Set-Difference: " + diff);
      this.score = total- diff.length;
      this.score = (this.score/total)*100;
      this.score =parseInt(this.score);
      console.log("Score is");
      console.log(this.score);
      try {
        console.log("Inside Add Marks");
        fetch(`http://localhost:8000/api/${this.user_id}/${this.password}/${this.assesment_id}/CreateAspirant`, {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ aspirant_score: this.score , aspirant_name : this.Name }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            console.log(register_data);
              sessionStorage.removeItem("Assesment_id");
            this.$router.push("/Assesments");    
            
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
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