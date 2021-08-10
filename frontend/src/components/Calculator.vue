<template>
  <div class="uk-container-xsmall uk-align-center">
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <input ref="input_expression" style="text-align: right; border: none"
               class="uk-card uk-card-default uk-input uk-form-large" placeholder="Enter your expression"
               :value=this.display type="text">
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <a @click="clear" ref="clear" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">AC</a>
      </div>
      <div>
        <a @click="append('arccos(')" ref="arcos" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">arccos(x)</a>
      </div>
      <div>
        <a @click="append('sinh(')" ref="sinh" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">sinh(x)</a>
      </div>
      <div>
        <a @click="append('log(')" ref="log" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">log<sub>b</sub>(x)
        </a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-success uk-text-center" uk-grid>
      <div>
        <a @click="append('MAD(')" ref="mad" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">MAD</a>
      </div>
      <div>
        <a @click="append('sd(')" ref="standardDeviation" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">σ(x)</a>
      </div>
      <div>
        <a @click="append('abPow(')" ref="abPowerX" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">ab<sup>x</sup>
        </a>
      </div>
      <div>
        <a @click="append('pow(')" ref="xPowerY" style="text-decoration: none"
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
      <div uk-tooltip="title: pi">
        <a @click="append('3.141592653589793')" ref="pi" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">
          &#x03C0;</a>
      </div>
      <div uk-tooltip="title: euler's number">
        <a @click="append('2.718281828459045235360')" ref="e"
           style="text-decoration: none; font-style: italic; font-family: 'Times New Roman',serif"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">
          e</a>
      </div>
      <div uk-tooltip="title: gravity">
        <a @click="append('9.80665')" ref="g" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">g</a>
      </div>
      <div uk-tooltip="title: speed of light">
        <a @click="append('299792458')" ref="c" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover"><span
            style="font-style: italic; font-family: 'Times New Roman',serif">c</span> (m/s)</a>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div uk-tooltip="title: phi">
        <a @click="append('1.6180339887')" ref="phi" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">&#x0278;</a>
      </div>
      <div uk-tooltip="title: avogadro's number">
        <a @click="append('602214076000000000000000')" ref="mol" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">mol</a>
      </div>
      <div uk-tooltip="title: pythagoras constant">
        <a @click="append('1.414213562')" ref="pyth" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-primary uk-card-body uk-card-hover">&#8730;2</a>
      </div>
      <div uk-tooltip="title: save your answer">
        <a @click="ANS" ref="ANS" style="text-decoration: none"
           class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">ANS</a>
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
import axios from 'axios'

export default {
  data() {
    return {
      display: "",
      expression: "",
      ansVar: "",
      error: ''
    }
  },
  methods: {
    clear() {
      this.display = ""
    },
    append(value) {
      this.display += value
    },
    backspace() {
      this.display = this.$refs.input_expression.value.slice(0, -1);
    },
    ANS() {
      this.display += this.ansVar;
    },
    async evaluate() {
      this.expression = this.$refs.input_expression.value
      this.expression = this.expression.replace(/[/]/mg, 'divide')
      await axios
          .get('http://127.0.0.1:8000/' + this.expression + "/")
          .then((response) => {
            this.display = response.data;
            if (this.display === "None" || this.display === "") {
              this.display = "Math Error"
            }
            this.ansVar = this.display;
          })
          .catch((error) => {
            this.display = "Syntax Error"
            console.log(error.response)
          })
    },
  }
}
</script>
