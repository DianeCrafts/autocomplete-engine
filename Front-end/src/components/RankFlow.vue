<script setup>
const props = defineProps({
  output: Array   // only final ranking needed now
});
</script>

<template>
  <div class="rank-wrapper">

    <h3 class="rank-title">Ranking</h3>

    <ul class="rank-list">
      <li 
        v-for="item in output" 
        :key="item.term"
        class="rank-item"
      >
        <span class="term">{{ item.term }}</span>
        <span class="score">score: {{ item.score.toFixed(2) }}</span>
      </li>
    </ul>

  </div>
</template>

<style scoped>
.rank-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
}

/* Centered, bold title */
.rank-title {
  font-size: 26px;
  font-weight: 800;
  color: var(--color-primary);
  margin-bottom: 20px;
}

/* Single column, centered */
.rank-list {  
  width: 100%;
  max-width: 650px;

  list-style: none;
  padding: 0;
  margin: 0;

  display: flex;
  flex-direction: column;
  gap: 14px;
}

/* Individual ranked item */
.rank-item {
  background: var(--color-accent);
  color: var(--color-primary);

  padding: 14px 20px;
  border-radius: 16px;

  display: flex;
  justify-content: space-between;
  align-items: center;

  font-size: 18px;
  font-weight: 600;

  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 4px 12px rgba(0,0,0,0.10);

  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.rank-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 14px rgba(0,0,0,0.15);
}

/* Term */
.term {
  font-weight: 700;
}

/* Score */
.score {
  font-size: 15px;
  opacity: 0.75;
}
</style>
