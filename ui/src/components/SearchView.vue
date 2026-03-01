<script setup>
import { ref, computed } from 'vue'

const query = ref('')
const apiOnly = ref(false)
const searching = ref(false)
const results = ref([])
const progress = ref({ completed: 0, total: 0 })
const summary = ref(null)
const error = ref(null)

let eventSource = null

const found = computed(() => results.value.filter(r => r.status === 'FOUND'))
const likely = computed(() => results.value.filter(r => r.status === 'LIKELY'))
const notFound = computed(() => results.value.filter(r => r.status === 'NOT_FOUND'))
const errors = computed(() => results.value.filter(r => r.status === 'ERROR' || r.status === 'SKIPPED'))

function startSearch() {
  if (!query.value.trim() || searching.value) return

  // Reset state
  results.value = []
  progress.value = { completed: 0, total: 0 }
  summary.value = null
  error.value = null
  searching.value = true

  const params = new URLSearchParams({ q: query.value.trim() })
  if (apiOnly.value) params.set('api_only', 'true')

  eventSource = new EventSource(`/api/search?${params}`)

  eventSource.addEventListener('search:start', (e) => {
    const data = JSON.parse(e.data)
    progress.value = { completed: 0, total: data.total_marketplaces }
  })

  eventSource.addEventListener('search:result', (e) => {
    const data = JSON.parse(e.data)
    results.value.push(data)
    if (data.progress) {
      progress.value = data.progress
    }
  })

  eventSource.addEventListener('search:complete', (e) => {
    const data = JSON.parse(e.data)
    summary.value = data
    searching.value = false
    eventSource.close()
    eventSource = null
  })

  eventSource.onerror = () => {
    if (searching.value) {
      error.value = 'Connection lost. The search may still be running on the server.'
      searching.value = false
    }
    if (eventSource) {
      eventSource.close()
      eventSource = null
    }
  }
}

function handleKeydown(e) {
  if (e.key === 'Enter') startSearch()
}
</script>

<template>
  <div class="search-view">
    <!-- Search bar -->
    <div class="search-bar">
      <input
        v-model="query"
        type="text"
        placeholder="Search 15 data marketplaces..."
        @keydown="handleKeydown"
        :disabled="searching"
        class="search-input"
      />
      <label class="api-only-label">
        <input type="checkbox" v-model="apiOnly" :disabled="searching" />
        API only
      </label>
      <button @click="startSearch" :disabled="searching || !query.trim()" class="search-btn">
        {{ searching ? 'Searching...' : 'Search' }}
      </button>
    </div>

    <!-- Progress bar -->
    <div v-if="searching || progress.total > 0" class="progress-section">
      <div class="progress-bar">
        <div
          class="progress-fill"
          :style="{ width: progress.total ? (progress.completed / progress.total * 100) + '%' : '0%' }"
          :class="{ animating: searching }"
        ></div>
      </div>
      <span class="progress-text">{{ progress.completed }} / {{ progress.total }} marketplaces</span>
    </div>

    <!-- Error -->
    <div v-if="error" class="error-banner">{{ error }}</div>

    <!-- Results -->
    <div v-if="results.length > 0" class="results">

      <!-- Found -->
      <div v-if="found.length" class="result-group">
        <h3 class="group-header found-header">Found</h3>
        <div v-for="r in found" :key="r.marketplace" class="result-card">
          <div class="card-header">
            <span class="marketplace-name">{{ r.marketplace }}</span>
            <span class="hit-count">{{ r.hits }} result{{ r.hits !== 1 ? 's' : '' }}</span>
            <span class="elapsed">{{ r.elapsed_seconds }}s</span>
          </div>
          <table v-if="r.matches && r.matches.length" class="matches-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Dataset</th>
                <th v-if="r.matches.some(m => m.pricing)">Pricing</th>
                <th>Link</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(m, i) in r.matches" :key="i">
                <td>{{ i + 1 }}</td>
                <td class="match-title">{{ m.title }}</td>
                <td v-if="r.matches.some(m2 => m2.pricing)">{{ m.pricing || '—' }}</td>
                <td><a v-if="m.url" :href="m.url" target="_blank" rel="noopener">View</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Likely -->
      <div v-if="likely.length" class="result-group">
        <h3 class="group-header likely-header">Likely</h3>
        <div v-for="r in likely" :key="r.marketplace" class="result-card">
          <div class="card-header">
            <span class="marketplace-name">{{ r.marketplace }}</span>
            <span class="hit-count">{{ r.hits }} result{{ r.hits !== 1 ? 's' : '' }}</span>
            <span class="elapsed">{{ r.elapsed_seconds }}s</span>
          </div>
          <table v-if="r.matches && r.matches.length" class="matches-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Dataset</th>
                <th v-if="r.matches.some(m => m.pricing)">Pricing</th>
                <th>Link</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(m, i) in r.matches" :key="i">
                <td>{{ i + 1 }}</td>
                <td class="match-title">{{ m.title }}</td>
                <td v-if="r.matches.some(m2 => m2.pricing)">{{ m.pricing || '—' }}</td>
                <td><a v-if="m.url" :href="m.url" target="_blank" rel="noopener">View</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Not Found -->
      <div v-if="notFound.length" class="result-group">
        <h3 class="group-header notfound-header">Not Found</h3>
        <div class="not-found-list">
          <span v-for="r in notFound" :key="r.marketplace" class="not-found-item">{{ r.marketplace }}</span>
        </div>
      </div>

      <!-- Errors -->
      <div v-if="errors.length" class="result-group">
        <h3 class="group-header error-header">Errors / Skipped</h3>
        <div v-for="r in errors" :key="r.marketplace" class="error-item">
          <span class="marketplace-name">{{ r.marketplace }}</span>
          <span class="error-msg">{{ r.error }}</span>
        </div>
      </div>
    </div>

    <!-- Summary banner -->
    <div v-if="summary" class="summary-banner">
      Searched {{ progress.total }} marketplaces in {{ summary.elapsed_seconds }}s
      — {{ summary.total_results }} total results
      <span class="report-path">Report: {{ summary.report_path }}</span>
    </div>

    <!-- Empty state -->
    <div v-if="!searching && results.length === 0 && !error" class="empty-state">
      Type a query to search across Kaggle, Hugging Face, AWS Data Exchange, Snowflake, and 11 more marketplaces.
    </div>
  </div>
</template>

<style scoped>
.search-view {
  padding: 2rem;
  max-width: 960px;
  margin: 0 auto;
}

.search-bar {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  margin-bottom: 1.5rem;
}

.search-input {
  flex: 1;
  padding: 0.7rem 1rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg-surface);
  color: var(--text);
  font-size: 1rem;
  outline: none;
  transition: border-color 0.15s;
}

.search-input:focus {
  border-color: var(--accent);
}

.search-input:disabled {
  opacity: 0.6;
}

.api-only-label {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  color: var(--text-muted);
  font-size: 0.85rem;
  white-space: nowrap;
  cursor: pointer;
}

.search-btn {
  padding: 0.7rem 1.5rem;
  border: none;
  border-radius: 6px;
  background: var(--accent);
  color: #1a1a2e;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: opacity 0.15s;
}

.search-btn:hover:not(:disabled) {
  opacity: 0.85;
}

.search-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Progress */
.progress-section {
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.progress-bar {
  flex: 1;
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--accent);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.progress-fill.animating {
  background: linear-gradient(90deg, var(--accent), #7dd3fc, var(--accent));
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.progress-text {
  color: var(--text-muted);
  font-size: 0.85rem;
  white-space: nowrap;
}

/* Results */
.results {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.result-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.group-header {
  font-size: 1rem;
  font-weight: 600;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
  display: inline-block;
  width: fit-content;
}

.found-header { color: #4ade80; border-left: 3px solid #4ade80; }
.likely-header { color: #facc15; border-left: 3px solid #facc15; }
.notfound-header { color: var(--text-muted); border-left: 3px solid var(--text-muted); }
.error-header { color: #f87171; border-left: 3px solid #f87171; }

.result-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.marketplace-name {
  font-weight: 600;
  color: var(--text);
}

.hit-count {
  color: var(--accent);
  font-size: 0.85rem;
}

.elapsed {
  color: var(--text-muted);
  font-size: 0.8rem;
  margin-left: auto;
}

.matches-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.matches-table th {
  text-align: left;
  padding: 0.4rem 0.6rem;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border);
  font-weight: 500;
}

.matches-table td {
  padding: 0.4rem 0.6rem;
  border-bottom: 1px solid rgba(37, 53, 84, 0.5);
}

.match-title {
  max-width: 400px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.matches-table a {
  color: var(--accent);
  text-decoration: none;
}

.matches-table a:hover {
  text-decoration: underline;
}

/* Not found */
.not-found-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.not-found-item {
  padding: 0.3rem 0.7rem;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 4px;
  color: var(--text-muted);
  font-size: 0.85rem;
}

/* Errors */
.error-item {
  display: flex;
  gap: 0.75rem;
  align-items: baseline;
  padding: 0.4rem 0;
}

.error-msg {
  color: #f87171;
  font-size: 0.85rem;
}

/* Summary */
.summary-banner {
  margin-top: 1.5rem;
  padding: 1rem;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--accent);
  font-weight: 500;
}

.report-path {
  display: block;
  margin-top: 0.3rem;
  color: var(--text-muted);
  font-size: 0.85rem;
  font-weight: 400;
}

/* Error banner */
.error-banner {
  padding: 0.75rem 1rem;
  background: rgba(248, 113, 113, 0.1);
  border: 1px solid #f87171;
  border-radius: 6px;
  color: #f87171;
  margin-bottom: 1rem;
}

/* Empty state */
.empty-state {
  text-align: center;
  color: var(--text-muted);
  padding: 4rem 2rem;
  font-size: 1.05rem;
  line-height: 1.6;
}
</style>
