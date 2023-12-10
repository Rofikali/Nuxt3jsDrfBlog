<script setup>

</script>
<template>
  <div class="gird-layout">
    <nav class="one">
      <ul>
        <li>
          <NuxtLink to="/">Home</NuxtLink>
        </li>
        <!-- <li>
          <NuxtLink :to="{ name: 'posts' }">Posts</NuxtLink>
        </li> -->
        <li>
          <NuxtLink :to="{ name: 'parents' }">Parents</NuxtLink>
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
}

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