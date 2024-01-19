<script setup>
const route = useRoute();
const user = useAttrs().user;
const { data } = await useFetch(`http://127.0.0.1:8000/categories/${route.params.category}`)
// console.log('what is inside categories/category ', data);
</script>


<template>
    <div>
        <h1>Cat / [ Category ] / [category].vue Page.</h1>
        <div v-for="item in data" :key="item.id">
            <h1>
                <!-- <NuxtLink :to="{
                    name: 'users-id-categories-category-id',
                    params: { id: item.id }
                }"> -->
                    {{ item.name }}
                <!-- </NuxtLink> -->
            </h1>
            <h2>category - {{ item.category }}</h2>
            <p>content - {{ item.content }}</p>
            <p>{{ item.detail_url }}</p>
        </div>

        <br>
        <!-- <h2>Hello world</h2> -->
        <!-- <h3>user - {{ user }}</h3> -->
    </div>
</template>


<style lang="scss" scoped></style>