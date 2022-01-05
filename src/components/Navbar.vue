<template>
  <nav class="navbar navbar-expand-lg navbar-light border-bottom">
    <div class="container">
      <router-link :to="{name : 'home'}" class="navbar-brand">9GaG</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
       <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
         <li class="nav-item">
            <button @click="$i18n.locale= 'en'" v-if="$i18n.locale != 'en'">EN</button>
           <button @click="$i18n.locale= 'uz'" v-if="$i18n.locale != 'uz'">UZ</button>
         </li>
         <li class="nav-item" v-if="!$store.state.profile">
           <router-link :to="{name: 'login'}" class="nav-link">{{ $t('login') }}</router-link>
         </li>
         <li class="nav-item" v-else>
           {{ $store.state.profile.username }} <a href="#" @click.prevent="onLogout">Fuck off</a>
         </li>
       </ul>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  methods:{
    onLogout(){
      this.$axios.delete('account/me/').then(() =>{
        alert("Fuck off");
      })
    }
  }
}
</script>
