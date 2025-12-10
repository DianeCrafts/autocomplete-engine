<script setup>
import { ref } from "vue";
import { fetchSuggestions } from "../services/api";
import { debugStore } from "../store/debugStore";

const emit = defineEmits(["suggestions"]);
const query = ref("");

let debounceTimer;

async function handleInput() {
  clearTimeout(debounceTimer);

  debounceTimer = setTimeout(async () => {
    if (!query.value) {
      emit("suggestions", []);
      debugStore.setDebug(null);
      return;
    }

    const res = await fetchSuggestions(query.value, true);
    emit("suggestions", res.suggestions);

    if (debugStore.enabled) {
      debugStore.setDebug(res.debug);
    }
  }, 300);
}


function clear() {
  query.value = "";
  emit("suggestions", []);
  debugStore.setDebug(null);
}

defineExpose({ clear });
</script>

<template>
  <input
    v-model="query"
    @input="handleInput"
    type="text"
    placeholder="Search..."
    class="search-input"
  />
</template>

<style scoped>
.search-input {
  width: 100%;
  padding: 16px 22px;
  border-radius: 20px;
  border: none;
  background: var(--color-text-light);

  font-size: 18px;
  font-weight: 600;
  color: var(--color-primary);

  box-shadow: 0 4px 12px rgba(0,0,0,0.12);

  transition: box-shadow 0.25s ease, transform 0.1s ease;
}

.search-input::placeholder {
  color: rgba(12, 43, 78, 0.4); /* soft version of primary */
}

.search-input:focus {
  outline: none;
  box-shadow: 0 0 0 4px rgba(255, 205, 201, 0.5);
  transform: scale(1.01);
}
</style>
>
