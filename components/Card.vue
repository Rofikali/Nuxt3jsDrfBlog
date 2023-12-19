<script setup>

// import { onMounted } from "vue";
import useShowPosts from '~/composables/postsData';

// const { allposts } = useShowPosts();
const { allposts, getPosts } = useShowPosts();

console.log('all posts, Card.vue Page', allposts);
console.log('first route, Card.vue Page', getPosts);


</script>
<template>
    <div>
        <!-- <div class="grid grid-rows-3 grid-flow-col gap-4" v-for=" ({ id, title, content, author }, i) in allposts"
            :key="id">
            <div class="row-span-3 ...">
                <section class="text-gray-600 body-font">
                    <div class="container px-5 py-24 mx-auto">
                        <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                            <div class="p-4 md:w-1/3 flex">
                                <div class="flex-grow pl-6">
                                    <h2 class="text-gray-900 text-lg title-font font-medium mb-2"> -->
        <!-- ID - {{ id }}
                                        <NuxtLink :to="{ name: 'parents-child', params: { child: id } }">
                                            {{ title }}
                                        </NuxtLink> -->
        <!-- <h2>{{ title }}</h2>
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
        </div> -->
        <h1>LazyCard page is this.</h1>
    </div>
</template>


<style scoped></style>