<script setup>
const route = useRoute();
const { data } = await useFetch('http://127.0.0.1:8000/categories/')
console.log('what is inside data', data);
</script>
<template>
    <div class="main">
        <!-- <div class="left">
            this is left side here.
            <h1>Users / [ ID.vue ] Page is this.</h1>
            <br>
            <li>
                <NuxtLink :to="{ name: 'users-id-user_posts', params: { id: data.id } }">
                    User_Posts
                </NuxtLink>
            </li>
            <li>
                <NuxtLink :to="{ name: 'users-id-posts', params: { id: data.id } }">
                    All_Posts
                </NuxtLink>
            </li>
            <li>
                <NuxtLink to="#">Todos</NuxtLink>
            </li>
            <li>
                <NuxtLink to="#">Carts</NuxtLink>
            </li> 
        </div> -->
        <div class="left">
            <h1>About Page, Users / [ ID.vue ] Page is this.</h1>
            <div v-for="item in data" :key="item.id">
                <h1>
                    <!-- Category - {{ item.category }} -->

                    <NuxtLink :to="{
                        name: 'users-id-categories-category',
                        params: { category: item.category }
                    }">
                        {{ item.category }}
                        <!-- Categories/Category - {{ item.category }} -->
                    </NuxtLink>

                </h1>
            </div>
        </div>


        <!-- <div class="right">
            <div>
                <NuxtPage :user="data" />
            </div>
        </div> -->

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