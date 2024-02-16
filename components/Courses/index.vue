<script setup>
// Notes - both are right 
// defineProps(['courses'])
// defineProps({
//     courses: Object
// })

const props = defineProps({
    courses: Object
})
// console.log('courses ', props.courses);

</script>

<template>
    <div class="main">
        <!-- main one  -->
        <div v-for="item in props.courses" :key="item.id" class="left-side">
            <h1>
                <NuxtLink :to="{
                    name: 'courses-courses-id',
                    params: { id: item.id }
                }">
                    <h1>
                        <strong> ID </strong>- {{ item.id }}
                    </h1>
                    <h1>
                        <strong> titles </strong>- {{ item.title }}
                    </h1>
                    <p>
                        <strong>content </strong> - {{ item.content.substring(0, 55) }}
                    </p>
                </NuxtLink>
            </h1>
        </div>

        <div class="right-side">
            <NuxtPage />
            <!-- <h2>right one</h2> -->
            <!-- <NuxtPage :user="data" /> -->
        </div>
    </div>
</template>


<style scoped>
.main {
    display: flex;
    width: 98%;
    height: auto;
    border: 2px solid red;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.left-side {
    border: 2px solid rgb(225, 228, 210);
    width: 30%;
    height: 155px;
    color: rgb(17, 16, 16);
    padding: 3px;
    text-align: justify;
    box-shadow: 2px 2px rgb(241, 233, 233);
    margin: 2px 3px;
    padding: 5px;
    border-radius: 5px;
}

.right-side {
    width: 66%;
    height: auto;
    color: rgb(17, 16, 16);
    padding: 10px;
    box-shadow: 2px 2px rgb(241, 233, 233);
    margin: 5px;
    border-radius: 5px;
}
</style>