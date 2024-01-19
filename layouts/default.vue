<script setup>

</script>

<template>
    <div>
        <Nav />
        <br>
        <BaseNav />
        <!-- <header>
            <slot name="header">
                Default header content
            </slot>
        </header> -->
        <slot />
        <!-- <AppFooter /> -->
    </div>
</template>


<style scoped>
header {
    border: 2px solid red;
}
</style>