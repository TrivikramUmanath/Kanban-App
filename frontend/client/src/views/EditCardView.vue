      

<template>
    <div class="body">
      <router-link to="/Dashboard">Dashboard </router-link> 
      <br>
      </br>
      <br>
    </br>
      <div class="box">
        <center>
          <form @submit.prevent="EditCard">

<label for="Lists">Move to another List:    </label>

            <select  id="categories" name="Lists" v-on:change="MoveCard($event)">
       <option v-for="(item , value) in List_Names" v-bind:key="index" >
            {{item}}
       </option>
</select>
<br>
</br>
            <label for="Title">Title</label>
            <br></br>
            <input type="message" name="Title"   v-model="Title" required>
            <!-- <p> {{ Title }}   </p> -->
            <br> 
            </br>
            <label for="Content">Content</label>
            <br></br>
            <input type="message" name="Content"   v-model="Content" required>
  <!-- <p> {{ Content }}  </p> -->
            <br>
           </br>
           <!-- <label for="Deadline">Deadline</label>
           <br></br>
           <input type="date" name="Deadline"   v-model="Deadline" required>
           <br></br> -->
           <label for="Deadline">Deadline</label>
           <br></br>
           <input type="date" name="Deadline"   v-model="Deadline" required>
           <br></br>
           <!-- <label for="date">Date</label> -->
           <!-- {{ date }} -->
           <!-- <date-pick
        v-model="date"
        :displayFormat="'DD.MM.YYYY'"
    ></date-pick> -->
  <!-- <p> {{ Deadline }}  </p> -->
  <br>
</br>
<label for="Status">Status</label>
<br></br>
<!-- <input type="checkbox" name="Status"   v-model="Status" required true-value="Completed"
  false-value="Incomplete" />> -->
  <label for="checkbox">{{ Status }}</label>
  <input type="checkbox" id="Status" v-model="Status"   true-value="Completed"
  false-value="Incomplete" />

  <br></br>
        
                <button type="submit">Save</button>
        
            
          </form>
        </center>
  
      </div>
  </div>
  </template>
  
  <script>
    import DatePick from 'vue-date-pick';
  export default {
    components: {DatePick},
  name: "EditCard",
  data() {
    return {
    Title :sessionStorage.getItem("Card_Name"),
    Content :"",
    Status: "",
    date:'',
    Deadline: "",
    id : sessionStorage.getItem("id"),
    card_id : null,
    token : localStorage.getItem("token"),
    card:null,
    Lst_id:'',
    List_Names:["Static"],
    namew:'',
    allLists:JSON.parse(sessionStorage.getItem("All Lists")),
    final_name:'',
    };
  },
  async created() {
    return fetch(`http://localhost:8000/api/${this.id}/${this.Title}/getCard`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
        })
      .then((response) => response.json())
      .then((re_data) => {

        this.card = re_data;
        this.Lst_id = re_data["List_Id"];
        this.card_id = re_data["Card_Id"];
        this.Title = re_data["Title"];
        this.Content = re_data["Content"];
        this.Status = re_data["Status"];
        this.Deadline = re_data["Deadline"];
        console.log("ALL");
    
        console.log(this.Lst_id);
        for (let [key, value] of Object.entries(this.allLists)) {
          console.log(key, value);
          if (Number(value) == Number(this.Lst_id))
          {
            console.log("FOUND");
            this.namew=key;
            // this.this.final_name = key;
          }
          else{
            this.List_Names.push(key);
          }
  
}
      })
      .catch((error) => console.log(this.Title));
    },
    methods: {
    async EditCard() {
      if(this.final_name!="Static")
      {
        this.Lst_id = this.allLists[this.final_name];
        console.log("CHANGED LIST");
        console.log(this.final_name);
        console.log(this.Lst_id);
      }
      try {
        fetch(`http://localhost:8000/api/${this.id}/${this.card_id}/EditCard`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
          body: JSON.stringify({ Title: this.Title, Deadline: this.Deadline, Status:this.Status, Content:this.Content, List_Id:this.Lst_id }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            sessionStorage.removeItem("Card_Name")
            this.$router.push('/Dashboard');
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
    },
    async MoveCard(e){
    console.log("NEW LIST");
    // console.log(e.target["firstElementChild"]["firstChild"]["data"]);
    console.log(e.target.value);
    // sessionStorage.setItem("Card_Name",e.target["firstElementChild"]["firstChild"]["data"]);
      
      if(e.target.value!="Static")
      {
        this.final_name = e.target.value;
      }
    // this.$router.push("/Dashboard/Add Card");
  },
},
};
</script>

  
  
  <style scoped></style>