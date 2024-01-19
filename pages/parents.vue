<script setup>

// const route = useRoute()


// console.log('post detail is here', route.params.id);
// const url = useRequestURL()

// {
// new here 
// const { pending, data: posts } = useLazyFetch("http://127.0.0.1:8000/");
// console.log('iam data here', posts)
// }

</script>

<template>
    <div class="main">
        <div class="right">
            <div>

                <LazyCard />

                <!-- { -->

                <!-- <h1>Parents.vue page.</h1>
                <div v-for="item in posts" :key="item.id">
                    <NuxtLink :to="{ name: 'parents-child', params: { child: item.id } }">
                        <h1> Title - {{ item.title }}</h1>
                    </NuxtLink>
                    <h1> Author - {{ item.author }}</h1>
                    <h1> Content - {{ item.content }}</h1>
                </div> -->

                <!-- }  -->

            </div>
        </div>

        <div class="left">
            <h2>Parents.vue page for child page</h2>
            <!-- <NuxtPage /> -->
            <!-- { -->
            <!-- new here  -->
            <NuxtPage />
            <!-- } -->
            <!-- <h1>Catching foobar value</h1> -->
        </div>
    </div>
</template>


<style scoped>
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 55px;
    border: 2px solid rgb(0, 4, 255);
    margin: 5px;
    padding: 5px;
}

.right {
    border: 2px solid red;
    width: 40%;
    height: auto;
}

.left {
    border: 2px solid rgb(255, 208, 0);
    width: 40%;
    height: auto;
}
</style>