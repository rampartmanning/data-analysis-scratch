<script setup>
import { ref, onMounted } from 'vue'
import TopicView from './components/TopicView.vue'

const topics = ref([])
const selected = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('./data/manifest.json')
    if (!res.ok) {
      topics.value = []
      loading.value = false
      return
    }
    const manifest = await res.json()
    topics.value = manifest.topics || []
  } catch (e) {
    error.value = 'No findings published yet.'
  } finally {
    loading.value = false
  }
})

function selectTopic(t) {
  selected.value = t
}
</script>

<template>
  <div class="app">
    <header>
      <h1>DAS <span class="subtitle">Research Findings</span></h1>
    </header>

    <div v-if="loading" class="status">Loading...</div>
    <div v-else-if="error" class="status muted">{{ error }}</div>
    <div v-else-if="topics.length === 0" class="status muted">
      No findings published yet. Run a research pipeline to generate data.
    </div>

    <div v-else class="layout">
      <nav class="sidebar">
        <ul>
          <li
            v-for="t in topics"
            :key="t.filename"
            :class="{ active: selected?.filename === t.filename }"
            @click="selectTopic(t)"
          >
            {{ t.topic }}
          </li>
        </ul>
      </nav>
      <main class="content">
        <TopicView v-if="selected" :topic="selected" />
        <div v-else class="status muted">Select a topic from the sidebar.</div>
      </main>
    </div>
  </div>
</template>

<style>
:root {
  --bg: #1a1a2e;
  --bg-surface: #16213e;
  --bg-sidebar: #0f3460;
  --text: #e0e0e0;
  --text-muted: #8892a4;
  --accent: #53c7f0;
  --border: #253554;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  line-height: 1.6;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  padding: 1.2rem 2rem;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
}

header h1 {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--accent);
}

header .subtitle {
  color: var(--text-muted);
  font-weight: 400;
  font-size: 1rem;
  margin-left: 0.5rem;
}

.status {
  padding: 3rem;
  text-align: center;
  font-size: 1.1rem;
}

.muted {
  color: var(--text-muted);
}

.layout {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 260px;
  background: var(--bg-sidebar);
  border-right: 1px solid var(--border);
  padding: 1rem 0;
  overflow-y: auto;
}

.sidebar ul {
  list-style: none;
}

.sidebar li {
  padding: 0.7rem 1.4rem;
  cursor: pointer;
  transition: background 0.15s;
  font-size: 0.95rem;
}

.sidebar li:hover {
  background: rgba(83, 199, 240, 0.1);
}

.sidebar li.active {
  background: rgba(83, 199, 240, 0.18);
  color: var(--accent);
  border-left: 3px solid var(--accent);
}

.content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}
</style>
