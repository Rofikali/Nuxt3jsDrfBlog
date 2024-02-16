<script setup>

const route = useRoute();
import useCategoryPosts from '~/composables/categoriesData'
import { onMounted } from "vue";

const {
    pending,
    categoriesCategory,
    error,
    getCategoriesCategory
} = useCategoryPosts(`http://127.0.0.1:8000/categories/${route.params.category}`);
onMounted(getCategoriesCategory);

import { ref } from 'vue';
const count = ref(0);


// Function to be executed after a delay
// function delayedFunction() {
//     console.log("This function was delayed!");
// }

// // Set a timeout of 2000 milliseconds (2 seconds) for the delayedFunction
// setTimeout(delayedFunction, 2000);

// import ID from '../categories/[category]/[id].vue'
import IdVue from '../categories/[category]/[id].vue';

</script>

<template>
    <div class="main">
        <div>
            <h1>Categories / [category].vue Page.</h1>
            <LazyCategoriesCategory :categoriesCategory="categoriesCategory" :pending="pending" :error="error" />
        </div>
        <div>
            <h2>Nuxt Page</h2>
            <!-- <button @click="count++">count is : {{ count }}</button> -->
            <button @click="">count is : {{ count }}</button>
            <NuxtPage />
            <!-- <CategoriesSingle :category="categoriesCategory" :pending_data="pending" :error_data="error" /> -->
            <!--  <NuxtPage :user="123" /> -->
            <!-- <NuxtPage :user="data" /> -->
        </div>
    </div>
</template>


<style scoped>
.main {
    display: flex;
}
</style>