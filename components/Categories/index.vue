<script setup>

defineProps(
    {
        categories: {
            type: Object
        },
        pendings: {
            type: Boolean
        },
        errors: {
            type: String
        }
    }
)



</script>

<template>
    <div>
        <div v-if="pendings">
            <h2>Pendig is here dud - {{ pendings }}</h2>
        </div>
        <div v-else-if="errors">
            <h2>Error occured here - {{ errors }}</h2>
        </div>
        <div v-else>
            <div v-for=" { id, category, category_url } in categories" class="grid grid-rows-3 grid-flow-col gap-4"
                :key="id">
                <div class="row-span-3 ...">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            <h2>{{ category }}</h2>
                                            <NuxtLink :to="{ name: 'categories-category', params: { category: category } }">
                                                Category Name - {{ category }}
                                            </NuxtLink>
                                        </h2>
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