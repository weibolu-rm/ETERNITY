import { createApp } from 'vue'
import App from './App.vue'
import $ from 'jquery'

createApp(App).mount('#app')

$('input.nightModeSwitch').click(function() {
  $("html").toggleClass( "nightMode" );
});