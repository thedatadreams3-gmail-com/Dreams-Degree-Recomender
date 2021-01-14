<template>
  <div style="padding: 0 4rem; max-width: 800px; margin: 4rem auto;">
    <div v-if="!isSubmitted">
      <h1 style="text-align: center; margin-bottom: 4rem;">Dreams Degree Recomender</h1>
      <p>
        <strong>Task:</strong> Write about postive scool experiences you had in terms of subjects.
      </p>

      <p>
        This can be an overall statement like "I enjoyed math" a more specific are like "Geometry and analysis were the most interesting topics".
      </p>

      <p>
        If you have any university or school related links like programming, java or HTML, Feel free to share them.
      </p>


      <p>
        <strong>Note:</strong> <span style="font-weight: bold; color: red;">Do not use any negative statments like "I don't/ didn't enjoy...." not tell about things you don't like!</span>
      </p>

      <p>
        <strong>Statement:</strong>
      </p>

      <textarea v-model="statement" rows="10" style="width: 100%;"></textarea>

      <p style="text-align: end;">
        <button style="border: solid 1px black; border-radius: 5px; margin-top: 2rem; padding: 0.5rem 2rem;" @click="submit">Submit</button>
      </p>
    </div>

    <div v-else>
      <h2>We recommend you:</h2>
      <h1 style="color: blue; text-align: center;">{{ result.field }}</h1>

      <p style="max-width: 400px; margin: 2rem auto;">{{ result.description }}</p>

      <div style="border-top: solid 1px gray; border-bottom: solid 1px gray; display: flex;">
        <div style="border-right: solid 1px gray; flex: 1; padding: 2rem 2rem 2rem 0rem;">
          <h3 style="text-align: center">Top {{ barChartData.labels.length }}: Study Programs</h3>

          <bar-chart
            :chartdata="barChartData"
            :options="barOptions"
          />
        </div>
        <div style="flex: 1; padding: 2rem 2rem 0rem 2rem;">
          <p>Here are your bachelor's degree options</p>

          <select v-model="selectedDegree" size="5">
            <option v-for="option, i in options" :value="option" @dblclick="openLink(option)">{{ i + 1 }}. {{ option }}</option>
          </select>

          <p>Click on degree to show hours info</p>
          <p>Double click on degree to show main courses</p>

          <h3 style="text-align: center">HOURS</h3>

          <pie-chart :chartdata="pieChartData" :options="pieOptions" />
        </div>
      </div>

      <p style="text-align: end;">
        <button style="border: solid 1px black; border-radius: 5px; margin-top: 2rem; padding: 0.5rem 2rem;" @click="reset">Reset</button>
      </p>
    </div>
  </div>
</template>

<script>
import BarChart from "./BarChart.vue";
import PieChart from "./PieChart.vue";
import degreesInfo from "../degrees_info.json";

export default {
  name: "App",
  components: {
    BarChart,
    PieChart,
  },
  data() {
    let allDegrees = {};
    for (let index in degreesInfo) {
      allDegrees[degreesInfo[index].study_program] = degreesInfo[index];
    }

    return {
      isSubmitted: false,
      statement: "",
      allDegrees,
      selectedDegree: "",
      result: {
        field: "Computer Engineering",
        description: "This can be an overall statement like \"I enjoyed math\" a more specific are like \"Geometry and analysis were the most interesting topics\"."
      },
      options: [],
      barChartData: null,
      barOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{ stacked: true }],
          xAxes: [{ stacked: true }]
        }
      },
      pieChartData: null,
      pieOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
    };
  },
  watch: {
    selectedDegree(degreeName) {
      const degreeInfo = this.allDegrees[degreeName];
      this.pieChartData = {
        labels: ["Lecture", "Exercise", "Practicum", "Seminar"],
        datasets: [
          {
            label: "HOURS",
            backgroundColor: ["#e59c2d", "#41B883", "#E46651", "#00D8FF"],
            data: [degreeInfo.lectures, degreeInfo.exercise, degreeInfo.practicum, degreeInfo.seminar]
          },
        ]
      };
    }
  },
  methods: {
    submit() {
      this.isSubmitted = true;
      this.options = ["B.Sc. Applied Cognitive and Media Science PO19 - B-KM-19", "B.Sc. Structural Engineering PO19 - B-SE-19", "B.Sc. Medical Engineering PO15 - B-MedT-15"];
      this.barChartData = {
        labels: ["Computer Engineering", "Applied Computer Science", "Mechanical Engineering", "Mechanical Engineering", "Mechanical Engineering"],
        datasets: [
          {
            label: "Related keywords",
            backgroundColor: "#70ad47",
            data: [8, 7, 5, 2, 1]
          }
        ]
      };
      this.selectedDegree = this.options[0];
    },
    reset() {
      this.isSubmitted = false;
      this.statement = "";
      this.result = {};
    },
    openLink(degreeName) {
      const degreeInfo = this.allDegrees[degreeName];
      window.open(degreeInfo.Link, "_blank");
    }
  }
};
</script>
