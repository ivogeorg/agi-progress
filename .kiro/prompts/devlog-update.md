---
description: "Update development log after feature completion"
---

# DevLog Update

## Role
You are a technical writer documenting development progress.

## When to Run
- After `@execute` completes a feature (canonical usage)
- Before switching sessions (to preserve context)
- After significant non-feature work (infrastructure, workflow fixes)

## Process

### 1. Check if an Entry is Warranted

```bash
# Last DEVLOG entry date and title
grep -E "^## \[" .kiro/DEVLOG.md | head -1

# Commits since last entry
last_date=$(grep -E "^## \[" .kiro/DEVLOG.md | head -1 | sed 's/## \[\(.*\)\].*/\1/')
git log --since="$last_date" --oneline --no-merges

# Files changed since last entry
git diff --stat $(git log --since="$last_date" --format="%H" | tail -1)..HEAD 2>/dev/null
```

**If there are no commits and no meaningful changes since the last entry**, tell the user:

```
ℹ️ No significant changes since last entry ([date] - [title]).
   Skipping DEVLOG update to avoid clutter.
```

Stop here. Do not create an empty or trivial entry.

### 2. Gather Context

- Read recently completed feature specs from `.kiro/features/` (check `completed_date`)
- Review git commits and change stats from step 1
- Note the current branch

### 3. Draft the Entry

Use the template from `.kiro/documentation/templates/devlog-entry-template.md`.

**Writing guidelines — keep it tight:**
- Objective: 1-2 sentences max
- Work Completed: 3-5 bullets, each one line plus an optional metric/detail line
- Key Decisions: only architectural/strategic choices, not every small call
- Learnings: genuinely reusable insights, not restatements of what was done
- Challenges/Blockers: only if significant; omit the section entirely if none
- Resources: only if actually referenced during work
- Next Steps: 2-4 items, link feature IDs
- Artifacts: files, commits — no prose

**Tone:** factual, scannable, no filler. A reader skimming 10 entries in a row should be able to extract the key facts from each in under 30 seconds.

### 4. Present for Review

Show the draft to the user:

```
📝 DEVLOG DRAFT

[full entry]

Accept? (yes / edit / regenerate)
```

If edit: apply the user's changes. If regenerate: ask what to change and redo.

### 5. Write the Entry and Update TOC

1. Insert the approved entry into `.kiro/DEVLOG.md` after the TOC block and `---` separator, before the first existing `## [` entry.

2. Add a TOC link for the new entry. The TOC lives between the header and the first `---` separator, formatted as:

```markdown
## Table of Contents
- [YYYY-MM-DD - Title](#yyyy-mm-dd---title-slug)
- [YYYY-MM-DD - Title](#yyyy-mm-dd---title-slug)
...
```

The anchor slug is the `## [YYYY-MM-DD] - Title` heading converted to a markdown anchor: lowercase, spaces to hyphens, strip `[]` and special characters. New entries go at the top of the TOC list.

3. Confirm:

```
✅ DEVLOG UPDATED

Entry: [date] - [title]
Feature: [feature-id] (if applicable)
```
