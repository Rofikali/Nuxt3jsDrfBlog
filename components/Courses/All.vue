<script setup>

// const data = [
//     {
//         'id': 1,
//         'title': 'what is Python3'
//     },
//     {
//         'id': 2,
//         'title': 'python3 is a programming language.'
//     },
//     {
//         'id': 3,
//         'title': 'python3 use for hacking everything'
//     },
// ]

// props declare ( same page )
// const props = defineProps(['id', 'title'])

// props passing

// props user ( same page )

// const data = useLazyAsyncData('http://127.0.0.1:8000/python')
const data = useLazyAsyncData()

console.log('data is here', data);

</script>
<template>
    <div class='container'>
        <div class="listing-data">
            <div v-for="item in data" :key="item.id" class="fst">
                <NuxtLink :to="{ name: 'courses-python-id', params: { id: item.id } }">
                    <h2>Title - {{ item.title }}</h2>
                </NuxtLink>
            </div>
        </div>
        <!-- <div class="single-data">
                <h2>NuxtPage</h2>
                here would be Q/N, Accouncement, DownloadableData.
                like ( CWD )
                <NuxtPage />
            </div> -->
        <!-- <div class="right-one"> -->
        <!-- here would be single data -->
        <!-- <NuxtPage /> -->
        <!-- <h2>NuxtPage</h2>
            <PostsSingle :id="props.id" :title="props.title" />
        </div> -->
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