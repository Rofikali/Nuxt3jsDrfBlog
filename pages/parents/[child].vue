<script setup>

const route = useRoute()
// import Detail from '~/components/Detail.vue';

const url = useRequestURL()
const { error, pending, data: posts } = useLazyFetch(`http://127.0.0.1:8000/detail/${route.params.child}`);

</script>

<template>
    <div>
        <h1>This is parents child page here</h1>
        <div v-if="pending">
            Loading ...
        </div>
        <div v-else-if="posts">
            ID is here - {{ route.params.child }}
            <LazyDetail :id=posts.id :slug=posts.slug :title=posts.title :content=posts.content :author=posts.author
                :key="posts.id" />
        </div>
        <div v-else="error">
            <h1>Error occured ... {{ error }}</h1>
        </div>
        <p>
            URL IS here - {{ url }}
        </p>
    </div>
    <!-- { -->
    <!-- new here  -->
    <!-- <h2>User - [child].vue - {{ user }}</h2> -->
    <!-- <div>
        <section class="text-gray-600 body-font">
            <div class="container px-5 py-24 mx-auto">
                <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                    <div class="p-4 md:w-1/3 flex">
                        <div class="flex-grow pl-6">
                            <h1 class="text-gray-900 text-lg title-font font-medium mb-2">ID - {{ posts.id }}</h1> -->
    <!-- <h2 class="text-gray-900 text-lg title-font font-medium mb-2">Title - {{ posts.title }}</h2>
                            <p class="leading-relaxed text-base">Content - {{ posts.content }}.</p>
                            <a class="mt-3 text-indigo-500 inline-flex items-center">Author - {{ posts.author }}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div> -->
    <!-- } -->
</template>


<style scoped></style>