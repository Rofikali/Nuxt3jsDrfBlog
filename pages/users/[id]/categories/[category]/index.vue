<script setup>
const route = useRoute();
const { data } = await useFetch(`http://127.0.0.1:8000/categories/${route.params.category}`)
console.log('what is inside categories/category ', data);
</script>

<template>
    <div class="main">
        <div class="left">
            <h1>Users / [ ID ] Categories / [ Category.vue ] Page is this.</h1>
        </div>
        <div class="right">
            <div v-for="item in data" :key="item.id">
                <!-- ID - {{ item.id }} -->
                <h1>
                    <NuxtLink :to="{
                        name: 'users-id-categories-category-id',
                        params: { id: item.id }
                    }">
                        {{ item.name }}
                    </NuxtLink>
                </h1>

                <!-- <h1>name - {{ item.name }}</h1> -->
                <h2>category - {{ item.category }}</h2>
                <p>content - {{ item.content }}</p>
                <p>{{ item.detail_url }}</p>
            </div>
        </div>
    </div>
</template>


<style scoped>
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    /* margin: 5px; */
}

.left {
    border: 2px solid rgb(0, 26, 255);
    /* margin: 15px auto; */
    margin-left: 5px;
    padding: 10px;
    width: 50vw;
    height: 60vh;
    /* height: auto; */
}

.right {
    border: 2px solid rgb(128, 4, 0);
    /* margin: 55px; */
    margin: 5px auto;
    /* margin-right: 1px; */
    padding: 15px;
    /* padding: 25px; */
    width: 50vw;
    height: 50vh;
    /* height: auto; */
}
</style>