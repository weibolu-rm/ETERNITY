<template>
  <ul class="uk-iconnav">
    <li><a href="" class="uk-text-primary uk-margin-small-right" uk-tooltip="title: Need help?"
           uk-icon="icon: question; ratio: 1.5"
           uk-toggle="target: #modal-close-default"></a>
      <div id="modal-close-default" uk-modal>
        <div class="uk-modal-dialog uk-modal-body" id="modal-theme">
          <button class="uk-modal-close-default" type="button" uk-close></button>
          <h2 class="uk-modal-title">How to write our functions?</h2>
          <p class="text-black">arccos(x) &rarr; arccos(x)</p>
          <p class="text-black">sinh(x) &rarr; sinh(x)</p>
          <p class="text-black">log<sub>b</sub>(x) &rarr; log(b, x)</p>
          <p class="text-black">MAD &rarr; MAD(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ...)</p>
          <p class="text-black">σ(x) &rarr; sd(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ...)</p>
          <p class="text-black"> ab<sup>x</sup> &rarr; abPow(a, b, x)</p>
          <p class="text-black"> x<sup>y</sup> &rarr; pow(x, y)</p>
        </div>
      </div>
    </li>
    <li><label class="switch nightModeSwitch" uk-tooltip="title: Switch to dark/light mode">
      <a class="nightModeSwitch uk-text-primary uk-margin-small-right" uk-icon="icon: paint-bucket; ratio: 1.5"></a>
    </label></li>
  </ul>
  <h1>Eternity Calculator</h1>
  <Calculator/>
</template>

<script>
import Calculator from './components/Calculator.vue'

export default {
  name: 'App',
  components: {
    Calculator
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
