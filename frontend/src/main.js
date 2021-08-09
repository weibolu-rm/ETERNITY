import { createApp } from 'vue'
import App from './App.vue'
import $ from 'jquery'

createApp(App).mount('#app')

$('a.nightModeSwitch').click(function() {
  $("html").toggleClass( "nightMode" );
  $("#modal-theme").toggleClass( "nightMode" );
});
