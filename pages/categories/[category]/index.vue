<script setup>

const route = useRoute();

</script>

<template>
    <div>
        <!-- <h1>Categories's Category page is this.</h1> -->
        <h2>
            Category Name - {{ route.params.category }}
            <LazyCategoriesCategory />
        </h2>
    </div>
</template>


<style scoped></style>