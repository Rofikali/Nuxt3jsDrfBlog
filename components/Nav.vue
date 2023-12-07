<script setup>

</script>
<template>
  <div class="gird-layout">
    <nav class="one">
      <ul>
        <li>
          <NuxtLink to="/">Home</NuxtLink>
        </li>
        <li>
          <NuxtLink :to="{ name: 'posts' }">Posts</NuxtLink>
        </li>
        <li>
          <NuxtLink :to="{ name: 'about' }">About</NuxtLink>
        </li>
      </ul>
    </nav>
  </div>
</template>


<style scoped>
.grid-layout {
  display: grid;
  /* grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-auto-rows: 200px;
  border: 3px solid green; */
}

/* .one {
  border: 2px solid red;
  height: 100%;
  width: 100%;
  grid-column-start: 1;
  grid-column-end: 4;
  display: flex;
  justify-content: center;
  align-items: center;
  /* display: inline-block;
  padding: 3px;

} */
* {
  padding: 0%;
  margin: 0%;
  box-sizing: border-box;
}

.one ul {
  display: flex;
  justify-content: center;
  align-items: center;
}

.one ul li {
  padding: 1%;
  border: 2px solid red;
  list-style: none;
  box-sizing: border-box;
}
</style>