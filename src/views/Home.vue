<template>
  <div class="row">
    <div class="col-lg-3">
      <h3>Kategoriyalar</h3>
      <div class="list-group">
        <div class="list-group-item d-flex cat-item"
             :class="{'active': $route.params.id == c.id }"
             v-for="c in categories" :key="c.id" @click="onClickCategory(c)">
          <img :src="c.image" alt="Fuck you" class="cat-img me-3">
          {{ c.name }}
        </div>
      </div>
    </div>
    <div class="col-lg-9">
      <img style="max-width: 100%" src="../assets/banner.gif" alt="aaa">
      <div v-if="posts.count > 0">
        <Post class="st_post" v-for="p in posts.results" :post="p" :key="p.id" />
      </div>
      <div v-else>
        <h3>Birorta ham maqola topilmadi!</h3>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post";
export default {
  components: {Post},
  data(){
    return {
      categories : [],
      posts : []
    }
  },
  watch: {
    $route(){
      this.loadPosts();

      if(this.$route.params.id){
        this.$store.commit('add_breadcrumb',`${this.current_cat.name}`)
      }
    },
    '$i18n.locale':function (){
      this.loadPosts();
      this.loadCategories(() => {
        if(this.$route.params.id){
          this.$store.commit('clear_breadcrumb')
          this.$store.commit('add_breadcrumb',`${this.current_cat.name}`)
        }
      })
    }
  },
  mounted() {
    this.loadCategories(() => {
    if(this.$route.params.id){
      this.$store.commit('add_breadcrumb',`${this.current_cat.name}`)
    }
  })
    this.loadPosts()
  },
  methods: {
    loadCategories(on_finish){
      this.$axios.get('categories/').then(r => {
        this.categories = r.data

        if(typeof on_finish === 'function'){
          on_finish();
        }
      })
    },
    loadPosts(){
      let url ="posts/";
      if (this.$route.params.id){
        url += this.$route.params.id.toString() + "/"
    }
      this.$axios.get(url).then(r => {
        this.posts = r.data
      })
    },
    onClickCategory(c){
      this.$router.push({
        name : 'cat', params: {id: c.id}
      })
    }
  },
  computed:{
    current_cat(){
      for(let i in this.categories){
        if(this.categories[i].id == this.$route.params.id){
          return this.categories[i];
        }
      }
      return null;
    }
  }


}
</script>

<style>
.cat-img{
  max-height: 30px;
}
.cat-item{
  cursor: pointer;
}


.st_post{
  max-height: 500px;
}
</style>


