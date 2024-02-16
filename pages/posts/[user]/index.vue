<script setup>
const route = useRoute();
// import { onMounted } from "vue";
import useShowPosts from '~/composables/postsData';
import { onMounted } from "vue";

// const { allposts } = useShowPosts();
const {
    posts,
    error,
    pending,
    getPosts
} = useShowPosts('http://127.0.0.1:8000/user/' + route.params.user);
onMounted(getPosts);

</script>

<template>
    <div>
        <LazyPostsPerticularUser :posts="posts" :error="error" :pending="pending" />
        hello dud.
    </div>
</template>

<style scoped></style>