<script setup>

const route = useRoute();
const parameter = route.params.category
const add_id = route.params.id

// const user = useAttrs().user;

import useCategoryPosts from '~/composables/categoriesData'
import { onMounted } from "vue";

const {
    pending_data,
    error_data,
    category,
    getCategory
} = useCategoryPosts('http://127.0.0.1:8000/categories/category/' + 1);
// } = useCategoryPosts(`http://127.0.0.1:8000/categories/${route.params.category}`);
onMounted(getCategory);

</script>

<template>
    <div>
        <div v-if="pending_data">
            <h2>Pendig is here dud - {{ pending }}</h2>
        </div>
        <div v-else-if="error_data">
            <h2>Error occured here - {{ error_data }}</h2>
        </div>
        <!-- <div v-if="category">
            Categories Single Category is here - {{ category }}
        </div> -->

        <!-- <div v-for="item in categoriesCategory" :key="item.id">
            <h1>
                {{ item }}
                <br>
            </h1>
        </div> -->

        <div v-else>
            <div class="grid grid-rows-3 grid-flow-col gap-4">
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
                                            Category Deatail Page - {{ id }}
                                            <br>
                                            Category Deatail Page - {{ detail_url }}
                                        </h2>
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
        <!-- <h1>
            Category World Dud -> {{ route.params.category }}
            <h2>user - {{ user }}</h2>
        </h1> -->
        <!-- <h2>data - {{ getCategory }}</h2> -->
        <!-- <br>
        <h1>
            ID - World Dud -> {{ route.params.id }}
        </h1> -->
    </div>
</template>


<style scoped></style>