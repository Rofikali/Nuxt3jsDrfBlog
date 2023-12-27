<script setup>

// import { onMounted } from "vue";
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

console.log('all posts', posts);
console.log('get posts', getPosts);
// console.log('first route, Card.vue Page', getPosts);


</script>
<template>
    <div>
        <div v-if="error">
            <h2>error is here - {{ error }}</h2>
        </div>
        <div v-else-if="pending">
            <h2>pending is here - {{ pending }}</h2>
        </div>
        <div v-else="posts">
            <div v-for=" { id, title, content, author } in posts" class="grid grid-rows-3 grid-flow-col gap-4" :key="id">
                <div class="row-span-3 ...">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            ID - {{ id }}
                                            <NuxtLink :to="{ name: 'parents-child', params: { child: id } }">
                                                {{ title }}
                                            </NuxtLink>
                                            <h2>{{ title }}</h2>
                                        </h2>
                                        <p class="leading-relaxed text-base">{{ content }}.</p>
                                        <a class="mt-3 text-indigo-500 inline-flex items-center">Author Name - {{ author }}
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
        <!-- <div v-if="posts">
            <h1>if block - {{ posts }} <span>Nothing here. </span></h1>
            <br>
            <br>
        </div>
        <div v-else="">
            <h1>else block - </h1>
        </div> -->
        <h1>LazyCard page is this.</h1>
    </div>
</template>


<style scoped></style>