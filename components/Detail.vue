<script setup>
// defineProps(["id", "title", "content", "author"]);
// defineProps(["id"]);
// const route = useRoute()
// import Detail from '~/components/Detail.vue';

// const url = useRequestURL()
// const { pending, data: posts } = useLazyFetch(`http://127.0.0.1:8000/detail/${route.params.slug}`);
const props = defineProps(['id', 'slug', 'title', 'content', 'author']);
</script>

<template>
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                <div class="p-4 md:w-1/3 flex">
                    <div class="flex-grow pl-6">
                        <h1 class="text-gray-900 text-lg title-font font-medium mb-2">{{ id }}</h1>
                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">{{ title }}</h2>
                        <p class="leading-relaxed text-base">{{ content }}.</p>
                        <a class="mt-3 text-indigo-500 inline-flex items-center">Detail - {{ author }}
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="css" scoped></style>