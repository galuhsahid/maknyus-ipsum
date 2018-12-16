<template>
  <div id="app">
    <div id="left"></div>
    <h1 class="title">Maknyus Ipsum</h1>
    <Generator />
    <Footer />
  </div>
</template>

<script>
import Footer from './components/Footer'
import Generator from './components/Generator'
export default {
  name: 'app',
  components: {
    Generator,
    Footer
  }
}
</script>

<style lang="scss">
  // Import Google Fonts
  @import url('https://fonts.googleapis.com/css?family=Cabin');
  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";
  // Colors
  $body-background-color: #FFF1EE;
  $body-color: #060F46;
  $primary: #FF3543;
  $primary-invert: findColorInvert($primary);
  $secondary: #2852FF;
  $secondary-invert: findColorInvert($secondary);
  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;
  // Font
  $family-primary: 'Cabin', sans-serif;
  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
  #left {
    background: $secondary;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    width: 15px;
    margin-right: 15px;
  }
  .title {
    color: $primary;
    padding: 50px;
    text-align: center;
  }
  .section .selector {
    font-size: 1.5rem;
    background-color: $white;
    border-radius: 5px;
    margin: 15px 30px;
    padding: 15px;
  } 
  .section .output {
    background-color: $white;
    border-radius: 5px;
    margin: 15px 30px;
    padding: 15px;
  }
  .section {
    padding: 15px;
  }
  span {
    font-size: 1.2rem;
    font-weight: 400;
  }
</style>
