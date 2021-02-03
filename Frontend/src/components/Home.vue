<template>
  <div style="width: 100%; display: flex; flex-direction: row">
    <div style="width: 200px; background-color: #eee" v-if="isSubmitted">
      <ul style="list-style: none; padding: 5px">
        <li><a class="menu-item" @click="selectedItem = 'all'">All Predictions</a></li>
        <li><a class="menu-item" @click="selectedItem = 'kmeans'">SVM Prediction</a></li>
        <li><a class="menu-item" @click="selectedItem = 'gensim'">Gensim Prediction</a></li>
        <li><a class="menu-item" @click="selectedItem = 'tf-idf'">TF-IDF Prediction</a></li>
      </ul>
    </div>
    <div style="padding: 0 4rem; margin: 4rem auto; display: flex; align-items: stretch; justify-content: stretch;">
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
        <div v-else>
          <div v-if="selectedItem == 'kmeans' || selectedItem == 'gensim' || selectedItem == 'tf-idf'">
            <h2>We recommend you:</h2>
            <h1 style="color: blue; text-align: center;">{{ recommendation }}</h1>
            <table>
              <tr>
                <td>
                  <h2>TF IDF Word Cloud:</h2>
                  <img :src="`/images/tf-idf/${recommendation}.png`" style="width: 600px; height: auto; display: block; margin: auto" @click="showModal('tf-idf')">
                  <modal name="tf-idf" :width="1000" :height="500">
                    <img :src="`/images/tf-idf/${recommendation}.png`" style="width: 100%; transform: scale(1.2); height: auto" @click="$modal.hide('tf-idf')">
                  </modal>
                </td>
                <td>
                  <h2>Count Word Cloud:</h2>
                  <img :src="`/images/count/${recommendation}.png`" style="width: 600px; height: auto; display: block; margin: auto" @click="showModal('count')">
                  <modal name="count" :width="1000" :height="500">
                    <img :src="`/images/count/${recommendation}.png`" style="width: 100%; transform: scale(1.2); height: auto" @click="$modal.hide('count')">
                  </modal>
                </td>
              </tr>
            </table>                
            
          </div>

          <div style="border-top: solid 1px gray; border-bottom: solid 1px gray;">
            <div v-if="selectedItem == 'all'" style="width: 100%">
              <h2>Our recommendations are</h2>
              <div>
                <h3 class="link" @click="selectedItem = 'kmeans'">SVM Prediction</h3>
                <p style="font-weight: 700; font-size: 1.1em">{{ result.field }}</p>
              </div>
              <div style="border-top: dashed 2px #bbb;">
                <h3 class="link" @click="selectedItem = 'gensim'">Gensim Prediction</h3>
                <ol>
                  <li style="font-weight: 700; font-size: 1.1em" v-if="related.length > 0">{{ related[0].program }}</li>
                  <li style="font-size: 1.1em" v-if="related.length > 1">{{ related[1].program }}</li>
                  <li v-if="related.length > 2">{{ related[2].program }}</li>
                </ol>
              </div>
              <div style="border-top: dashed 2px #bbb;">
                <h3 class="link" @click="selectedItem = 'tf-idf'">TF-IDF Prediction</h3>
                <ol>
                  <li style="font-weight: 700; font-size: 1.1em" v-if="furkansList.length > 0">{{ furkansList[0][1] }}</li>
                  <li style="font-size: 1.1em" v-if="furkansList.length > 1">{{ furkansList[1][1] }}</li>
                  <li v-if="furkansList.length > 2">{{ furkansList[2][1] }}</li>
                </ol>
              </div>
            </div>
            <div v-if="selectedItem == 'gensim'">
              <div style="display: flex; margin: 1rem; justify-content: center; grid-gap: 1rem;">
                <button :class="`radio ${selectedCount == 5 ? 'active' : ''}`" @click="selectedCount = 5">Top 5</button>
                <button :class="`radio ${selectedCount == 10 ? 'active' : ''}`" @click="selectedCount = 10">Top 10</button>
              </div>

              <h3 style="text-align: center">Top {{ Math.min(selectedCount, barChartData.labels.length) }}: Study Programs Based on Gensim Prediction:</h3>

              <bar-chart
                :chartdata="barChartData"
                :options="barOptions"
              />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto;"></div>

              <h3 style="text-align: center">Top {{ Math.min(selectedCount, barChart3Data.labels.length) }}: Study Courses Based on Gensim Prediction:</h3>

              <bar-chart
                :chartdata="barChart3Data"
                :options="barOptions"
              />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto;"></div>

              <h2>Gensim Hours</h2>

              <select v-model="selectedDegree" size="5">
                <option v-for="(option, i) in this.related" :key="option.program" :value="option.program" @dblclick="openLink(option.program)">{{ i + 1 }}. {{ option.program }}</option>
              </select>

              <p>Click on degree to show hours info</p>
              <p>Double click on degree to show main courses</p>

              <h3 style="text-align: center">HOURS</h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
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
              <div style="display: flex; margin: 1rem; justify-content: center; grid-gap: 1rem;">
                <button :class="`radio ${selectedCount == 5 ? 'active' : ''}`" @click="selectedCount = 5">Top 5</button>
                <button :class="`radio ${selectedCount == 10 ? 'active' : ''}`" @click="selectedCount = 10">Top 10</button>
              </div>

              <h3 style="text-align: center">Top {{ Math.min(selectedCount, barChart2Data.labels.length) }}: Study Programs Based on TF-IDF Prediction:</h3>

              <bar-chart
                :chartdata="barChart2Data"
                :options="barOptions"
              />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto;"></div>

              <h2>TF-IDF Hours</h2>

              <select v-model="selectedDegree" size="5">
                <option v-for="(option, i) in this.furkansList" :key="option[1]" :value="option[1]" @dblclick="openLink(option[1])">{{ i + 1 }}. {{ option[1] }}</option>
              </select>

              <p>Click on degree to show hours info</p>
              <p>Double click on degree to show main courses</p>

              <h3 style="text-align: center">HOURS</h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
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
      tfIdfPopped: false,
      countPopped: false,
      selectedCount: 10,
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
    },
    barChartData() {
      return {
        labels: this.related.slice(0, this.selectedCount).map(x => x.program),
        datasets: [
          {
            label: "Related keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.related.slice(0, this.selectedCount).map(x => (parseFloat(x.similarity) * 100).toFixed(2))
          }
        ]
      };
    },
    barChart2Data() {
      return {
        labels: this.furkansList.slice(0, this.selectedCount).map(x => x[1]),
        datasets: [
          {
            label: "TF-IDF Similarity",
            backgroundColor: "#70ad47",
            data: this.furkansList.slice(0, this.selectedCount).map(x => parseFloat(x[0]).toFixed(2))
          }
        ]
      };
    },
    barChart3Data() {
      return {
        labels: this.gensimCourse.slice(0, this.selectedCount).map(x => `${x.studyProgram.slice(0, x.studyProgram.indexOf('  PO'))} - ${x.courses}`),
        datasets: [
          {
            label: "Related keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.gensimCourse.slice(0, this.selectedCount).map(x => (parseFloat(x.similarity) * 100).toFixed(2))
          }
        ]
      };
    },
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
      this.gensimCourse = prediction.gensimCourse;
      this.furkansList.reverse();
      this.selectedDegree = this.options[0];

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
    },
    showModal(name) {
      this.$modal.show(name);
    },
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
.popup {
  transform-origin: center;
  transform: scale(1);
  transition: transform 0.5s ease-in-out;
}
.popup.popped {
  transform: scale(1.5);
}
.radio {
  border: solid 1px #999;
  border-radius: 10px;
  background-color: #eee;
  padding: 0.5rem 1rem;
  font-size: 1.1rem;
}
.radio.active {
  background-color: #333;
  color: white;
}
</style>
