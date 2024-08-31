<template>
    <div>
        <div ref="editorContainer"></div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import Quill from 'quill'
import 'quill/dist/quill.snow.css' // Use the Snow theme

const editorContainer = ref(null)

onMounted(() => {
    const quill = new Quill(editorContainer.value, {
        theme: 'snow', // Choose the Quill theme
        modules: {
            toolbar: [
                [{ header: [1, 2, false] }],
                ['bold', 'italic', 'underline'],
                [{ list: 'ordered' }, { list: 'bullet' }],
                ['link', 'image'],
            ],
        },
    })
})
</script>

<style scoped>
/* Add custom styles if needed */
</style>