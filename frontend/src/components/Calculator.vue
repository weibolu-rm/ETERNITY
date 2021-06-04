<template>
  <p>Calculator works!</p>
  <p>{{ test }}</p>
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