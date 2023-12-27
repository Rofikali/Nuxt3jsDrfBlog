
<template>
    <div>
        <Nav />
        <br>
        <BaseNav />
        <slot />
        <!-- <AppFooter /> -->
    </div>
</template>

<script setup>
import BaseNav from '~/components/base/BaseNav.vue';


</script>

<style scoped></style>