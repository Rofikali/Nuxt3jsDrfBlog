<script setup>
const route = useRoute()
// import Detail from '~/components/Detail.vue';
import Card from '~/components/Card.vue';

// const url = useRequestURL()
// const { pending, data: posts } = useLazyFetch("http://127.0.0.1:8000/");
// console.log('iam data here', posts)
</script>

<template>
    <div>
        <div>
            <!-- <div v-if="pending">
                Loading ...
            </div> -->
            <div>
                <!-- <div v-for="post in posts">
                    <LazyCard :id=post.id :slug=post.slug :title=post.title :content=post.content :author=post.author
                        :key=post.id />
                </div> -->
                <LazyCard />
                <h1>Parents.vue page.</h1>
            </div>
        </div>
        <h2>This is Parents Page with composables.</h2>
        <!-- <NuxtPage :foobar="123" /> -->
        <NuxtPage :id='123' />
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