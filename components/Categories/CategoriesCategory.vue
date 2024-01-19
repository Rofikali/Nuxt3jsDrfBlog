<script setup>

const route = useRoute();
const parameter = route.params.category


import useCategoryPosts from '~/composables/categoriesData'
import { onMounted } from "vue";

const {
    pending,
    categoriesCategory,
    error,
    getCategoriesCategory
} = useCategoryPosts('http://127.0.0.1:8000/categories/', + parameter);
onMounted(getCategoriesCategory);

// } = useCategoryPosts(`http://127.0.0.1:8000/categories/${route.params.category}`);


</script>

<template>
    <div class="main">
        <div v-if="pending">
            <h2>Pendig is here dud - {{ pending }}</h2>
        </div>
        <div v-else-if="error">
            <h2>Error occured here - {{ error }}</h2>
        </div>
        <div v-else class="main-list">
            <div v-for=" { id, name, category, content, detail_url, date_created, date_updated } in categoriesCategory"
                class="grid grid-rows-3 grid-flow-col gap-4" :key="id">
                <div class="row-span-3">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            <p>{{ id }}</p>
                                            <p>{{ name }}</p>
                                            <br>
                                            <h2>{{ category }}</h2>
                                            <NuxtLink :to="{ name: 'categories-category-id', params: { id: id } }">
                                                Category Deatail Page - {{ id }}
                                            </NuxtLink>
                                        </h2>
                                        <a class="mt-3 text-indigo-500 inline-flex items-center">Category Url - {{
                                            detail_url }}
                                        </a>
                                        <p>{{ content }}</p>
                                        <br>
                                        <p>{{ date_created }}</p>
                                        <p>{{ date_updated }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
        <div class="main-detail">
            <h3>
                <h1>
                    Nuxt page is this.
                </h1>
                <NuxtPage :user='categoriesCategory' />
            </h3>
            <!-- categories-category-id -->
            <!-- <h1>What is Python3 use for</h1>
            <p>Python3 use for web development, data science, machin learning, website hacking, web browser hacking,
                operating system hacking and networ hacking, android phone hacking, mac os hacking and it's use for hacking
                anythng</p>
            <h3>Author - Micky Virus</h3>
            <p>Date - 12/11/2003</p>
            <h1>
                Categories category components -> {{ route.params.category }}
            </h1> -->
        </div>
    </div>
</template>


<style scoped>
* {
    margin: 0%;
    padding: 0%;
    box-sizing: border-box;

}

.main {
    display: flex;
    border: 2px solid rgb(13, 14, 13);
    width: 90vw;
    /* height: auto; */
    /* padding: 2 */
    margin: auto;
}

.main-list {
    border: 2px solid red;
    /* margin: 2em; */
    padding: 2em;
    /* display: flex; */
}


.main-detail {
    border: 2px solid green;
    padding: 2em;
    /* margin: 44px; */
    margin-left: 1em;
}
</style>