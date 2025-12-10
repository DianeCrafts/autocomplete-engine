<template>
  <div class="app-root">

    <!-- TOP MAIN UI CONTAINER -->
    <div class="app-container">
      <h1 class="app-title">Autocomplete Engine</h1>

      <SearchBar @suggestions="suggestions = $event" />

      <transition name="suggestions">
        <SuggestionList
          v-if="suggestions.length > 0"
          :suggestions="suggestions"
          @selected="handleSelect"
        />
      </transition>

      <button class="debug-btn" @click="debugStore.toggle()">
        {{ debugStore.enabled ? "Hide Engine Internals" : "Show Engine Internals" }}
      </button>
    </div>

    <!-- NEW DEBUG CONTAINER BELOW THE MAIN BOX -->
    <div 
      v-if="debugStore.enabled && debugStore.debug" 
      class="debug-container"
      >
      <DebugPanel />
    </div>


  </div>
</template>

<script setup>
import { ref } from "vue";
import SearchBar from "./components/SearchBar.vue";
import SuggestionList from "./components/SuggestionList.vue";
import DebugPanel from "./components/DebugPanel.vue";
import { debugStore } from "./store/debugStore.js";
import { logSelection } from "./services/api";

const suggestions = ref([]);

function handleSelect(term) {
  logSelection(term);
}
</script>
<style scoped>
/* ============================= */
/* APP LAYOUT                    */
/* ============================= */

.app-root {
  min-height: 100vh;
  width: 100%;
  background: var(--color-primary);
  display: flex;
  flex-direction: column; /* <-- stack vertically */
  align-items: center;    /* center horizontally */
  padding-top: 60px;
}

.app-container {
  width: 90%;
  max-width: 700px;
  background: var(--color-light);
  border-radius: 24px;
  padding: 40px 50px;
  /* box-shadow: 0 20px 40px rgba(0,0,0,0.25); */
  display: flex;
  flex-direction: column;
  gap: 26px;
}

/* ============================= */
/* TITLE                         */
/* ============================= */

.app-title {
  text-align: center;
  font-size: 36px;
  font-weight: 800;
  color: var(--color-primary);
  margin-bottom: 10px;
}


/* ============================= */
/* DEBUG BUTTON                  */
/* ============================= */

.debug-btn {
  background: var(--color-accent);
  color: var(--color-primary);
  padding: 12px 24px;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  font-size: 15px;
  font-weight: 700;

  align-self: center;

  transition: background 0.2s ease, transform 0.1s ease;
}

.debug-btn:hover {
  background: #ffb1ac;
}

.debug-btn:active {
  transform: scale(0.97);
}

/* ============================= */
/* SUGGESTION LIST TRANSITION    */
/* ============================= */

.suggestions-enter-from {
  opacity: 0;
  transform: translateY(-6px);
  max-height: 0;
}

.suggestions-enter-active {
  transition: all 0.25s ease;
}

.suggestions-enter-to {
  opacity: 1;
  transform: translateY(0);
  max-height: 500px;
}

.suggestions-leave-from {
  opacity: 1;
  transform: translateY(0);
  max-height: 500px;
}

.suggestions-leave-active {
  transition: all 0.25s ease;
}

.suggestions-leave-to {
  opacity: 0;
  transform: translateY(-6px);
  max-height: 0;
}


/* ============================= */
/* DEBUG CONTAINER (SEPARATE BOX) */
/* ============================= */

.debug-container {
  width: 90%;
  max-width: 1200px;

  margin-top: 30px;
  padding: 30px;

  background: var(--color-light);
  border-radius: 22px;
  box-shadow: 0 14px 40px rgba(0,0,0,0.18);

  display: flex;
  flex-direction: column;
  gap: 20px;
  animation: fadeIn 0.25s ease-out;
}

/* fade animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-6px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


</style>
