# Hugging Face Datasets — Categories

**URL**: https://huggingface.co/datasets
**Scraped**: 2026-02-26
**Total Datasets on Hub**: ~881,543

---

## Category Taxonomy

Hugging Face organizes datasets across multiple independent filter dimensions. The primary taxonomy axis is **Task Categories**, but datasets are also filterable by modality, format, language, license, library compatibility, size, and evaluation status. Each dataset card uses YAML frontmatter metadata to declare its categories.

### 1. Task Categories

The canonical `task_categories` field in dataset card metadata. Organized into six top-level groups in the UI:

#### Multimodal
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `image-text-to-text` | Image-Text-to-Text | 12 |
| `image-text-to-image` | Image-Text-to-Image | 1 |
| `image-text-to-video` | Image-Text-to-Video | 0 |
| `visual-question-answering` | Visual Question Answering | 57 |
| `video-text-to-text` | Video-Text-to-Text | 3 |
| `visual-document-retrieval` | Visual Document Retrieval | 6 |
| `any-to-any` | Any-to-Any | 4 |

#### Computer Vision
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `depth-estimation` | Depth Estimation | 18 |
| `image-classification` | Image Classification | 251 |
| `object-detection` | Object Detection | 250 |
| `image-segmentation` | Image Segmentation | 60 |
| `text-to-image` | Text-to-Image | 196 |
| `image-to-text` | Image-to-Text | 59 |
| `image-to-image` | Image-to-Image | 55 |
| `image-to-video` | Image-to-Video | 15 |
| `unconditional-image-generation` | Unconditional Image Generation | 0 |
| `video-classification` | Video Classification | 5 |
| `text-to-video` | Text-to-Video | 146 |
| `zero-shot-image-classification` | Zero-Shot Image Classification | 0 |
| `mask-generation` | Mask Generation | 1 |
| `zero-shot-object-detection` | Zero-Shot Object Detection | 0 |
| `text-to-3d` | Text-to-3D | 8 |
| `image-to-3d` | Image-to-3D | 8 |
| `image-feature-extraction` | Image Feature Extraction | 0 |

#### Natural Language Processing
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `text-classification` | Text Classification | 322 |
| `token-classification` | Token Classification | 25 |
| `table-question-answering` | Table Question Answering | 12 |
| `question-answering` | Question Answering | 445 |
| `zero-shot-classification` | Zero-Shot Classification | 4 |
| `translation` | Translation | 435 |
| `summarization` | Summarization | 121 |
| `feature-extraction` | Feature Extraction | 12 |
| `text-generation` | Text Generation | 217 |
| `fill-mask` | Fill-Mask | 2 |
| `sentence-similarity` | Sentence Similarity | 16 |
| `table-to-text` | Table to Text | 1 |
| `multiple-choice` | Multiple Choice | 67 |
| `text-ranking` | Text Ranking | 10 |
| `text-retrieval` | Text Retrieval | 569 |

#### Audio
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `text-to-speech` | Text-to-Speech | 78 |
| `text-to-audio` | Text-to-Audio | 10 |
| `automatic-speech-recognition` | Automatic Speech Recognition | 64 |
| `audio-to-audio` | Audio-to-Audio | 2 |
| `audio-classification` | Audio Classification | 12 |
| `voice-activity-detection` | Voice Activity Detection | 10 |

#### Tabular
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `tabular-classification` | Tabular Classification | 7 |
| `tabular-regression` | Tabular Regression | 10 |
| `tabular-to-text` | Tabular to Text | 0 |
| `time-series-forecasting` | Time Series Forecasting | 3 |

#### Reinforcement Learning
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `reinforcement-learning` | Reinforcement Learning | 434 |
| `robotics` | Robotics | 1,281 |

#### Other
| Task Category (slug) | Display Name | Dataset Count |
|---|---|---|
| `graph-ml` | Graph Machine Learning | 8 |

**Total distinct task categories: 44**

---

### 2. Modalities

Auto-detected from file contents, or forced via `tags` in metadata. These are separate from task categories.

| Modality | Slug |
|---|---|
| 3D | `3d` |
| Audio | `audio` |
| Document | `document` |
| Geospatial | `geospatial` |
| Image | `image` |
| Tabular | `tabular` |
| Text | `text` |
| Time-series | `timeseries` |
| Video | `video` |

---

### 3. File Formats

| Format |
|---|
| `json` |
| `csv` |
| `parquet` |
| `optimized-parquet` |
| `imagefolder` |
| `soundfolder` |
| `webdataset` |
| `text` |
| `arrow` |

---

### 4. Compatible Libraries

Libraries that can natively load the dataset. Auto-detected or manually tagged.

| Library |
|---|
| Datasets (HuggingFace `datasets`) |
| Croissant (`mlcroissant`) |
| Polars |
| pandas |
| Dask |
| WebDataset |
| Distilabel |
| Argilla |
| FiftyOne |
| NeMo Data Designer |
| Lance |

---

### 5. Languages

Datasets are tagged with ISO 639-1 language codes. The Hub lists 8,131+ languages total. The top languages displayed in the UI filter (in order):

1. English (en)
2. French (fr)
3. Chinese (zh)
4. Spanish (es)
5. Russian (ru)
6. Japanese (ja)
7. German (de)
8. Arabic (ar)
9. Korean (ko)
10. Portuguese (pt)
11. Italian (it)
12. Vietnamese (vi)
13. Turkish (tr)
14. Hindi (hi)
15. Indonesian (id)
16. Dutch (nl)
17. Polish (pl)
18. Persian (fa)
19. Thai (th)
20. Bengali (bn)
21. Czech (cs)
22. Swedish (sv)
23. Tamil (ta)
24. Romanian (ro)
25. Ukrainian (uk)
26. Catalan (ca)
27. Finnish (fi)
28. Greek (el)
29. Danish (da)
30. Hungarian (hu)
31. Telugu (te)
32. Urdu (ur)
33. Bulgarian (bg)
34. Basque (eu)
35. Marathi (mr)
36. Hebrew (he)
37. Estonian (et)
38. Swahili (sw)
39. Slovak (sk)
40. Malayalam (ml)
41. Slovenian (sl)
42. Lithuanian (lt)
43. Malay (ms)
44. Croatian (hr)
45. Gujarati (gu)
46. Latvian (lv)
47. Kannada (kn)
48. Serbian (sr)
49. Amharic (am)
50. Norwegian (no)
51. Panjabi (pa)
52. Kazakh (kk)
53. Burmese (my)
54. Nepali (ne)
55. Azerbaijani (az)
56. Afrikaans (af)
57. Icelandic (is)
58. Breton (br)
59. Code (code)
60. Hausa (ha)
61. Yoruba (yo)
62. Irish (ga)
63. Oriya (or)
64. Galician (gl)
65. Maltese (mt)
66. Assamese (as)
67. Sinhala (si)
68. Latin (la)
69. Uzbek (uz)
70. Khmer (km)
71. Welsh (cy)
72. Tagalog (tl)
73. Macedonian (mk)
74. Albanian (sq)
75. Georgian (ka)
76. Igbo (ig)
77. Armenian (hy)

Plus ~8,054 more languages available in the full filter.

---

### 6. Licenses

Full list of recognized license identifiers for dataset cards:

| Full Name | Identifier |
|---|---|
| Apache License 2.0 | `apache-2.0` |
| MIT | `mit` |
| OpenRAIL license family | `openrail` |
| BigScience OpenRAIL-M | `bigscience-openrail-m` |
| CreativeML OpenRAIL-M | `creativeml-openrail-m` |
| BigScience BLOOM RAIL 1.0 | `bigscience-bloom-rail-1.0` |
| BigCode Open RAIL-M v1 | `bigcode-openrail-m` |
| Academic Free License v3.0 | `afl-3.0` |
| Artistic License 2.0 | `artistic-2.0` |
| Boost Software License 1.0 | `bsl-1.0` |
| BSD license family | `bsd` |
| BSD 2-Clause "Simplified" | `bsd-2-clause` |
| BSD 3-Clause "New"/"Revised" | `bsd-3-clause` |
| BSD 3-Clause Clear | `bsd-3-clause-clear` |
| Computational Use of Data Agreement | `c-uda` |
| Creative Commons family | `cc` |
| CC Zero v1.0 Universal | `cc0-1.0` |
| CC Attribution 2.0 | `cc-by-2.0` |
| CC Attribution 2.5 | `cc-by-2.5` |
| CC Attribution 3.0 | `cc-by-3.0` |
| CC Attribution 4.0 | `cc-by-4.0` |
| CC Attribution Share Alike 3.0 | `cc-by-sa-3.0` |
| CC Attribution Share Alike 4.0 | `cc-by-sa-4.0` |
| CC Attribution Non Commercial 2.0 | `cc-by-nc-2.0` |
| CC Attribution Non Commercial 3.0 | `cc-by-nc-3.0` |
| CC Attribution Non Commercial 4.0 | `cc-by-nc-4.0` |
| CC Attribution No Derivatives 4.0 | `cc-by-nd-4.0` |
| CC Attribution NC ND 3.0 | `cc-by-nc-nd-3.0` |
| CC Attribution NC ND 4.0 | `cc-by-nc-nd-4.0` |
| CC Attribution NC SA 2.0 | `cc-by-nc-sa-2.0` |
| CC Attribution NC SA 3.0 | `cc-by-nc-sa-3.0` |
| CC Attribution NC SA 4.0 | `cc-by-nc-sa-4.0` |
| CDLA Sharing 1.0 | `cdla-sharing-1.0` |
| CDLA Permissive 1.0 | `cdla-permissive-1.0` |
| CDLA Permissive 2.0 | `cdla-permissive-2.0` |
| WTFPL | `wtfpl` |
| Educational Community License v2.0 | `ecl-2.0` |
| Eclipse Public License 1.0 | `epl-1.0` |
| Eclipse Public License 2.0 | `epl-2.0` |
| Etalab Open License 2.0 | `etalab-2.0` |
| EU Public License 1.1 | `eupl-1.1` |
| EU Public License 1.2 | `eupl-1.2` |
| AGPL v3.0 | `agpl-3.0` |
| GNU Free Documentation License family | `gfdl` |
| GPL family | `gpl` |
| GPL v2.0 | `gpl-2.0` |
| GPL v3.0 | `gpl-3.0` |
| LGPL family | `lgpl` |
| LGPL v2.1 | `lgpl-2.1` |
| LGPL v3.0 | `lgpl-3.0` |
| ISC | `isc` |
| H Research License | `h-research` |
| Intel Research Use License | `intel-research` |
| LaTeX Project Public License v1.3c | `lppl-1.3c` |
| Microsoft Public License | `ms-pl` |
| Apple Sample Code License | `apple-ascl` |
| Apple Model License for Research | `apple-amlr` |
| Mozilla Public License 2.0 | `mpl-2.0` |
| ODC Attribution family | `odc-by` |
| Open Database License family | `odbl` |
| Open Model, Data & Weights License 1.0 | `openmdw-1.0` |
| Open Rail++-M License | `openrail++` |
| Open Software License 3.0 | `osl-3.0` |
| PostgreSQL License | `postgresql` |
| SIL Open Font License 1.1 | `ofl-1.1` |
| NCSA Open Source License | `ncsa` |
| The Unlicense | `unlicense` |
| zLib License | `zlib` |
| ODC Public Domain Dedication License | `pddl` |
| LGPL for Linguistic Resources | `lgpl-lr` |
| DeepFloyd IF Research License | `deepfloyd-if-license` |
| FAIR Noncommercial Research License | `fair-noncommercial-research-license` |
| Llama 2 Community License | `llama2` |
| Llama 3 Community License | `llama3` |
| Llama 3.1 Community License | `llama3.1` |
| Llama 3.2 Community License | `llama3.2` |
| Llama 3.3 Community License | `llama3.3` |
| Llama 4 Community License | `llama4` |
| Grok 2 Community License | `grok2-community` |
| Gemma Terms of Use | `gemma` |
| Unknown | `unknown` |
| Other | `other` |

**Total recognized license identifiers: 72**

When using `license: other`, a `LICENSE` file should be included in the repo, and `license_name` should be set.

---

### 7. Size Filter

The Hub provides a row-count range slider for filtering datasets by size. The range spans from `< 1K` rows to `> 1T` rows. The dataset card metadata also supports a `size_categories` field with these standard values:

- `n<1K`
- `1K<n<10K`
- `10K<n<100K`
- `100K<n<1M`
- `1M<n<10M`
- `10M<n<100M`
- `100M<n<1B`
- `1B<n<10B`
- `10B<n<100B`
- `100B<n<1T`
- `n>1T`

---

### 8. Evaluation

| Filter | Description |
|---|---|
| Benchmark | Flags the dataset as a benchmark dataset |

---

### 9. Dataset Card Metadata Fields (YAML Frontmatter)

The complete set of metadata fields supported in dataset card YAML:

| Field | Type | Description |
|---|---|---|
| `language` | list of strings | ISO 639-1 language codes |
| `pretty_name` | string | Human-readable dataset name |
| `tags` | list of strings | Free-form tags (also used for modality, library, arxiv) |
| `license` | string | License identifier from the list above |
| `license_name` | string | Custom license name (when `license: other`) |
| `task_categories` | list of strings | Task categories from the 44-item taxonomy |
| `size_categories` | list of strings | Size range bucket |
| `configs` | object | Data file configurations |

Tags with special semantics:
- Modality tags: `3d`, `audio`, `geospatial`, `image`, `tabular`, `text`, `timeseries`, `video`
- Library tags: `argilla`, `dask`, `datasets`, `distilabel`, `fiftyone`, `mlcroissant`, `pandas`, `webdataset`
- ArXiv tags: `arxiv:XXXX.XXXXX` (auto-extracted from paper links)

---

## Notes

### Taxonomy Structure Observations

1. **Flat taxonomy with UI grouping**: The `task_categories` field is a flat list of 44 slugs. The six top-level groups (Multimodal, Computer Vision, NLP, Audio, Tabular, Reinforcement Learning, Other) exist only in the UI for display purposes -- they are not part of the metadata schema itself.

2. **Sparse tail**: Many task categories have very few or zero datasets (e.g., `unconditional-image-generation`: 0, `zero-shot-image-classification`: 0, `tabular-to-text`: 0, `fill-mask`: 2). The taxonomy represents an aspirational classification rather than a reflection of current content.

3. **Concentration in a few categories**: The most populated categories are Robotics (1,281), Text Retrieval (569), Question Answering (445), Translation (435), Reinforcement Learning (434), Text Classification (322), Image Classification (251), and Object Detection (250). These eight categories account for the majority of categorized datasets.

4. **Most datasets are uncategorized**: With ~881,543 total datasets and only a few thousand across all task categories, the vast majority of datasets do not have `task_categories` metadata set.

5. **Multi-axis filtering**: Filters are independent and combinable. A dataset can have multiple task categories, multiple languages, and multiple modalities simultaneously.

6. **Modalities are auto-detected**: Unlike task categories which require manual metadata, modalities are automatically inferred from file types in the repository (audio files = audio modality, images = image modality, etc.). They can also be forced via tags.

7. **No hierarchical task IDs**: Earlier versions of the Hub supported a `task_ids` field for sub-task classification (e.g., `sentiment-classification` under `text-classification`). This appears to have been deprecated in favor of the flatter `task_categories` system and free-form `tags`.

8. **License taxonomy is extensive**: 72 recognized identifiers covering open source, Creative Commons, research-specific, and model-specific licenses. The `other` option with `license_name` provides escape-hatch extensibility.

9. **Library compatibility is growing**: The list of compatible libraries includes both HuggingFace-native tools (Datasets, Distilabel, Argilla) and third-party data tools (pandas, Polars, Dask, Lance), reflecting the Hub's role as a general-purpose data platform beyond just ML.

10. **Sort options**: Datasets can be sorted by Trending, Most Downloads, Most Likes, and Recently Updated.
