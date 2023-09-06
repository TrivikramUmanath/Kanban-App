<template>
  <div class="Login">
<input type="email" v-model="email" name="email" placeholder="Email" />
<br>
</br>
<!-- <p>Message is: {{ message }}</p> -->
<input type="password" name="password"  v-model="password" placeholder="Password" />
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
            first_name:'',
        }
    },
    methods : {
        login : function login() {
            
            let data = {
                "email": this.email,
                "password": this.password
            }
			// body...
      console.log("FIRST NAME");
			
			fetch(
				"http://localhost:8000/login",
				{
				method: "POST",
				body: JSON.stringify(data),
				headers:{
					"Content-Type":"application/json",
				},
				

				}
			).then(function(response) {
				return response.json()
			}).then(function(rdata) {
				localStorage.setItem("token", rdata["response"]["user"]["authentication_token"]);
        console.log("User id");
        console.log(rdata["response"]["user"]["id"]);
        let t= data["email"].split("@")[0]
        localStorage.setItem("First_Name",t);
        localStorage.setItem("id",rdata["response"]["user"]["id"]);
        sessionStorage.setItem("id",rdata["response"]["user"]["id"]); 
                  console.log(rdata["response"]["user"]["authentication_token"]);
  
			})
            this.$router.push('/Dashboard');
				

		}
    }

}
</script>
<!-- 
<script>
export default {
  name: "Login",
  props: {
    msg: String,
  },
  mounted() {
    fetch("http://127.0.0.1:8000/login?include_auth_token")
    .then(response => response.json())
    .then(data => {
      this.msg = data["msg"];
    });
  console.log(this.msg);
  }
};
</script> -->

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
