<script setup>
const route = useRoute();
const { data } = await useFetch(`http://127.0.0.1:8000/categories/category/${route.params.id}`)
console.log('what is inside data', data);
</script>
<template>
    <div class="main">
        <div class="left">
            <!-- this is left side here. -->
            <h1>Users / [ ID.vue ] Page is this.</h1>
            <br>
            <li>
                <NuxtLink :to="{ name: 'users-id-categories' }">
                    All_Categories
                </NuxtLink>
            </li>
            <li>
                <NuxtLink to="#">Todos</NuxtLink>
            </li>
            <li>
                <NuxtLink to="#">Carts</NuxtLink>
            </li>
        </div>
        <div class="right">
            <!-- this is right side here. -->
            <div>
                <NuxtPage :user="data" />
            </div>
        </div>
    </div>
</template>
u   ewn

<style scoped>
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    /* margin: 5px; */
}

.left {
    border: 2px solid red;
    margin: 15px auto;
    padding: 10px;
    width: 40vw;
    height: 50vh;
}

.right {
    border: 2px solid green;
    margin: 15px;
    margin: 15px auto;
    padding: 10px;
    width: 40vw;
    height: 50vh;
}
</style>