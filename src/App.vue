<template>
  <navbar/>

  <div class="container mt-3">
    <nav v-if="$route.name != 'home'" class="border-bottom">
      <ol class="breadcrumb">
        <li class="breadcrumb-item" v-for="(b, i) in $store.state.breadcrumb" :key="i">
          <router-link :to="{name : 'home'}">{{ $t('home')}}</router-link></li>
        <li class="breadcrumb-item active" v-for="(b, i) in $store.state.breadcrumb" :key="i">
          {{ b }}
        </li>
      </ol>
    </nav>
    <router-view />
  </div>
</template>
<script>
import Navbar from "./components/Navbar"
export default {
  components: {Navbar},
  watch:{
    '$i18n.locale':function (to){
      localStorage.setItem('locale', to);
      this.$axios.defaults.baseURL = "/" + to + "/api";
    }

  }
}
</script>
