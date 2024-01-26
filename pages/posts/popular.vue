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
            <div v-for="item in data" :key="item.id" class="fst">
                <NuxtLink :to="{ name: 'posts-popular-id', params: { id: item.id } }">
                    <h2>Title - {{ item.title }}</h2>
                </NuxtLink>
            </div>
            <!-- <div class="single-data">
                <h2>NuxtPage</h2>
                here would be Q/N, Accouncement, DownloadableData.
                like ( CWD )
                <NuxtPage />
            </div> -->
        </div>
        <div class="right-one">
            <!-- here would be single data -->
            <h2>NuxtPage</h2>
            <!-- <NuxtPage /> -->
            <PostsSingle />
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

.fst {
    border: 2px solid green;
}

.listing-data {
    border: 2px solid rgb(128, 0, 0);
    width: 25%;
}

.single-data {
    border: 2px solid rgb(255, 166, 0);
    width: 70%;
    margin: auto;
    margin-top: 5px;
}

.right-one {
    border: 2px solid red;
    margin: auto;

}
</style>