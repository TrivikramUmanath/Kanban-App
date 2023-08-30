

<template>
    <div class="body">
      <div class="box">
        <nav>
      
      <router-link to="/">Login</router-link> |
      <router-link to="/Register">Register</router-link>
    </nav>
          <form @submit.prevent="register">

            <label for="Name">Name </label>
            <input type="Name" name="Name" v-model="Name" required>

            <br>
            </br>
            <br>
           </br>


            <label for="email">Email </label>
            <input type="email" name="email" v-model="email" required>

            <br>
            </br>
            <br>
           </br>
            <label for="password">Password </label>
            <input type="password" name="password" v-model="password" required>

            <br>
            </br>
            <br>
           </br>
           <label for="Category">Category </label>
       <select required name="category" id="category" v-model="Category">
      <option value="Junior">Junior</option>
      <option value="Senior">Senior</option>
      <option value="POD">POD</option>
    </select>
  <br>
            </br>
            <br>
           </br>
           <br>
            </br>
            <br>
           </br>
            <center>
                <button type="submit">Register</button>
            </center>
            
          </form>


      </div>
  </div>
</template>

<script>

export default {
  name: "UserRegister",
  data() {
    return {
      email: "",
      password: "",
      Name:"",
      Category:"",
    };
  },
  methods: {
    async register() {
      try {
        console.log("Inside REG");
        fetch("http://localhost:8000/api/user/CreateUser", {
          method: "POST",
          headers: {
            'Access-Control-Allow-Origin': '*',
       'Content-type': 'application/json',
          },
          body: JSON.stringify({ Name: this.Name, password: this.password, Category: this.Category, email: this.email }),
        })
          .then((resp) => {
            return resp.json();
          })
          .then(async (register_data) => {
            this.$router.push('/');
          })
          .catch((error) => {
            console.log(error);
          });
      } catch (error) {
        console.log("Unsuccessful Save ", error);
      }
}
},
};
</script>


<style scoped></style>