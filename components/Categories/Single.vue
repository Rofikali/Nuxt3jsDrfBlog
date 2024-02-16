<script setup>

defineProps(
    {
        category: {
            type: Object
        },
        pending_data: {
            type: Boolean
        },
        error_data: {
            type: String
        }
    }
)

console.log('logs', typeof (category))
// console.log('logs data', category)

</script>

<template>
    <div>
        <p>single data is here - </p>
        <!-- {{ category }} -->
        <div v-if="pending_data">
            <h2>Pendig is here dud - {{ pending_data }}</h2>
        </div>
        <div v-else-if="error_data">
            <h2>Error occured here - {{ error_data }}</h2>
        </div>

        <div v-else="category">
            <div class="grid grid-rows-3 grid-flow-col gap-4">
                <div class="row-span-3">
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto">
                            <div class="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
                                <div class="p-4 md:w-1/3 flex">
                                    <div class="flex-grow pl-6">
                                        <h2 class="text-gray-900 text-lg title-font font-medium mb-2">
                                            <p>ID - {{ category.id }}</p>
                                            <p> Name -{{ category.name }}</p>
                                            <br>
                                            <h2>Category - {{ category.category }}</h2>
                                        </h2>
                                        <p>Content - {{ category.content }}</p>
                                        <br>
                                        <p>Date-Created - {{ category.date_created }}</p>
                                        <p>Date-Updated - {{ category.date_updated }}</p>
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