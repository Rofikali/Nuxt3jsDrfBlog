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
} = useCategoryPosts('http://127.0.0.1:8000/categories/category/' + route.params.id);
onMounted(getCategory);


</script>

<template>
    <h1>Categories / [category] / [id.vue] Page.</h1>
    <div>
        <h2>Data is here - </h2>
        <!-- {{ category }} -->
        <LazyCategoriesSingle :category="category" :pending_data="pending_data" :error_data="error_data" />
        <!-- user  {{ user }} -->
    </div>
</template>


<style scoped></style>