<script setup>
const route = useRoute();
const user = useAttrs().user;
</script>

<template>
    <div>
        <h1>Cat / [ Category ] / index.vue </h1>
        <div v-for="item in user" :key="item.id">
            <h1>
                <!-- <NuxtLink :to="{
                    name: 'users-id-categories-category-id',
                    params: { id: item.id }
                }"> -->
                {{ item.name }}
                <!-- </NuxtLink> -->
            </h1>
            <h2>category - {{ item.category }}</h2>
            <p>content - {{ item.content }}</p>
            <p>{{ item.detail_url }}</p>
        </div>

        <br>
        <div>
            <h2>Hello world</h2>
            <h3>user - {{ user }}</h3>
        </div>
    </div>
</template>


<style lang="scss" scoped></style>