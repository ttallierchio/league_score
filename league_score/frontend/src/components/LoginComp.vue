
<script>
    export default {
    data() {return {password:'',user_name:''}},
    methods: {
      login_test() {
        const formData = new FormData();
        var item = { username: this.user_name, password: this.password }
        Object.entries(item).forEach(([key, value]) => {
            formData.append(key, value);
        });
        const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body:  encodeURI(`username=${this.user_name}&password=${this.password}`)
      };
       fetch("http://localhost:8000/login", requestOptions)
        .then(response => response.json()).then( data =>
          document.cookie = encodeURIComponent("access_token") + '=' + encodeURIComponent(data["access_token"])
        )
      }
    }
    }
</script>
<style>
.div {
  position: fixed;
  inset: 0px;
  width: 12rem;
  height: 5rem;
  max-width: 100vw;
  max-height: 100dvh;
  margin: auto;
}</style>
<template>
  <div><h1>Enter your Login Information!</h1>
    <div>
        <div><label>User Name:</label><input v-model="user_name"></div>
      <div><label>Password:</label><input v-model="password" type="password"></div>
      <button @click="login_test">Login</button>
    </div>
</div>
  
</template>