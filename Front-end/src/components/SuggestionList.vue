<template>
  <ul 
    v-if="suggestions && suggestions.length > 0"
    class="list-container"
  >
    <li 
      v-for="item in suggestions" 
      :key="item.term"
      @click="select(item.term)"
      class="list-item"
    >
      <div class="item-title">{{ item.term }}</div>
      <div class="item-score">score: {{ item.score }}</div>
    </li>
  </ul>
</template>

<script setup>
const props = defineProps({
  suggestions: Array
});

const emit = defineEmits(["selected"]);

function select(term) {
  emit("selected", term);
}
</script>


<style scoped>
/* List container */
.list-container {
  background: white;
  padding: 8px 0;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  border: 1px solid #e0e6ed;
  overflow: hidden;
}

/* Individual suggestion */
.list-item {
  padding: 14px 18px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;

  background: white;
  transition: background 0.2s ease, transform 0.15s ease;
}

.list-item:hover {
  background: var(--color-accent);
  transform: translateY(-1px);
}

/* Term */
.item-title {
  font-size: 17px;
  font-weight: 600;
  color: var(--color-primary);
}

/* Score */
.item-score {
  font-size: 14px;
  color: #6c7a89;
}
</style>
