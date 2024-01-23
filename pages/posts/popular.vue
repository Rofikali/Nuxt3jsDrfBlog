<script setup>

const data = [
    {
        'id': 1,
        'title': 'this is first title'
    },
    {
        'id': 2,
        'title': 'this is second title'
    },
    {
        'id': 3,
        'title': 'this is third title'
    },
]

</script>
<template>
    <div class='container'>
        <div class="listing-data">
            <div v-for="item in data" :key="item.id">
                <NuxtLink :to="{ name: 'posts-popular-id', params: { id: item.id } }">
                    <h2>Title - {{ item.title }}</h2>
                </NuxtLink>
            </div>
        </div>
        <div class="single-data">
            <h2>NuxtPage</h2>
            <NuxtPage />
        </div>
    </div>
</template>


<style scoped>
.container {
    display: flex;
    border: 2px solid rgb(0, 38, 255);
    width: 98%;
    gap: 10px;
    text-align: center;
    justify-content: center;
}

.listing-data {
    border: 2px solid rgb(128, 0, 0);
    width: 25%;
}

.single-data {
    border: 2px solid rgb(255, 166, 0);
    width: 70%;
}
</style>