<template>
  <div class="Login">
<input type="email" v-model="email" name="email" placeholder="email" />
<br>
</br>
<input type="password" name="password"  v-model="password" placeholder="password" />
<br>
</br>
    <button @click=login>Login</button>
  </div>
</template>


<script>
export default {
    name: 'Login',
    data(){
        return {
            email: '',
            password: '',
            user_id:'',
            Name:'',
            Category:''
        }
    },
    methods : {
        login : function login() {
            
            let data = {
                "email": this.email,
                "password": this.password
            }
      console.log("FIRST NAME");
      return fetch(`http://localhost:8000/api/${this.email}/${this.password}/Login`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
        })
      .then((response) => response.json())
      .then((re_data) => {
        this.user_id = re_data["user_id"];
        this.Name=re_data["Name"];
        this.Category=re_data["Category"];
        console.log(re_data);
        sessionStorage.setItem("user_id",this.user_id);
        sessionStorage.setItem("Name",this.Name);
        sessionStorage.setItem("Category",this.Category);
        sessionStorage.setItem("password",this.password);
        sessionStorage.setItem("email",this.email);
        this.$router.push("/Dashboard"); 
      })
      .catch((error) => console.log(error));
    }
    }

}
</script>
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
