<script setup>

import RichTextEditor from '~/components/RichTextEditor.vue'
const route = useRoute();
const { data, pending, error } = await useFetch(`http://127.0.0.1:8000/api/${route.params.courses}/${route.params.id}`)
console.log('courses id page here - Data ', data);
console.log('courses - Data ', route.params.courses);
console.log('id - Data ', route.params.id);

</script>

<template>
    <div>
        <RichTextEditor />
        <h3>[courses]/[id] page </h3>
        <LazyCoursesSingle :course="data" />
    </div>
</template>

<style scoped></style>
