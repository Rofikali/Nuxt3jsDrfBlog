<script setup>
const route = useRoute();
const id = route.params.id
// console.log('here is id', id);
// import { onMounted } from "vue";
import useShowPosts from '~/composables/postsData';
import { onMounted } from "vue";

// const { allposts } = useShowPosts();
const {
    posts,
    error,
    pending,
    getPosts
} = useShowPosts('http://127.0.0.1:8000/posts/' + id);
onMounted(getPosts);


</script>
<template>
    <div>
        <div v-if="error">
            <h2>error is here - {{ error }}</h2>
        </div>
        <div v-else-if="pending">
            <h2>pending is here - {{ pending }}</h2>
        </div>
        <div v-else>
            data - {{ posts }}
        </div>
        <div v-else="posts">
            <div class="grid grid-rows-3 grid-flow-col gap-4">
                <div class="row-span-3 ...">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            ID - {{ posts.id }}
                                        </h2>
                                        <p class="leading-relaxed text-base">title - {{ posts.title }}.</p>
                                        <a class="mt-3 text-indigo-500 inline-flex items-center">Author - {{ posts.author }}
                                        </a>
                                        <h3>Content - {{ posts.content }}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped></style>