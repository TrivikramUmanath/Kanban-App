<template>
  <div class="Login">
    <nav>
      
      <router-link to="/">Login</router-link> |
      <router-link to="/Register">Register</router-link>
    </nav>
    <h1>Placement Portal</h1>
    <img alt="Vue logo" src="../assets/Placement_Logo.jpg" />
    <Login msg="Kanban App" />
  </div>
  
</template>

<script>
// @ is an alias to /src
import Login from "@/components/Login.vue";

export default {
  name: "LoginView",
  components: {
    Login,
  },
};
</script>
