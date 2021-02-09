<template>
  <div style="">
    <div style="margin: 49px 272px 56px 212px" v-if="isSubmitted">
      <ul style="list-style: none; padding: 5px; text-align: center">
        <li>
          <a class="menu-item" @click="selectedItem = 'all'">All Predictions</a>
        </li>
        <li>
          <a class="menu-item" @click="selectedItem = 'gensim'"
            >Gensim Prediction</a
          >
        </li>
        <li>
          <a class="menu-item" @click="selectedItem = 'kmeans'"
            >SVM Prediction</a
          >
        </li>
        <li>
          <a class="menu-item" @click="selectedItem = 'tf-idf'"
            >TF-IDF Prediction</a
          >
        </li>
      </ul>
    </div>
    <div
      style="
        padding: 0 4rem;
        margin: 4rem auto;
        display: flex;
        align-items: stretch;
        justify-content: stretch;
      "
    >
      <div v-if="!isSubmitted">
        <h1 class="headingTitle">Dreams Degree Recommender</h1>
        <h2 class="task">
          <strong>Task:</strong> Write about postive school experiences you had
          in terms of subjects.
        </h2>

        <h3 class="taskExplain">
          This can be an overall statement like
          <strong class="stateMent">"I enjoyed math" </strong> more specific are
          like
          <strong class="stateMent"
            >"Geometry and analysis were the most interesting topics"</strong
          >.
        </h3>

        <h4 class="taskExplainUni">
          If you have any university or school related links like
          <strong class="stateMent">programming, java or HTML</strong>, Feel
          free to share them.
        </h4>

        <h5>
          <strong class="notes">Note:</strong>
          <span class="note"
            > Do not use any negative statments like "I don't/ didn't enjoy...."
            not tell about things you don't like!</span
          >
        </h5>

        <p class="stateMent">
          <strong>What do you like to learn? What is your interest?</strong>
        </p>

        <textarea v-model="statement" rows="10" class="inputText"></textarea>

        <p style="text-align: center">
          <button class="submitButn" @click="submit">Submit</button>
        </p>
      </div>

      <div
        v-else
        style="display: flex; flex-direction: column; width: 100%; flex: 1"
      >
        <div v-if="isLoading">Loading... Please wait.</div>
        <div v-else>
          <div
            v-if="
              selectedItem == 'kmeans' ||
              selectedItem == 'gensim' ||
              selectedItem == 'tf-idf'
            "
          >
            <div v-if="selectedItem == 'kmeans'">
              <h1 style="color: #003b7a;">SVM Prediction:</h1>
            </div>
            <div v-if="selectedItem == 'gensim'">
              <h1 style="color: #003b7a;">Gensim Prediction:</h1>
            </div>
            <div v-if="selectedItem == 'tf-idf'">
              <h1 style="color: #003b7a;">TF-IDF Prediction:</h1>
            </div>
            <h2 style="color: #003b7a;">We recommend you:</h2>
            <h1 style="color: blue; text-align: center">
              {{ recommendation }}
            </h1>
            <table>
              <tr>
                <td>
                  <h2 style="color: #003b7a;">TF IDF Word Cloud:</h2>
                  <img
                    :src="`/images/tf-idf/${recommendation}.png`"
                    style="
                      width: 600px;
                      height: auto;
                      display: block;
                      margin: auto;
                    "
                    @click="showModal('tf-idf')"
                  />
                  <modal name="tf-idf" :width="1000" :height="500">
                    <img
                      :src="`/images/tf-idf/${recommendation}.png`"
                      style="width: 100%; transform: scale(1.2); height: auto"
                      @click="$modal.hide('tf-idf')"
                    />
                  </modal>
                </td>
                <td>
                  <h2 style="color: #003b7a;">Count Word Cloud:</h2>
                  <img
                    :src="`/images/count/${recommendation}.png`"
                    style="
                      width: 600px;
                      height: auto;
                      display: block;
                      margin: auto;
                    "
                    @click="showModal('count')"
                  />
                  <modal name="count" :width="1000" :height="500">
                    <img
                      :src="`/images/count/${recommendation}.png`"
                      style="width: 100%; transform: scale(1.2); height: auto"
                      @click="$modal.hide('count')"
                    />
                  </modal>
                </td>
              </tr>
            </table>
          </div>
          <div
            style="border-top: solid 1px gray; border-bottom: solid 1px gray"
          >
            <div
              v-if="selectedItem == 'all'"
              style="width: 100%; text-align: center"
            >
              <h1 style="color: #003b7a">Our recommendations are</h1>
              <h2 style="color: #003b7a">Semantics Predictions:</h2>
              <div>
                <h3 class="link" @click="selectedItem = 'gensim'">
                  Gensim Prediction
                </h3>
                <ol>
                  <li
                    style="
                      <!-- margin-left: 215px; -->
                      <!-- margin-right: 257px; -->
                      font-weight: 700;
                      font-size: 1.1em;
                      color: #003b7a;
                    "
                    v-if="related.length > 0"
                  >
                    {{ related[0].program }}
                  </li>
                  <li
                    style="
                      <!-- margin-left: 213px; -->
                      <!-- margin-right: 86px; -->
                      text-align: center;
                      font-size: 1.1em;
                      color: #003b7a;
                    "
                    v-if="related.length > 1"
                  >
                    {{ related[1].program }}
                  </li>
                  <li
                    style="
                      <!-- margin-left: 212px; -->
                      <!-- margin-right: 120px; -->
                      text-align: center;
                      color: #003b7a;
                    "
                    v-if="related.length > 2"
                  >
                    {{ related[2].program }}
                  </li>
                </ol>
              </div>
              <div style="border-top: solid 1px gray">
                <h2 style="color: #003b7a">Non-Semantics Predictions:</h2>
                <h3 class="link" @click="selectedItem = 'kmeans'">
                  SVM Prediction
                </h3>
                <p style="font-weight: 700; font-size: 1.1em; color: #003b7a">
                  {{ result.field }}
                </p>
              </div>
              <div style="border-top: dashed 2px #bbb">
                <h3 class="link" @click="selectedItem = 'tf-idf'">
                  TF-IDF Prediction
                </h3>
                <ol>
                  <li
                    style="
                      <!-- margin-left: 215px; -->
                      <!-- margin-right: 257px; -->
                      font-weight: 700;
                      font-size: 1.1em;
                      color: #003b7a;
                    "
                    v-if="furkansList.length > 0"
                  >
                    {{ furkansList[0][1] }}
                  </li>
                  <li
                    style="
                      <!-- margin-left: 213px; -->
                      <!-- margin-right: 64px; -->
                      font-size: 1.1em;
                      color: #003b7a;
                    "
                    v-if="furkansList.length > 1"
                  >
                    {{ furkansList[1][1] }}
                  </li>
                  <li
                    style="
                      <!-- margin-left: 212px; -->
                      <!-- margin-right: 134px; -->
                      color: #003b7a;
                    "
                    v-if="furkansList.length > 2"
                  >
                    {{ furkansList[2][1] }}
                  </li>
                </ol>
              </div>
            </div>
            <div v-if="selectedItem == 'gensim'">
              <div
                style="
                  display: flex;
                  margin: 1rem;
                  justify-content: center;
                  grid-gap: 1rem;
                "
              >
                <button
                  :class="`radio ${selectedCount == 5 ? 'active' : ''}`"
                  @click="selectedCount = 5"
                >
                  Top 5
                </button>
                <button
                  :class="`radio ${selectedCount == 10 ? 'active' : ''}`"
                  @click="selectedCount = 10"
                >
                  Top 10
                </button>
              </div>

              <h3 style="text-align: center; color: #003b7a;">
                Top {{ Math.min(selectedCount, barChartData.labels.length) }}:
                Study Programs Based on Gensim Prediction:
              </h3>

              <bar-chart :chartdata="barChartData" :options="barOptions" />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto"></div>

              <div
                style="
                  display: flex;
                  margin: 1rem;
                  justify-content: center;
                  grid-gap: 1rem;
                "
              >
                <button
                  :class="`radio ${selectedCount2 == 5 ? 'active' : ''}`"
                  @click="selectedCount2 = 5"
                >
                  Top 5
                </button>
                <button
                  :class="`radio ${selectedCount2 == 10 ? 'active' : ''}`"
                  @click="selectedCount2 = 10"
                >
                  Top {{ gensimCourse.length }}
                </button>
              </div>
              <h3 style="text-align: center; color: #003b7a;">
                Top {{ Math.min(selectedCount, barChart3Data.labels.length) }}:
                Study Courses Based on Gensim Prediction:
              </h3>

              <bar-chart :chartdata="barChart3Data" :options="barOptions" />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto"></div>

              <h2 style="color: #003b7a; font-size: 25px; text-align: center">
                List of Gensim Recommended Degrees
              </h2>

              <select v-model="selectedDegree" size="5" class="selectionDegree">
                <option
                  v-for="(option, i) in this.related"
                  :key="option.program"
                  :value="option.program"
                  @dblclick="openLink(option.program)"
                >
                  {{ i + 1 }}. {{ option.program }}
                </option>
              </select>

              <p style="color: #003b7a; font-size: 25px">
                Click on degree to show hours info
              </p>
              <p style="color: #003b7a; font-size: 25px">
                Double click on degree to show main courses
              </p>

              <h3 style="text-align: center; color: #003b7a; font-size: 25px">
                HOURS
              </h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
            </div>
            <div v-if="selectedItem == 'kmeans'">
              <p style="text-align: center; color: #003b7a;font-size: 25px">
                Here are your bachelor's degree options based on Kmeans
                Clustering
              </p>

              <select v-model="selectedDegree" size="5" class="selectionDegree">
                <option
                  v-for="(option, i) in options"
                  :key="option"
                  :value="option"
                  @dblclick="openLink(option)"
                >
                  {{ i + 1 }}. {{ option }}
                </option>
              </select>

              <p style="color: #003b7a; font-size: 25px">
                Click on degree to show hours info
              </p>
              <p style="color: #003b7a; font-size: 25px">
                Double click on degree to show main courses
              </p>

              <h3 style="text-align: center; color: #003b7a; font-size: 25px">
                HOURS
              </h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
            </div>
            <div v-if="selectedItem == 'tf-idf'">
              <div
                style="
                  display: flex;
                  margin: 1rem;
                  justify-content: center;
                  grid-gap: 1rem;
                "
              >
                <button
                  :class="`radio ${selectedCount == 5 ? 'active' : ''}`"
                  @click="selectedCount = 5"
                >
                  Top 5
                </button>
                <button
                  :class="`radio ${selectedCount == 10 ? 'active' : ''}`"
                  @click="selectedCount = 10"
                >
                  Top 10
                </button>
              </div>

              <h3 style="text-align: center; color: #003b7a; font-size: 1.5rem">
                Top {{ Math.min(selectedCount, barChart2Data.labels.length) }}:
                Study Programs Based on TF-IDF Prediction:
              </h3>

              <bar-chart :chartdata="barChart2Data" :options="barOptions" />

              <div style="border-top: dashed 2px #bbb; margin: 2rem auto"></div>

              <h2 style="color: #003b7a; font-size: 25px; text-align: center">
                List of TF-IDF Recommended Degrees
              </h2>

              <select v-model="selectedDegree" size="5" class="selectionDegree">
                <option
                  v-for="(option, i) in this.furkansList"
                  :key="option[1]"
                  :value="option[1]"
                  @dblclick="openLink(option[1])"
                >
                  {{ i + 1 }}. {{ option[1] }}
                </option>
              </select>

              <p style="color: #003b7a; font-size: 25px">
                Click on degree to show hours info
              </p>
              <p style="color: #003b7a; font-size: 25px">
                Double click on degree to show main courses
              </p>

              <h3 style="text-align: center; color: #003b7a; font-size: 25px">
                HOURS
              </h3>

              <pie-chart :chartdata="pieChartData" :options="pieOptions" />
            </div>
          </div>
        </div>

        <p style="">
          <button class="resetButn" @click="reset">Reset</button>
        </p>
      </div>
    </div>

    <!-- footer start -->
    <div class="footer">
      <div class="footer-content">
        <div class="footer-section about">
          <h1 class="logo-text"><span> Dream </span> Degree Recomender</h1>
          <p>
            The "Dream Degree Recomender" is a tool that helps you... More often
            than not, students that are about to graduate highschool are still
            undecided about which university degree want to enroll in.
          </p>
        </div>

        <div class="footer-section uniLogo">
          <a href="https://www.uni-due.de/en/" target="_blank">
            <img src="../assets/images/UDE-logo.svg" />
          </a>
        </div>
        <div class="footer-section teamLogo">
          <a href="https://github.com/thedatadreams3-gmail-com" target="_blank">
            <img src="../assets/images/Final Logo.png" />
          </a>
        </div>

        <div class="footer-section links">
          <h2>Quick Links</h2>
          <br />
          <ul>
            <a
              href="https://www.uni-due.de/soco/teaching/courses/lecture-la-ws21.php"
              target="_blank"
            >
              <li>Learning Analytics</li>
            </a>
            <a
              href="https://github.com/thedatadreams3-gmail-com"
              target="_blank"
            >
              <li>Our GitHub</li>
            </a>
            <a
              href="https://www.uni-due.de/soco/people/mohamed-chatti.php"
              target="_blank"
            >
              <li>Mentores</li>
            </a>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2021 The Data Dreams Team <br />
        <span style="font-size: 20px">thedatadreams3@gmail.com</span>
      </div>
    </div>
    <!-- footer end -->
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
        field: "Computer Engineering",
      },
      related: [],
      options: [],
      furkansList: [],
      barOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{ stacked: true }],
          xAxes: [{ stacked: true }],
        },
        onClick: (e) => {
          let x = e.target.getElementsAtEvent(e);
          console.log(x);
        },
      },
      pieChartData: null,
      pieOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
      tfIdfPopped: false,
      countPopped: false,
      selectedCount: 10,
      selectedCount2: 10,
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
            backgroundColor: ["#003f5c", "#58508d", "#bc5090", "#ff6361"],
            data: [
              degreeInfo.lectures,
              degreeInfo.exercise,
              degreeInfo.practicum,
              degreeInfo.seminar,
            ],
          },
        ],
      };
    },
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
        labels: this.related.slice(0, this.selectedCount).map((x) => x.program),
        datasets: [
          {
            label: "Cosine Similarity Keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.related
              .slice(0, this.selectedCount)
              .map((x) => (parseFloat(x.similarity) * 100).toFixed(2)),
          },
        ],
      };
    },
    barChart2Data() {
      return {
        labels: this.furkansList.slice(0, this.selectedCount).map((x) => x[1]),
        datasets: [
          {
            label: "TF-IDF Sum Up",
            backgroundColor: "#70ad47",
            data: this.furkansList
              .slice(0, this.selectedCount)
              .map((x) => parseFloat(x[0]).toFixed(2)),
          },
        ],
      };
    },
    barChart3Data() {
      return {
        labels: this.gensimCourse
          .slice(0, this.selectedCount2)
          .map(
            (x) =>
              `${x.studyProgram.slice(0, x.studyProgram.indexOf("  PO"))} - ${
                x.courses
              }`
          ),
        datasets: [
          {
            label: "Cosine Similarity Keywords Percentage",
            backgroundColor: "#70ad47",
            data: this.gensimCourse
              .slice(0, this.selectedCount2)
              .map((x) => (parseFloat(x.similarity) * 100).toFixed(2)),
          },
        ],
      };
    },
  },
  methods: {
    async submit() {
      if (this.statement == "") {
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
        body: JSON.stringify({ a: this.statement }),
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
  },
};
</script>
<style>
.menu-item {
  display: block;
  background-color: #ddd;
  border-radius: 5px;
  margin: 5px;
  padding: 10px;
  font-size: 1.5rem;
  cursor: pointer;
  color: #003b7a;
}
.menu-item:hover {
  background-color: #fff;
}
.link {
  color: blue;
  cursor: pointer;
  text-align: center;
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
  background-color: #003b7a;
  color: white;
}
</style>
