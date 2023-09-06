import Vue from "vue";
import VueRouter from "vue-router";
import LoginViewVue from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import DashboardView from "../views/DashboardView.vue";
import AddListView from "../views/AddListView.vue";
import EditListView from "../views/EditListView.vue";
import DeleteListView from "../views/DeleteListView.vue";
import AddCardView from "../views/AddCardView.vue";
import DeleteCardView from "../views/DeleteCardView.vue";
import EditCardView from "../views/EditCardView.vue";
import SummaryView from "../views/SummaryView.vue"; 
import HelloWorldView from "../views/HelloWorldView.vue"; 

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Login",
    component: LoginViewVue,
  },
  {
    path: "/Register",
    name: "Register",
    component:RegisterView,
  },
  {
    path:"/Dashboard",
    name: "Dashboard",
    component:DashboardView,

  },
  {
    path:"/Dashboard/AddList",
    name: "AddList",
    component:AddListView,

  },
  {
    path:"/Dashboard/Edit List",
    name: "EditList",
    component:EditListView ,

  },
  {
    path:"/Dashboard/Delete List",
    name: "DeleteList",
    component:DeleteListView ,
  },
  {
    path:"/Dashboard/Add Card",
    name: "AddCard",
    component:AddCardView ,
  },
  {
    path:"/Dashboard/Delete Card",
    name: "DeleteCard",
    component:DeleteCardView ,
  },
  {
    path:"/Dashboard/Edit Card",
    name: "EditCard",
    component:EditCardView ,
  },
  {
    path:"/Summary",
    name: "Summary",
    component:SummaryView ,
  },
  {
    path:"/Dashboard/Check",
    name: "Check",
    component:HelloWorldView,
  }

];

const router = new VueRouter({
  routes,
});

export default router;
