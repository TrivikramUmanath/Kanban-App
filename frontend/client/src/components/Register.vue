

<template>
  <div class="body">
    <div class="box">
        <form @submit.prevent="register">

          <label for="email">Email</label>
          <input type="email" name="email" v-model="email" required>

          <br>
          </br>
          <br>
         </br>

          <label for="password">Password</label>
          <input type="password" name="password" v-model="password" required>

          <br>
          </br>
          <br>
         </br>

         <label for="Name">Name</label>
          <input type="Name" name="Name" v-model="Name" required>

          <br>
          </br>
          <br>
         </br>

         <label for="Category">Category</label>
          <input type="Category" name="Category" v-model="Category" required>

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
    Name:"",
    email: "",
    password: "",
    Category:"",

  };
},
methods: {
  async register() {
    try {
      fetch("http://127.0.0.1:8000/api/user/CreateUser", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({ email: this.email, password: this.password }),
      })
        .then((resp) => {
          return resp.json();
        })
        .then(async (register_data) => {
          const { response } = register_data;
          if (response.errors) {
            const { email, password } = response.errors;
            console.log({ email, password });
            // this.error_email = email ? email[0] : "";
            // this.error_password = password ? password[0] : "";
            // console.log(this.error_email, this.error_password);
          } else {
            this.$router.push("/");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    } catch (error) {
      console.log("Registration unsuccessful: ", error);
    }
  },
},
};
</script>


<style scoped></style>