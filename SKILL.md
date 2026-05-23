---
name: obsidian-content-flywheel
description: |
  Turn saved links, transcripts, podcasts, videos, newsletters, X/Twitter threads, Xiaohongshu posts, web articles, and rough notes into a sustainable Obsidian-based content output system. Use this skill whenever the user wants to end bookmark-hoarding, process a pile of saved materials, build an AI content workflow, connect notes in Obsidian, extract topic ideas from sources, or repurpose one insight into X/Twitter, Xiaohongshu, newsletter, WeChat, short-video, or podcast drafts.
---

# Obsidian Content Flywheel

This skill turns fragmented content consumption into a reusable content production loop:

1. Clean raw material.
2. Extract knowledge atoms into a four-dimensional matrix.
3. Link new atoms to the user's Obsidian vault.
4. Generate topic seeds from collisions between old and new notes.
5. Recompose one idea into platform-specific COPE drafts.

The goal is not generic summarization. The goal is to convert saved material into a living content system that preserves source evidence, creates usable ideas, and makes repeated publishing easier.

## Operating Principles

- Keep source grounding visible. Do not invent facts, quotes, numbers, or links.
- Remove noise aggressively, but preserve claims, examples, data, mechanisms, and memorable phrasing.
- Treat Obsidian as a thinking graph, not a folder archive. Link ideas by mechanism, case, audience pain, platform fit, and reusable framework.
- Produce drafts only after extracting atoms and linking context. Output without context becomes disposable content.
- Leave aesthetic judgment, final positioning, and personal taste to the creator. The AI handles cleaning, decomposition, retrieval, and format recomposition.

## Inputs

Accept any of these:

- A raw transcript from video, podcast, meeting, or voice note
- A web article, newsletter, report, or long-form essay
- X/Twitter thread text
- Xiaohongshu copy, comments, or screenshot transcription
- A list of saved links with notes
- Existing Obsidian notes
- A topic direction plus a source folder

If the user provides only links and no accessible text, fetch or ask for text depending on available tools and permissions. If source access is unavailable, create a source-intake checklist instead of pretending to have read it.

## Required Output Modes

Pick the smallest output mode that satisfies the user's request:

- **Intake mode:** cleaned source note only.
- **Matrix mode:** cleaned source note plus four-dimensional knowledge matrix.
- **Graph mode:** matrix plus Obsidian backlink/link suggestions.
- **Topic mode:** graph plus topic seed bank.
- **COPE mode:** topic seed plus multi-platform drafts.
- **System mode:** create or update vault folders, templates, and workflow docs.

When the user asks to "build the system", use System mode first, then create sample outputs only if source material is available.

## Vault Detection

Before writing files:

1. Look for an obvious Obsidian vault in the current workspace.
2. Prefer existing folders named like `AI内容管理系统`, `内容管理系统`, `Obsidian`, or folders containing `.obsidian`.
3. If a vault exists, reuse its structure.
4. If no vault exists, create a local output folder such as `content-flywheel-output/`.
5. Do not reorganize the user's existing vault unless explicitly asked.

Suggested default folder mapping:

| Purpose | Existing vault target | Generic target |
|---|---|---|
| Cleaned source | `02_输入库/` | `01_Inbox/` |
| Knowledge atoms | `02_知识原子/` or `05_素材生产/` | `02_Knowledge_Atoms/` |
| Topic seeds | `03_选题池/` | `03_Topic_Seeds/` |
| COPE drafts | `04_内容生产/` | `04_COPE_Drafts/` |
| Templates | `99_模板/` | `99_Templates/` |
| Workflow docs | `08_AI工作流/` | `00_Workflow/` |

## Workflow

### Phase 1: Source Intake And Cleaning

Convert raw material into a clean source note.

Keep:

- Main claims
- Concrete examples and cases
- Data, numbers, named entities, dates, and causal relationships
- Memorable lines that can become hooks
- Steps, models, and frameworks
- Audience pain points and objections

Remove:

- Filler words and repeated transitions
- Sponsor messages and CTA clutter
- Politeness padding
- Redundant setup
- Pure vibe statements without informational value

Create a source note using `templates/source-note.md`.

### Phase 2: Four-Dimensional Knowledge Matrix

Extract knowledge atoms into exactly these four dimensions:

1. **Counterintuitive insight:** What breaks common belief?
2. **Emotional anchor:** What case, sentence, conflict, or pain point creates resonance?
3. **Method framework:** What can become a repeatable model, checklist, or step-by-step process?
4. **Underlying logic:** What economic, psychological, technical, social, or operational mechanism explains the phenomenon?

For each atom, include:

- Atom title
- Dimension
- Source evidence
- Why it matters
- Usable content sentence
- Link candidates
- Confidence: high, medium, or low

Use `templates/knowledge-matrix.md`.

### Phase 3: Obsidian Graph Linking

Search existing notes before creating links. Prefer `rg` for local search.

Link by:

- Same audience pain
- Same mechanism
- Same case type
- Same business or creator problem
- Same tool/workflow
- Opposite viewpoint
- Follow-up question

Add Obsidian wiki links in a `Related notes` section:

```markdown
## Related notes
- [[Existing Note]] - why this connects
```

Do not create noisy links just because keywords match. A useful link must explain a content collision or retrieval path.

### Phase 4: Topic Seed Generation

A topic seed is not a title. It is a publishable argument waiting for a format.

For each seed, include:

- One-sentence thesis
- Why now
- Audience pain
- Source atoms used
- Existing notes linked
- Platform fit
- Required proof or example
- Risk: what would make this shallow, wrong, or boring

Use `templates/topic-seed.md`.

### Phase 5: COPE Recomposition

COPE means "Create Once, Publish Everywhere". Recompose one topic into different formats without flattening the idea.

Produce only the formats the user asks for, or default to these three:

1. **Instant media:** X/Twitter or Xiaohongshu
   - Use counterintuitive insight plus emotional anchor.
   - Keep it hook-first, readable, and easy to save.
2. **Depth media:** Newsletter, WeChat, blog, or long-form essay
   - Use method framework plus underlying logic.
   - Pull in linked cases from the vault.
3. **Dynamic media:** Short video, long video, or podcast
   - Use this structure: golden 3-second opening, pain expansion, core intervention, proof/example, call to action.

Use `templates/cope-draft.md`.

## Platform Rules

Read `references/platform-rules.md` when producing platform drafts.

Default platform behavior:

- X/Twitter: one sharp idea, clean rhythm, no excessive formatting.
- Xiaohongshu: high-density hook, save-worthy structure, scannable sections.
- Newsletter/WeChat: thesis-driven long logic, examples, objections, and implications.
- Short video: spoken language, fast opening, one conflict, one intervention.
- Podcast: conversational arc, richer context, fewer visual dependencies.

## File Naming

Use readable filenames:

```text
YYYY-MM-DD_来源_主题.md
YYYY-MM-DD_知识矩阵_主题.md
YYYY-MM-DD_选题种子_主题.md
YYYY-MM-DD_COPE_主题.md
```

Avoid special characters that break shell scripts. For Chinese titles, keep filenames short and put the full title in the note.

## Quality Bar

Before finalizing, check:

- Every factual claim traces back to source material or is marked as inference.
- The four matrix dimensions are not empty or repetitive.
- Obsidian links have reasons, not just keyword matches.
- Topic seeds contain a real argument, not a generic theme.
- Platform drafts differ structurally rather than being the same text with minor formatting changes.
- The final output gives the creator a next action: publish, research, record, link, or discard.

## Optional Scaffold Script

If the user wants a fresh vault structure, use:

```bash
python scripts/scaffold_vault.py /path/to/vault
```

This creates folders and copies templates into the vault. Do not run it against an existing production vault without checking what it will create.

