<template>
  <div style="width: 100%; display: flex; flex-direction: row">
    <div style="width: 200px; background-color: #eee" v-if="isSubmitted">
      <ul style="list-style: none; padding: 5px">
        <li><a class="menu-item" @click="selectedItem = 'all'">All Predictions</a></li>
        <li><a class="menu-item" @click="selectedItem = 'kmeans'">Kmeans Cluster</a></li>
        <li><a class="menu-item" @click="selectedItem = 'gensim'">Gensim Prediction</a></li>
        <li><a class="menu-item" @click="selectedItem = 'tf-idf'">TF-IDF Prediction</a></li>
      </ul>
    </div>
    <div style="padding: 0 4rem; max-width: 1440px; margin: 4rem auto; display: flex; align-items: stretch; justify-content: stretch;">
      <div v-if="!isSubmitted">
        <h1 style="text-align: center; margin-bottom: 4rem;">Dreams Degree Recommender</h1>
        <p>
          <strong>Task:</strong> Write about postive school experiences you had in terms of subjects.
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

      <div v-else style="display: flex; flex-direction: column; width: 100%; flex: 1">
        <div v-if="isLoading">
          Loading... Please wait.
        </div>
        <div v-else style="width: 1000px">
          <div v-if="selectedItem == 'kmeans' || selectedItem == 'gensim' || selectedItem == 'tf-idf'">
            <h2>We recommend you:</h2>
            <h1 style="color: blue; text-align: center;">{{ recommendation }}</h1>
            <img :src="`/images/${recommendation}.png`" style="width: 600px; height: auto; display: block; margin: auto">
          </div>

          <div style="border-top: solid 1px gray; border-bottom: solid 1px gray;">
            <div v-if="selectedItem == 'all'" style="width: 100%">
              <h2>Our recommendations are</h2>
              <div>
                <h3 class="link" @click="selectedItem = 'kmeans'">Kmeans Cluster</h3>
                <ol>
                  <li v-for="option in options" :key="option">{{ option }}</li>
                </ol>
              </div>
              <div style="border-top: dashed 2px #bbb;">
                <h3 class="link" @click="selectedItem = 'gensim'">Gensim Prediction</h3>
                <ol>
                  <li v-for="option in related" :key="option.program">{{ option.program }}</li>
                </ol>
              </div>
              <div style="border-top: dashed 2px #bbb;">
                <h3 class="link" @click="selectedItem = 'tf-idf'">TF-IDF Prediction</h3>
                <ol>
                  <li v-for="option in furkansList" :key="option[1]">{{ option[1] }}</li>
                </ol>
              </div>
            </div>
            <div v-if="selectedItem == 'gensim'">
              <h3 style="text-align: center">Top {{ barChartData.labels.length }}: Study Programs Based on Gensim Prediction:</h3>

              <bar-chart
                :chartdata="barChartData"
                :options="barOptions"
              />
            </div>
            <div v-if="selectedItem == 'kmeans'">
              <p>Here are your bachelor's degree options based on Kmeans Clustering</p>

              <select v-model="selectedDegree" size="5">
                <option v-for="(option, i) in options" :key="option" :value="option" @dblclick="openLink(option)">{{ i + 1 }}. {{ option }}</option>
              </select>

              <p>Click on degree to show hours info</p>
              <p>Double click on degree to show main courses</p>

              <h3 style="text-align: center">HOURS</h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
            </div>
            <div v-if="selectedItem == 'tf-idf'">
              <h3 style="text-align: center">Top {{ barChartData.labels.length }}: Study Programs Based on TF-IDF Prediction:</h3>

              <bar-chart
                :chartdata="barChart2Data"
                :options="barOptions"
              />
            </div>
          </div>
        </div>

        <p style="text-align: end;">
          <button style="border: solid 1px black; border-radius: 5px; margin-top: 2rem; padding: 0.5rem 2rem;" @click="reset">Reset</button>
        </p>
      </div>
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
      selectedItem: "all",
      isLoading: false,
      statement: "",
      allDegrees,
      selectedDegree: "",
      result: {
        field: "Computer Engineering"
      },
      related: [],
      options: [],
      furkansList: [],
      barChartData: null,
      barOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{ stacked: true }],
          xAxes: [{ stacked: true }]
        },
        onClick: (e) => {
          let x = e.target.getElementsAtEvent(e);
          console.log(x);
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
  computed: {
    recommendation() {
      if (this.selectedItem == "gensim") {
        return this.related.length === 0 ? "" : this.related[0].program;
      }
      if (this.selectedItem == "tf-idf") {
        return this.furkansList.length === 0 ? "" : this.furkansList[0][1];
      }
      return this.result.field;
    }
  },
  methods: {
    async submit() {
      if (this.statement == '') {
        alert("Statement must not be empty!");
        return;
      }

      this.isSubmitted = true;
      this.isLoading = true;

      const result = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ a: this.statement })
      });

      const prediction = await result.json();

      this.result.field = prediction.prediction;
      this.options = prediction.clusterList;

      this.related = prediction.gensimList;
      this.furkansList = prediction.furkansList;
      this.furkansList.reverse();

      this.barChartData = {
        labels: this.related.map(x => x.program),
        datasets: [
          {
            label: "Related keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.related.map(x => Math.round(x.similarity * 100))
          }
        ]
      };
      this.selectedDegree = this.options[0];

      this.barChart2Data = {
        labels: this.furkansList.map(x => x[1]),
        datasets: [
          {
            label: "Related keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.furkansList.map(x => Math.round(x[0]))
          }
        ]
      };

      this.isLoading = false;
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
<style>
.menu-item {
  display: block;
  background-color: #ddd;
  border-radius: 5px;
  margin: 5px;
  padding: 10px;
  cursor: pointer;
}
.menu-item:hover {
  background-color: #fff;
}
.link {
  color: blue;
  cursor: pointer;
}
</style>
