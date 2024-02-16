<script setup>

const route = useRoute();
// const id = route.params.id
import useShowPosts from '~/composables/postsData';
import { onMounted } from "vue";

// const { allposts } = useShowPosts();
const {
    posts,
    error,
    pending,
    getPosts
} = useShowPosts('http://127.0.0.1:8000/posts/' + route.params.id);
onMounted(getPosts);


</script>

<template>
    <div>
        <LazyPostsSingle :posts="posts" :error="error" :pending="pending" />
    </div>
</template>


<style scoped></style>