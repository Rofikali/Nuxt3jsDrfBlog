<script setup>

const route = useRoute();
// const user = useAttrs().user;
const { data } = await useFetch(`http://127.0.0.1:8000/categories/category/${route.params.id}`)
// console.log('what is inside categories/category ', data);
</script>

<template>
    <!-- <div class="main"> -->
    <!-- {{ data }} -->
    <!-- <div class="first"> -->
    <h1>Categories / [category] / [id.vue] Page.</h1>
    <div>
        <!-- <Card /> -->
        <!-- <categoriesSingleCategory /> -->
        {{ data }}
        <h2>Data is here - </h2>
        <!-- user  {{ user }} -->
    </div>
    <!-- <div v-for="item in data" :key="item.id">
                <h1> -->
    <!-- <NuxtLink :to="{
                        name: 'users-id-categories-category-id',
                        params: { id: item.id }
                    }"> -->
    <!-- categories titles - {{ item.name }} -->
    <!-- </NuxtLink> -->
    <!-- </h1> -->
    <!-- <h2>category - {{ item.category }}</h2>
                <p>content - {{ item.content }}</p> -->
    <!-- <p>{{ item.detail_url }}</p> -->
    <!-- </div> -->
    <!-- </div> -->
    <!-- <br> -->
    <!-- <div class="second">
            <h2>Nuxt Page</h2> -->
    <!-- <NuxtPage /> -->
    <!-- <h3>user - {{ user }}</h3> -->
    <!-- </div> -->
    <!-- </div> -->
</template>


<style scoped>
.main {
    display: flex;
    width: 90%;
    justify-content: center;
    align-items: center;
    border: 2px solid rgb(0, 4, 255);
    margin: auto;
}

.first {
    border: 2px solid red;
    width: 45%;
    margin: 10px;
}

.second {
    border: 2px solid rgb(0, 110, 255);
    width: 45%;
}
</style>