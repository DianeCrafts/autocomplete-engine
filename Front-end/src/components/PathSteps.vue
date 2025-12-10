<script setup>
const props = defineProps({
  path: Array
});
</script>

<template>
  <div class="path-wrapper">
    <h3 class="path-title">Prefix Path</h3>

    <div class="path-chips">
      <div 
        v-for="(letter, i) in path"
        :key="i"
        class="chip"
      >
        {{ letter }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.path-wrapper {
  width: 100%;
}

.path-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 10px;
}

.path-chips {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.chip {
  background: var(--color-secondary);
  color: var(--color-light);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 18px;
  font-weight: 600;
  box-shadow: 0 3px 6px rgba(0,0,0,0.15);
  transition: transform 0.15s ease;
}

.chip:hover {
  transform: scale(1.08);
}
</style>
