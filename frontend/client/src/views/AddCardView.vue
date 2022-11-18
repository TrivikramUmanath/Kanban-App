

<template>
    <div class="body">
      <div class="box">
        <center>
          <form @submit.prevent="AddCard">
  
            <label for="List">List</label>
            <br>
            </br>
  
            <!-- <input type="message" name="List_Name" v-model="ListName" required> -->
            <!-- <select class="form-control" id="format" v-on:change="changeRoute($event)"> 
                                  <option selected >  {{ list.Name }}  </option> 
                                  <option>Edit List</option> 
                                  <option >Delete List</option> 
                                </select> -->

                                <!-- <select id="categories" v-model="ListNamePair" v-on:change="ChangeCard($event)">
  <option v-for="item in ListNamePair"  v-if="value==LST_id" selected :value="item.name">{{ item.id }}</option>
</select> -->
<select  id="categories" v-on:change="ChangeCard($event)">
       <option v-for="(item , value) in List_Names" v-bind:key="index" :selected= "item == namew" >
            {{item}}
       </option>
</select>

            <br>
            </br>
  
            <label for="Title">Title</label>
            <br>
        </br>
        <input type="message" name="Title" v-model="Title" required>
        <br>
            </br>
        <label for="Content">Content</label>
            <br>
        </br>
        <input type="message" name="Content" v-model="Content" required>
            <br>
            </br>
            <br>
           </br>
           <!-- <label for="date">Deadline</label>
           <date-pick
        v-model="date"
        :displayFormat="'DD.MM.YYYY'"
    ></date-pick> -->
               <label for="Deadline">Deadline</label>
           <br></br>
           <input type="date" name="Deadline"   v-model="date" required>
           <br></br>
<br>
</br>
<br>
</br>
    <input type="checkbox" id="checkbox" v-model="checked"   true-value="Completed"
  false-value="Incomplete" />
<label for="checkbox">{{ checked }}</label>
<br>
</br>
<br>
</br>        
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
  name: "AddCard",
  data() {
    return {
    date: '',
    checked:"Incomplete",
    List_Names:[],
    Name_List:[],
    description :"",
    List:null,
    List_Id:sessionStorage.getItem("Lists_Id"),
    AllLists:{},
    ListNamePair:[],
    NameListPair:{},
    LST_id:'',
    namew:sessionStorage.getItem("List_Name"),
    id : sessionStorage.getItem("id"),
    token : localStorage.getItem("token")
    };
  },
  async created(){

    // this.List_Id = sessionStorage.getItem("Lists_Id");
    // this.List_Name = 
    const e= JSON.parse(sessionStorage.getItem("All Lists"));
    console.log("ADD CARD");
    console.log(e);
    this.AllLists = e;
    for (const [key, value] of Object.entries(e)) {
     this.List_Names.push(key);
     console.log("KEY");
     console.log(key);
     console.log("Value");
     console.log(value);
     console.log("LST ID");
     this.LST_id=this.AllLists[this.namew];
     console.log(this.LST_id);
    //  if( Number(value)-Number(this.LST_Id)==0)
    //  {
    //   console.log("Found");
    //   console.log(this.LST_id);
    //   this.namew=key;
    //  }
    //  console.log("KEY");
    //  console.log(key);
    //  console.log("Value");
    //  console.log(value);
     this.ListNamePair.push({"id":key,"name":value});
    //  this.NameListPair.push({value:key});
    //  console.log(this.ListNamePair[0]);
}
console.log("LIST NAME PAIR");
console.log(this,this.ListNamePair);
// this.LST_id = this.id;
    
  },
  methods: {
    async AddCard() {
      console.log(this.LST_id);
      try {
        fetch(`http://localhost:8000/api/${this.id}/${this.LST_id}/AddCard`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
            "Authentication-Token": `${this.token}`,
          },
          body: JSON.stringify({ Title: this.Title, Content: this.Content, Deadline:this.date, Status:this.checked }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            this.$router.push('/Dashboard');
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
    },

    async ChangeCard(e){
      console.log("Changing Card");
      // console.log(r);
      console.log(this.LST_id);
      const r= e.target.options[e.target.options.selectedIndex].text;
      this.namew = r;
      console.log("ALL LISTS")
      console.log(this.AllLists);
      console.log(this.AllLists[String(this.namew)]);
      this.LST_id = this.AllLists[String(this.namew)];
      console.log(r);
      console.log(this.LST_id);
      // console.log(e.target["firstElementChild"]["firstChild"]["data"]);
      // this.LST_id=e.target.value;
      // sessionStorage.setItem("List Name",e.target["firstElementChild"]["firstChild"]["data"]);
      // sessionStorage.setItem("List Name",e.target["firstElementChild"]["firstChild"]["data"]);
    }
},
};
</script>

  
  
  <style scoped></style>