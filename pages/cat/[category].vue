<script setup>

const route = useRoute();
const { data } = await useFetch('http://127.0.0.1:8000/categories/')
console.log('what is inside data', data);

</script>

<template>
    <div class="main">
        <div class="left">
            <h1>Cat / [category ].vue Page.</h1>
            <div v-for="item in data">
                <h1>
                    <NuxtLink :to="{
                        name: 'cat-category-category',
                        params: { category: item.category }
                    }">
                        {{ item.category }}
                    </NuxtLink>

                </h1>
            </div>
        </div>

        <div class="right">
            <div>
                <NuxtPage :user="data" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3rem;
    /* padding: 10px; */
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

/* .middle {
    border: 2px solid green;
    margin: 15px;
    margin: 15px auto;
    padding: 10px;
    width: 40vw;
    height: 50vh;
} */
</style>