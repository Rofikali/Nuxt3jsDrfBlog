<script setup>

// import useShowPosts from '~/composables/postsData';
import useCategoryPosts from '~/composables/categoriesData'
import { onMounted } from "vue";

// const {
//     pendings,
//     categories,
//     errors,
//     getCategories
// } = useCategoryPosts();
// onMounted(getCategories);
// } = useCategoryPosts('http://127.0.0.1:8000/categories/');


// new one 
// const route = useRoute();
// const { data } = await useFetch(`http://127.0.0.1:8000/${route.params.courses}`)

</script>
<template>
    <!-- <div v-if="pendings">
        <h2>Pendig is here dud - {{ pendings }}</h2>
    </div>
    <div v-else-if="errors">
        <h2>Error occured here - {{ errors }}</h2>
    </div>

    <div v-else class="snd-nav">
        <div v-for="item in categories" :key="item.id">
            <ul>
                <li>
                    <NuxtLink :to="{
                        name: 'categories-category',
                        params: { category: item.category }
                    }">
                        {{ item.category }}
                    </NuxtLink>
                </li>
            </ul>
        </div>
    </div> -->
    <br>
    <ul class="snd-nav">
        <li>
            <NuxtLink :to="{
                name: 'courses-courses',
                params: { courses: 'python' }
            }">
                Python
            </NuxtLink>
        </li>
        <br>
        <li>
            <NuxtLink :to="{
                name: 'courses-courses',
                params: { courses: 'posts' }
            }">
                Anothr_Posts
            </NuxtLink>
        </li>
        <br>
        <!-- <li>
            <NuxtLink :to="{
                name: 'courses-courses',
                params: { courses: 'django' }
            }">
            Django
        </NuxtLink>
    </li>
    <br> -->
    </ul>
</template>


<style scoped>
* {
    background-color: grey;
    margin: 0%;
    padding: 0%;
}

.snd-nav {
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px solid black;
}

ul {
    margin: 1rem;
    /* border: 2px solid green; */
}

ul li {
    padding: 1%;
    /* border: 2px solid rgb(255, 187, 0); */
    list-style: none;
    box-sizing: border-box;
    padding: 0.6em;
}
</style>