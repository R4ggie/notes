<template>
  <content class="home">
    <div class="txt font-light font-lg dark-bg">
      <div class="middle">
        <h1>Welcome to the main page</h1>
        <button class="btn-cls">{{ msg }}</button>
        <ul>
          <li>
            <a href="https://www.google.com/">google</a>
          </li>
          <li>
            <a href="https://www.youtube.com/">youtube</a>
          </li>
          <div class="card">
            <div class="note">
              <input type="text" class="input-txt" name="note" />
            </div>
            <form method="POST" action="">
              <input type="submit" class="btn-cls" value="add" />
            </form>
          </div>
        </ul>
      </div>
    </div>
  </content>
</template>

<script>
import axios from "axios"; 

export default {
  //this renders the mssg to the template
  name: "HomePage",
  data() {
    return {
      msg: "", //get msg from flask api
    };
  },

  methods: {
    getResponse() {
      //a func we made that gets the mssg from the backend flask app.py page()
      const path = "http://localhost:5000/homepage";
      axios
        .get(path) //sends a request to this path
        .then((res) => {
          //res is short for response//then means do this with the response
          console.log(res.data); //res = return from app.py // shhows us in logs
          this.msg = res.data; //res.data contains the respnse from backend and stores it in msg
        });
    },
  },
  created() {
    this.getResponse(); //runs the getresponse func before the page loads cz it wont run unless with this or a button
  },
};
</script>
