import { createStore } from 'vuex'

export default createStore({
  state: {
    profile : null,
    breadcrumb: []
  },
  mutations: {
    add_breadcrumb(state,data){
      state.breadcrumb.push(data)
    },
    clear_breadcrumb(state){
      state.breadcrumb.splice(0,state.breadcrumb.length)
    },
    profile(state,user){
      state.profile=user
      // this.$set(state.profile, user)
    },
    logout(state){
      state.profile = null;
    }
  },
  actions: {
  },
  modules: {
  }
})
