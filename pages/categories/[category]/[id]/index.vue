<script setup>

const route = useRoute();

</script>

<template>
    <div>
        <!-- <h1>Categories Category ID page is this.</h1> -->
        <h2>
            <!-- Categori id page is this. -->
            ID Number - {{ route.params.category }}
            <LazyCategoriesSingleCategory />
        </h2>
    </div>
</template>


<style scoped></style>