<script setup>

const route = useRoute()

console.log('post detail is here', route.params.id);
console.log('attra foobar ', useAttrs().foobar);
// const url = useRequestURL()
// const { pending, data: posts } = useLazyFetch("http://127.0.0.1:8000/");
// console.log('iam data here', posts)

</script>

<template>
    <div>
        <div>
            <div>
                <LazyCard />
                <h1>Parents.vue page.</h1>
            </div>
        </div>
        <h2>Parents.vue page with composables same page.</h2>
        <NuxtPage :foobar="123" />
        <!-- <CategoriesSingleCategory /> -->
        <h1>Catching foobar value - {{ $attrs.foobar }}</h1>
        <!-- <Detail :id=1 /> ### this is working well i will do this.  -->
        <!-- <NuxtPage :id='123' /> -->
    </div>
</template>


<style scoped>
div {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 55px;
    border: 2px solid red;
    justify-content: space-around;
    margin: 5px;
    padding: 5px;
}
</style>