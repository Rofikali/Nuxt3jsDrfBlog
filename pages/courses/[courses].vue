<script setup>

import RichTextEditor from '~/components/RichTextEditor.vue'
const route = useRoute();
const { data, pending, error } = await useFetch(`http://127.0.0.1:8000/api/${route.params.courses}`)
console.log('courses here', data);
console.log('type of data', typeof (data));

</script>

<template>
    <div>
        <h2>[courses] page </h2>
        <RichTextEditor />
        <LazyCourses :courses='data' />
    </div>
</template>


<style scoped></style>
