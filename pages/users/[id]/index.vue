<script setup>

const user = useAttrs().user;

</script>

<template>
    <div>
        <h1>Users / [ ID ] / Index Page.</h1>
        <h2>User - {{ user }}</h2>
    </div>
</template>


<style scoped></style>