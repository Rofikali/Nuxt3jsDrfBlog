<script setup>

const route = useRoute()
import Detail from '~/components/Detail.vue';

const url = useRequestURL()
const { error, pending, data: posts } = useLazyFetch(`http://127.0.0.1:8000/detail/${route.params.id}`);
</script>


<template>
    <div>
        <h1>post detail page slug wise ... wise</h1>
        <div v-if="pending">
            Loading ...
        </div>
        <div v-else-if="posts">
            ID is here - {{ route.params.id }}
            <Detail :id=posts.id :slug=posts.slug :title=posts.title :content=posts.content :author=posts.author
                :key="posts.id" />
        </div>
        <div v-else="error">
            <h1>Error occured ... {{ error }}</h1>
        </div>
        <p>
            URL IS here - {{ url }}
        </p>
    </div>
</template>

<style scoped></style>