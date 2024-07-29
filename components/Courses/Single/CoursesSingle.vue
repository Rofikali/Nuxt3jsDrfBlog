<script setup>

// defineProps(['course'])
defineProps({
    course: Object
})

</script>

<template>
    <div class="container">
        <div style="color: red;" class="left-sidebar">
            <div v-for="item in course" :key="item.id">
                {{ item }}
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    /* display: flex; */
    width: 100%;
    height: auto;
    border: 2px solid rgb(10, 32, 228);
    gap: 5px;
    padding: 10px;
    background-color: rgb(10, 10, 10);
    color: white;
}

.left-sidebar {
    border: 2px solid red;
}
</style>