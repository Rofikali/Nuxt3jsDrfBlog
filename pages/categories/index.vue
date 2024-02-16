<script setup>

import useCategoryPosts from '~/composables/categoriesData'
import { onMounted } from "vue";

const {
    pendings,
    categories,
    errors,
    getCategories
} = useCategoryPosts();
// } = useCategoryPosts('http://127.0.0.1:8000/categories/');
onMounted(getCategories);


</script>

<template>
    <div>
        <h1>Categories / index.vue Page.</h1>
        <LazyCategories :categories="categories" :pendings="pendings" :errors="errors" />
    </div>
</template>


<style scoped></style>