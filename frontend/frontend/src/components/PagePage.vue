<template>
  <div class="dark-bg font-light middle">
    <p>{{ msg }}</p>
  </div>
</template>

<!-- this pages is a test to how i can GET request to za server to get something -->

<script>
import axios from 'axios' //a bridge between back and front

export default {
  name: 'PagePage',
  data() {
    return {
      msg: '' //get msg from flask api
    }
  },

  methods: {
    getResponse() {
      //a func we made that gets the mssg from the backend flask app.py page()
      const path = 'http://localhost:5000/pagepage'
      axios
        .get(path) //sends a get
        .then((res) => {
          //handle the responses
          console.log(res.data) //shhows us
          this.msg = res.data //res.data contains the respnse from backend and stores it in msg
        })
    }
  },

  created() {
    this.getResponse() //runs the getresponse func when ??component is initialized???
  }
}
</script>
