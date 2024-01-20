<script setup>

</script>

<template>
  <div>
    <nav>
      <ul>
        <li>
          <NuxtLink :to="{ name: 'posts-popular' }">Popular-Posts</NuxtLink>
        </li>
        <li>
          <NuxtLink :to="{ name: 'posts-resent' }">Resent-Posts</NuxtLink>
        </li>
        <li>
          <NuxtLink :to="{ name: 'posts-tranding' }">Tranding-Posts</NuxtLink>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style scoped></style>