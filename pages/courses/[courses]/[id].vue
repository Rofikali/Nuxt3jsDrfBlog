<script setup>

// const user = useAttrs().user;

const route = useRoute();
const { data } = await useFetch(`http://127.0.0.1:8000/${route.params.courses}/${route.params.id}`)
console.log('courses here', data);

</script>

<template>
    <div>
        <h1>Courses / [Courses] / [id].vue Page.</h1>
        <!-- <h2>User - {{ user }}</h2> -->
        <br>
    </div>
    <div style="color: red;">
        <div v-for="item in data" :key="item.id">
            {{ item }}
        </div>
    </div>
</template>


<style scoped></style>