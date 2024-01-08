<script setup>
const route = useRoute();
const { data } = await useFetch(`http://127.0.0.1:8000/categories/category/${route.params.id}`)
// console.log('what is inside categories/category ', data);

</script>

<template>
    <div>
        <h1>Categories / [ Category ] [ id.vue ] Page. </h1>
        <br>
        <!-- <h2>Category single - {{ data }}</h2> -->
        <h1>name - {{ data.name }}</h1>
        <h2>category - {{ data.category }}</h2>
        <p>content - {{ data.content }}</p>
        <p>{{ data.detail_url }}</p>
    </div>
</template>


<style scoped></style>