<template>
<div class="uk-text-right">
<label class="switch nightModeSwitch">
  <input class="nightModeSwitch" type="checkbox" unchecked>
  <span class="slider round"></span>
</label>
</div>
  <div class="uk-container-xsmall uk-align-center">
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-default uk-card-default uk-card-body uk-text-right uk-text-lead">
          {{ this.equation }}
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="clear" ref="clear" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">AC</a>
      </div>
      <div>
        <a @click="arcos" ref="arcos" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">arccos(x)</a>
      </div>
      <div>
        <a @click="sinh" ref="sinh" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">sinh(x)</a>
      </div>
      <div>
        <a @click="log" ref="log" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">log<sub>b</sub>(x)
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-success uk-text-center" uk-grid>
      <div>
        <a @click="mad" ref="mad" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">MAD</a>
      </div>
      <div>
        <a @click="standardDeviation" ref="standardDeviation" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">σ(x)</a>
      </div>
      <div>
        <a @click="abPowerX" ref="abPowerX" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">ab<sup>x</sup>
        </a>
      </div>
      <div>
        <a @click="xPowerY" ref="xPowerY" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">x<sup>y</sup>
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-success uk-text-center" uk-grid>
      <div>
        <a @click="append('(')" ref="lparen" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-text-warning uk-card-body uk-card-hover">&lpar;</a>
      </div>
      <div>
        <a @click="append(')')" ref="rparen" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-text-warning uk-card-body uk-card-hover">&rpar;</a>
      </div>
      <div>
        <a @click="append(', ')" ref="comma" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-text-warning uk-card-body uk-card-hover">&comma;
        </a>
      </div>
      <div>
        <a @click="backspace()" ref="backspace" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">DEL
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="append('7')" ref="seven" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">7</a>
      </div>
      <div>
        <a @click="append('8')" ref="eight" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">8</a>
      </div>
      <div>
        <a @click="append('9')" ref="nine" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">9</a>
      </div>
      <div>
        <a @click="append('/')" ref="divide" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-text-warning uk-card-body uk-card-hover">
          &divide;
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="append('4')" ref="four" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">4</a>
      </div>
      <div>
        <a @click="append('5')" ref="five" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">5</a>
      </div>
      <div>
        <a @click="append('6')" ref="six" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">6</a>
      </div>
      <div>
        <a @click="append('*')" ref="multiply" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-text-bold uk-card-body uk-card-hover">
          &times;
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="append('1')" ref="one" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">1</a>
      </div>
      <div>
        <a @click="append('2')" ref="two" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">2</a>
      </div>
      <div>
        <a @click="append('3')" ref="three" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">3</a>
      </div>
      <div>
        <a @click="append('-')" ref="minus" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-text-bold uk-card-body uk-card-hover">
          &minus;
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="append('.')" ref="decimal" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&bullet;</a>
      </div>
      <div>
        <a @click="append('0')" ref="zero" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-bold uk-card-body uk-card-hover">0</a>
      </div>
      <div>
        <a @click="evaluate" ref="equals" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-text-bold uk-card-body uk-card-hover">
          &equals;
        </a>
      </div>
      <div>
        <a @click="append('+')" ref="plus" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-text-bold uk-card-body uk-card-hover">
          &plus;
        </a>
      </div>
    </div>
  </div>

</template>
<script>
export default {
  data() {
    return {
      equation: "",
      expression: ""
    }
  },
  methods: {
    clear() {
      this.display = ""
      this.equation = ""
    },
    arcos() {
      this.equation = "arccos"
    },
    sinh() {
      this.equation = "sinh"
    },
    log() {
      this.equation = "log"
    },
    mad() {
      this.equation = "mad"
    },
    standardDeviation() {
      this.equation = "standard deviation"
    },
    abPowerX() {
      this.equation = "ab power x"
    },
    xPowerY() {
      this.equation = "x power y"
    },
    append(value) {
      this.equation += value
    },
    backspace(){
      this.equation = this.equation.slice(0,-1);
    },
    async evaluate() {
      this.expression = this.equation.replace(/[/]/mg, 'divide')
      let response = await fetch('http://127.0.0.1:8000/' + this.expression + "/");
      this.equation = await response.json();
    }
  }
}
</script>