<script setup>

defineProps(
    {
        categoriesCategory: {
            type: Object
        },
        pending: {
            type: Boolean
        },
        error: {
            type: String
        }
    }
)


</script>

<template>
    <div class="main">
        <div v-if="pending">
            <h2>Pendig is here dud - {{ pending }}</h2>
        </div>
        <div v-else-if="error">
            <h2>Error occured here - {{ error }}</h2>
        </div>
        <div v-else class="main-list">
            <div v-for=" { id, name, category, content, detail_url, date_created, date_updated } in categoriesCategory"
                class="grid grid-rows-3 grid-flow-col gap-4" :key="id">
                <div class="row-span-3">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            <p>{{ id }}</p>
                                            <p>{{ name }}</p>
                                            <br>
                                            <h2>{{ category }}</h2>
                                            <NuxtLink :to="{ name: 'categories-category-id', params: { id: id } }">
                                                Category Deatail Page - {{ id }}
                                            </NuxtLink>
                                        </h2>
                                        <a class="mt-3 text-indigo-500 inline-flex items-center">Category Url - {{
                                            detail_url }}
                                        </a>
                                        <p>{{ content }}</p>
                                        <br>
                                        <p>{{ date_created }}</p>
                                        <p>{{ date_updated }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </div>
        <!-- <div class="main-detail">
            <h3>
                <h1>
                    Nuxt page is this.
                </h1>
                <NuxtPage />
            </h3>
        </div> -->
        <!-- <NuxtPage :user='categoriesCategory' /> -->
    </div>
</template>


<style scoped>
* {
    margin: 0%;
    padding: 0%;
    box-sizing: border-box;

}
</style>