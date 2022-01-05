<template>
  <h5>{{ post.subject }}</h5>
  <div v-if="post.is_image">
    <img :src="post.file" alt="" />
  </div>
  <div v-else-if="post.is_video">
    <video controls>
      <source :src="post.file" />
    </video>
  </div>
  <div v-else-if="post.is_audio">
    <audio controls>
      <audio :src="post.file" />
    </audio>
  </div>

  <div class="d-flex">
    <a href="#" class="me-3" @click="onClickLike('like')">Like:{{ like }}</a>
    <a href="#" @click="onClickLike('dislike')">Dislike:{{ dislike }}</a>
  </div>
  <hr>
</template>

<script>
export default {
  props: {
    post: {
      type:Object
    }
  },
  data(){
    return{
      like : this.post.like,
      dislike : this.post.dislike
    }
  },
  methods: {
    onClickLike(t){
      this.$axios.get('post/' + t + '/' + this.post_id + '/').then(() => {
        if (t === 'like') {
          this.like ++;
        }else{
          this.dislike ++
        }
      })
    }

  }
}
</script>