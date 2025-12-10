<script setup>
import TrieNode from "./TrieNode.vue";

const props = defineProps({
  tree: Object
});
</script>

<template>
  <div class="trie-wrapper">
    <h3 class="trie-title">Trie Visualization</h3>

    <div class="trie-box">
      <TrieNode :node="tree" letter="root" />
    </div>
  </div>
</template>

<style scoped>
.trie-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.trie-title {
  font-size: 22px;
  font-weight: 800;
  color: var(--color-primary);
  margin-bottom: 16px;
}

.trie-box {
  width: 100%;
  max-height: none;
  overflow: visible;
  padding: 5px 0;
  background: var(--color-light);
  border-radius: 18px;
  /* box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12); */
  border: 1px solid rgba(0,0,0,0.08);

  /* Smooth scroll */
  scrollbar-width: thin;
  scrollbar-color: var(--color-secondary) transparent;
}

.trie-box::-webkit-scrollbar {
  width: 8px;
}

.trie-box::-webkit-scrollbar-thumb {
  background: var(--color-secondary);
  border-radius: 8px;
}

.trie-box::-webkit-scrollbar-track {
  background: transparent;
}
</style>
