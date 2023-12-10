<script setup>
const route = useRoute()
// import Detail from '~/components/Detail.vue';
import Card from '~/components/Card.vue';

const url = useRequestURL()
const { pending, data: posts } = useLazyFetch("http://127.0.0.1:8000/");
// console.log('iam data here', posts)
</script>

<template>
    <div>
        <div>
            <div v-if="pending">
                Loading ...
            </div>
            <div v-else>
                <div v-for="post in posts">
                    <LazyCard :id=post.id :slug=post.slug :title=post.title :content=post.content :author=post.author
                        :key=post.id />
                </div>
            </div>
        </div>
        <h2>Hello Single Post is Here.</h2>
        <!-- <NuxtPage :foobar="123" /> -->
        <NuxtPage :id=posts.id />

    </div>
</template>


<style scoped>
div {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 55px;
    border: 2px solid red;
    justify-content: space-around;
    margin: 5px;
    padding: 5px;
}
</style>