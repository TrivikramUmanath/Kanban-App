<template>
    <div>
      <bar-chart :chart-data="chartData" :options="chartOptions"></bar-chart>
    </div>
  </template>
  
  <script>
  import { Bar, mixins } from 'vue-chartjs';
  
  export default {
    extends: Bar,
    mixins: [mixins.reactiveProp],
    props: ['chartData', 'options'],
    mounted() {
      this.renderChart(this.chartData, this.options);
    }
  };
  </script>
  