<template>
  <div class="uk-container-xsmall uk-align-center">
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover uk-text-right uk-text-lead">
          {{ this.test }}
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">AC</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">arcos(x)</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">sinh(x)</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">log<sub>b</sub>(x)
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-success uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">MAD</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">σ(x)</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">ab<sup>x</sup>
        </div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-success uk-card-body uk-card-hover">x<sup>y</sup>
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">7</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">8</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">9</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&divide;</div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">4</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">5</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">6</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&times;
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">1</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">2</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">3</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&minus;
        </div>
      </div>
    </div>
    <div class="uk-grid-small uk-child-width-expand@s uk-text-center" uk-grid>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-card-body uk-card-hover">0</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&bullet;</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&equals;</div>
      </div>
      <div>
        <div class="uk-card uk-card-small uk-card-default uk-text-warning uk-card-body uk-card-hover">&plus;
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      test: ""
    }
  },
  async created() {
    const response = await fetch('http://127.0.0.1:8000/function/');
    this.test = await response.json();
    this.test = this.test['value']
  }
}
</script>