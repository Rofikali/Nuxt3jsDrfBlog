<script setup>
const url = useRequestURL()

</script>
<template>
    <div>
        <div class="grid-container">
            <header>
                <h1>Hello iam header here.</h1>
            </header>

            <main>
                <h2>hello iam main content here.</h2>
            </main>

            <aside>
                <h3>Hello iam aside bare here</h3>
            </aside>
            <p>URL is: {{ url }}</p>
            <p>Path is: {{ url.pathname }}</p>
        </div>
    </div>
</template>


<style lang="css" scoped>
.wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: 100px;
    border: 2px solid red;
}

.box1 {
    grid-column-start: 1;
    grid-column-end: 4;
    grid-row-start: 1;
    grid-row-end: 3;
    border: 2px solid green;
}

.box2 {
    grid-column-start: 1;
    grid-row-start: 3;
    grid-row-end: 5;
    border: 2px solid yellow;
    text-align: center;
}
</style>
