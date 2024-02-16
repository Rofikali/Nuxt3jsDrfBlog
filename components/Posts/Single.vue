<script setup>
// defineProps(['posts'])
defineProps({
    // posts: Object
    posts: {
        type: Object,
        required: true
    },
    error: {
        type: String
    },
    pending: {
        type: Boolean
    }
})

</script>
<template>
    <div>
        <div v-if="error">
            <h2>error is here - {{ error }}</h2>
        </div>
        <div v-else-if="pending">
            <h2>pending is here - {{ pending }}</h2>
        </div>
        <div v-else="posts">
            <div class="grid grid-rows-3 grid-flow-col gap-4">
                <div class="row-span-3 ...">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            ID - {{ posts.id }}
                                        </h2>
                                        <p class="leading-relaxed text-base">title - {{ posts.title }}.</p>
                                        <NuxtLink :to="{ name: 'posts-user', params: { user: posts.author } }">
                                            Author - {{ posts.author }}
                                        </NuxtLink>
                                        <h3>Content - {{ posts.content }}</h3>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped></style>