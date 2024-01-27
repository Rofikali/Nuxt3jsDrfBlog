<script setup>

</script>

<template>
    <div>
        <nav class="container">
            <div class="one">
                <ul>
                    <li>
                        <NuxtLink :to="{ name: 'courses-python' }">courses-python </NuxtLink>
                    </li>
                </ul>
            </div>
            <div class="two">
                <ul>
                    <li>
                        <NuxtLink :to="{ name: 'courses-linux' }">courses-linux</NuxtLink>
                    </li>
                </ul>
            </div>
            <!-- <div class="three">
                <ul>
                    <li>
                        <NuxtLink :to="{ name: 'posts-trending' }">Tranding-Posts</NuxtLink>
                    </li>
                </ul>
            </div> -->
        </nav>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    /* border: 2px solid red; */
    gap: 15px;
    justify-content: center;
    width: 98%;
    margin: auto;
    text-shadow: 3px 3px 3px red;
    border-bottom: 2px solid rgb(240, 225, 225);
    padding: 15px;
}
</style>