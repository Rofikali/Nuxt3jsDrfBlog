<script setup>

// import { onMounted } from "vue";
// import RichTextEditor from '~/components/RichTextEditor.vue'
import useShowPosts from '~/composables/postsData';
import { onMounted } from "vue";


// const { allposts } = useShowPosts();
const {
    posts,
    error,
    pending,
    getPosts
} = useShowPosts();
onMounted(getPosts);


// console.log('Get-Posts', getPosts);

</script>


<template>
    <div>
        <div>
            <RichTextEditor />
        </div>
        <LazyPosts :posts="posts" :error="error" :pending="pending" />
    </div>
</template>


<style scoped></style>