<script setup>

// const user = useAttrs().user;
// new one 
const route = useRoute();
const { data } = await useFetch(`http://127.0.0.1:8000/${route.params.courses}`)
console.log('courses here', data);
</script>

<template>
    <div class="main">
        <div class="first">
            <h1>Courses / [courses].vue <strong>'First One'.</strong></h1>
            <div v-for="item in data" :key="item.id">
                <h1>
                    <NuxtLink :to="{
                        name: 'courses-courses-id',
                        params: { id: item.id }
                    }">
                        titles - {{ item.title }}
                    </NuxtLink>
                </h1>
            </div>
        </div>
        <br>
        <div class="second">
            <h1>Courses / [courses].vue <strong> 'NuxtPage'/'Second One'.</strong></h1>
            <!-- <NuxtPage :user="123" /> -->
            <NuxtPage />
            <!-- <NuxtPage :user="data" /> -->
        </div>
    </div>
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