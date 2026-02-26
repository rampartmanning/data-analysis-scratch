<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  topic: Object,
})

const data = ref(null)
const loading = ref(false)

watch(
  () => props.topic,
  async (t) => {
    if (!t) return
    loading.value = true
    try {
      const res = await fetch(`./data/${t.filename}`)
      data.value = await res.json()
    } catch {
      data.value = null
    } finally {
      loading.value = false
    }
  },
  { immediate: true }
)
</script>

<template>
  <div v-if="loading" class="status">Loading findings...</div>
  <div v-else-if="!data" class="status muted">Failed to load data.</div>
  <div v-else class="topic-view">
    <h2>{{ data.topic }}</h2>
    <p class="meta">Generated: {{ new Date(data.generated_at).toLocaleString() }}</p>

    <div v-if="data.metadata && Object.keys(data.metadata).length" class="meta-box">
      <div v-for="(val, key) in data.metadata" :key="key" class="meta-item">
        <span class="meta-key">{{ key }}:</span> {{ val }}
      </div>
    </div>

    <div class="findings">
      <div v-for="(f, i) in data.findings" :key="i" class="finding-card">
        <h3 v-if="f.title">{{ f.title }}</h3>
        <p v-if="f.summary" class="summary">{{ f.summary }}</p>
        <div v-if="f.details" class="details">{{ f.details }}</div>
        <a v-if="f.url" :href="f.url" target="_blank" class="source-link">{{ f.url }}</a>
        <div v-if="f.tags" class="tags">
          <span v-for="tag in f.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.topic-view h2 {
  color: var(--accent);
  margin-bottom: 0.3rem;
}

.meta {
  color: var(--text-muted);
  font-size: 0.85rem;
  margin-bottom: 1.5rem;
}

.meta-box {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.8rem 1.2rem;
  margin-bottom: 1.5rem;
}

.meta-item {
  font-size: 0.9rem;
}

.meta-key {
  color: var(--accent);
  font-weight: 600;
}

.findings {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.finding-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.2rem 1.5rem;
}

.finding-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
}

.summary {
  margin-bottom: 0.5rem;
}

.details {
  font-size: 0.9rem;
  color: var(--text-muted);
  white-space: pre-wrap;
  margin-bottom: 0.5rem;
}

.source-link {
  color: var(--accent);
  font-size: 0.85rem;
  text-decoration: none;
  word-break: break-all;
}

.source-link:hover {
  text-decoration: underline;
}

.tags {
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin-top: 0.6rem;
}

.tag {
  background: rgba(83, 199, 240, 0.15);
  color: var(--accent);
  font-size: 0.75rem;
  padding: 0.15rem 0.6rem;
  border-radius: 12px;
}
</style>
