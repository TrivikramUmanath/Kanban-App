

<template>
    <div class="body">
      <div class="box">
        <nav>
      
      <router-link to="/">Login</router-link> |
      <router-link to="/Register">Register</router-link>
    </nav>
          <form @submit.prevent="register">

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
    };
  },
  methods: {
    async register() {
      try {
        fetch("http://127.0.0.1:8000/register", {
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