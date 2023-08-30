import Vue from "vue";
import VueRouter from "vue-router";
import LoginViewVue from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import DashboardView from "../views/DashboardView.vue";
import SummaryView from "../views/SummaryView.vue"; 
import MyAccountView from "../views/MyAccountView.vue";
import ThreadDetailsView from "../views/ThreadDetailsView.vue";
import AddThreaView from "../views/AddThreadView.vue";
import MyThreadsView from "../views/MyThreadsView.vue";
import MessageRecordsView from "../views/MessageRecordsView.vue";
import MyAssesmentsView from "../views/MyAssesmentsView.vue";
import AssesmentsView from "../views/AssesmentsView.vue";
import AttemptQuizView from "../views/AttemptQuizView.vue";
import ScoreStatsView from "../views/ScoreStatsView.vue";
import ViewScoreView from "../views/ViewScoreView.vue";

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
  ,

  {
    path:"/MyAccounts/MessageRecords",
    name: "MesssageRecords",
    component:MessageRecordsView ,

  },
  
  {
    path:"/Summary",
    name: "Summary",
    component:SummaryView ,
  },
  {
    path:"/MyAccount",
    name: "MyAccount",
    component:MyAccountView ,
  },
  {
    path:"/MyThreads",
    name: "MyThreads",
    component:MyThreadsView ,
  },
  {
    path:"/Dashboard/ThreadDetails",
    name: "ThreadDetails",
    component:ThreadDetailsView ,
  },
  {
    path:"/Dashboard/AddThread",
    name: "AddThread",
    component:AddThreaView ,
  }
  ,
  {
    path:"/MyAssesments",
    name: "MyAssesments",
    component:MyAssesmentsView,
  },
  
  {
    path:"/Assesments",
    name: "Assesments",
    component:AssesmentsView,
  },
  {
    path:"/Assesment/AttemptQuiz",
    name: "AttemptQuiz",
     component: AttemptQuizView,
  },
  {
    path:"/Assesment/ViewScoreStats",
    name: "ViewScoreStats",
     component: ScoreStatsView,
  },
  {
    path:"/Assesment/CheckAllScores",
    name: "CheckAllScores",
     component: ViewScoreView,
     
  }


];

const router = new VueRouter({
  routes,
});

export default router;
