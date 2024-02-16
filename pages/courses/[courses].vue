<script setup>



const route = useRoute();
const { data, pending, error } = await useFetch(`http://127.0.0.1:8000/${route.params.courses}`)
console.log('courses here', data);
console.log('type of data', typeof (data));

</script>

<template>
    <div>
        <LazyCourses :courses='data' />
    </div>
</template>


<style scoped></style>