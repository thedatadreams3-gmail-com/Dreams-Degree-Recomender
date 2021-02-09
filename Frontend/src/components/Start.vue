<template>
  <!-- below start page  -->
  <div class="startpageCss">
    <div class="leftColor">
      <p>
        <code
          ><h1 class="logo-texts">Dream Degree Recomender</h1>
          <a href="https://github.com/thedatadreams3-gmail-com" target="_blank">
            <img class="startPageLogo" src="../assets/images/Final Logo.png" />
          </a>
        </code>
      </p>
    </div>
  

    <div class="b">
      <h1 style="margin-left: 50px; font-size: 40px; margin-top: 25px">Are</h1>
      <h1 style="margin-left: 150px; font-size: 40px; margin-top: -19px">
        you
      </h1>
      <h1 style="margin-left: 245px; font-size: 40px">ready</h1>
      <h1 style="margin-left: 110px; font-size: 40px">for</h1>
      <h1 style="margin-left: 225px; font-size: 40px">your</h1>
      <h1 style="text-align: center; font-size: 50px">Dream Course?</h1>

      <!-- This div element has position: absolute and right: 0. -->
    </div>


    <div class="startButton" >
      <div> <button @click="goTo('/') " class="startButn">Start</button>
    </div>
    </div>

<!-- 
    <home-page v-if="page == 'home'" /> -->
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
      <div class="footer-bottom">&copy; 2021 The Data Dreams Team  <br>
      <span style="font-size: 20px;">thedatadreams3@gmail.com</span>
      </div>
    </div>

    <!-- footer end -->
  </div>
</template>

<script>
// import HomePage from "../components/Home.vue";

export default {
  components: {
    // HomePage,
  },
  data: () => ({
    page:"home"
  }),
  methods: {
    goTo() {
      window.location = 'home';
    }
  }
};
</script>

<style>
</style>