<template>
  <div class="row">
    <div class="col-lg-4 offset-lg-4">
      <form @submit.stop.prevent="onLogin" class="card">
        <div class="card-header">Fuck you</div>
        <div class="card-body">
          <div class="mb-3">
            <label>Username</label>
          <input type="text" class="form-control" v-model="form.username" />
          </div>
          <div class="mb-3">
          <label>Password</label>
          <input type="password" class="form-control" v-model="form.password" />
          </div>
          <button type="submit" class="bg-success">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      form:{
        username:"",
        password:""
      }
    }
  },
  mounted(){
    this.$store.commit('add_breadcrumb',"Tizimga Kirish")
  },
  methods:{
    onLogin(){
      this.$axios.post('account/login/',this.form).then(r =>{
        if (r.data.token){
          localStorage.setItem('token',r.data.token);
          this.$axios.defaults.headers['Authorization']="Token"+r.data.token;

          this.$store.commit('profile',r.data.user);

          this.$router.push({name:'home'})
        }
      })
    }
  }
}
</script>