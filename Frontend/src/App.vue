<template>
  <div id="app">
    <div class="navbar">
      <a href="#" @click="page = 'home'">Home</a>
      <a href="#" @click="page = 'about'">About</a>
      <div class="dropdown">
        <button class="dropbtn">
          Sources
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="https://www.uni-due.de/vdb/studiengang/liste" target="_blank">Study Courses List</a>
        </div>
      </div>
    </div>
    <home-page v-if="page == 'home'" />
    <about-page v-if="page == 'about'" />
  </div>
</template>

<script>
import HomePage from "./components/Home.vue";
import AboutPage from "./components/About.vue";

export default {
  components: {
    HomePage,
    AboutPage
  },
  data: () => ({
    page: "home"
  })
};
</script>

<style>
body {
  padding: 0;
  margin: 0;
  font-family: "Rockwell", Helvetica, sans-serif;
}

.navbar {
  overflow: hidden;
  background-color: #333;
}

.navbar a {
  float: left;
  font-size: 20px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Header Design */

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 20px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover,
.dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}
/*End of Header design  */

table {
  width: 100%;
}

.action-button {
  background-color: #333;
  color: white;
  padding: 1rem 2rem;
  border: solid 1px #666;
  border-radius: 5px;
  cursor: pointer;
}
.action-button.small {
  padding: 3px 6px;
}
.action-button:hover {
  background-color: #444;
}
</style>
