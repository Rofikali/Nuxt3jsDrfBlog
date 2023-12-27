<script setup>

// import Detail from '~/components/Detail.vue';
import Card from '~/components/Card.vue';

const url = useRequestURL()
const { pending, data: posts } = useLazyFetch("http://127.0.0.1:8000/");
// console.log('iam data here', posts)

</script>


<template>
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
</template>

<style scoped></style>