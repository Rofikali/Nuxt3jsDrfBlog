<script setup>
const data = {
    'id': 1,
    'title': 'this is first title'
}



defineProps{
    'id': '1',
        'title': 'hello man this is what happening here.'
}
</script>

<template>
    <div class="card-data">
        <h1>{{ data.id }}</h1>
        <h2>{{ data.title }}</h2>
    </div>
</template>


<style scoped>
.card-data {
    /* display: flex */
    border: 2px solid red;
    margin: auto;
    padding: 5px;
    width: 100%;
}
</style>