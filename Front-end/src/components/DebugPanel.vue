<script setup>
import { debugStore } from "../store/debugStore";
import PathSteps from "./PathSteps.vue";
import RankFlow from "./RankFlow.vue";
import TrieTree from "./TrieTree.vue";
</script>

<template>
  <div 
    v-if="debugStore.debug" 
    class="debug-panel"
  >
    <h2 class="debug-title">Engine Debug View</h2>

    <section class="debug-section">
      <PathSteps :path="debugStore.debug.prefix_path" />
    </section>

    <section class="debug-section">
      <TrieTree :tree="debugStore.debug.trie_subtree" />
    </section>

    <section class="debug-section">
      <RankFlow 
        :input="debugStore.debug.rank_input"
        :output="debugStore.debug.rank_output"
      />
    </section>
  </div>
</template>

<style scoped>
/* ====================================== */
/* DEBUG PANEL CONTAINER                  */
/* ====================================== */
.debug-panel {
  width: 100%;
  background: var(--color-light);
  border-radius: 24px;
  padding: 32px 40px;
  box-shadow: 0 18px 45px rgba(0,0,0,0.18);
  animation: fadeIn 0.3s ease-out;

  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Fade animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ====================================== */
/* TITLE                                  */
/* ====================================== */
.debug-title {
  font-size: 28px;
  font-weight: 800;
  color: var(--color-primary);
  text-align: center;
  margin-bottom: 8px;
}

/* ====================================== */
/* EACH SECTION WRAPPER                   */
/* ====================================== */
.debug-section {
  padding: 20px 0;
  border-top: 1px solid rgba(0,0,0,0.08);

  /* Extra spacing between groups */
  display: flex;
  justify-content: center;
}

.debug-section:first-of-type {
  border-top: none;
}
</style>
