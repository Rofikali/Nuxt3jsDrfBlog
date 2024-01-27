<script setup>

// const data = [
//     {
//         'id': 1,
//         'title': 'what is Python3'
//     },
//     {
//         'id': 2,
//         'title': 'python3 is a programming language.'
//     },
//     {
//         'id': 3,
//         'title': 'python3 use for hacking everything'
//     },
// ]

// props declare ( same page )
// const props = defineProps(['id', 'title'])

// props passing

// props user ( same page )


</script>
<template>
    <div>
        <h1>this is single course single datapage.</h1>
    </div>
</template>


<style scoped>
.container {
    display: flex;
    border: 2px solid rgb(0, 38, 255);
    width: 98%;
    gap: 10px;
    text-align: center;
    justify-content: center;
}

.fst {
    border: 2px solid green;
}

.listing-data {
    border: 2px solid rgb(128, 0, 0);
    width: 25%;
}

.single-data {
    border: 2px solid rgb(255, 166, 0);
    width: 70%;
    margin: auto;
    margin-top: 5px;
}

.right-one {
    border: 2px solid red;
    margin: auto;

}
</style>