<script setup>
const props = defineProps({
  node: Object,
  letter: String
});
</script>

<template>
  <div class="node-container">

    <!-- node bubble -->
    <div 
      class="node-bubble"
      :class="{ 'node-end': node.is_end }"
    >
      <!-- Node Character -->
      <div class="node-letter">
        {{ letter }}
      </div>

      <!-- Full term if terminal -->
      <div v-if="node.term" class="node-term">
        {{ node.term }}
      </div>

      <!-- Frequency -->
      <div class="node-frequency">
        freq: {{ node.frequency }}
      </div>
    </div>

    <!-- Children -->
    <div 
      v-if="Object.keys(node.children).length"
      class="children-container"
    >
      <!-- Vertical line from parent to group -->
      <div class="connector-vertical"></div>

      <div class="children-row">
        <div 
          v-for="(child, ch) in node.children"
          :key="ch"
          class="child-wrapper"
        >
          <!-- horizontal line to child -->
          <div class="connector-horizontal"></div>

          <TrieNode :node="child" :letter="ch" />
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>

/* smooth animation for all elements */
.node-container,
.node-bubble,
.child-wrapper,
.children-container {
  transition: all 0.25s ease;
}

/* overall wrapper */
.node-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 28px;
}

/* main bubble */
.node-bubble {
  padding: 8px 10px;        /* smaller padding */
  min-width: 60px;          /* smaller width */
  
  background: white;
  border-radius: 12px;
  border: 1px solid #d7dce3;

  box-shadow: 0 4px 10px rgba(0,0,0,0.06);

  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;

  transform: scale(1);
}


.node-bubble:hover {
  transform: scale(1.04);
}

/* highlight terminal nodes */
.node-end {
  background: var(--color-accent);
  border-color: var(--color-secondary);
}

/* Letter inside bubble */
.node-letter {
  font-size: 26px;
  font-weight: 700;
  color: var(--color-primary);
}

/* The term (for end nodes only) */
.node-term {
  margin-top: 4px;
  font-size: 14px;
  font-weight: 700;
  color: var(--color-secondary);
}

/* frequency label */
.node-frequency {
  margin-top: 3px;
  font-size: 11px;
  color: #4a5568;
}

/* ====================================== */
/* CHILDREN STRUCTURE                     */
/* ====================================== */

.node-container {
  margin-bottom: 10px; /* much tighter */
}


.children-row {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 4px;
}

.child-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* connectors */
.connector-vertical {
  width: 2px;
  height: 8px;
  background: #cbd5e1;
  margin: 0 auto;
}

.connector-horizontal {
  width: 40px;
  height: 2px;
  background: #cbd5e1;
  margin-bottom: 8px;
}
</style>
