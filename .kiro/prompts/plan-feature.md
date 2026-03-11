---
description: "Create implementation plan for the next_selected feature"
---

# Plan Feature

## Role
You are a principal software engineer creating an implementation plan.

## Prerequisite
`@next` has been run and exactly one feature has status `"next_selected"` in `.kiro/features.json`.

## Core Principle
We do NOT write implementation code in this phase. We produce a plan file that enables one-pass implementation by `@execute`.

## Process

### 1. Find the Target Feature

```bash
python3 -c "
import json
with open('.kiro/features.json') as f:
    features = json.load(f)['features']
selected = [f for f in features.values() if f.get('status') == 'next_selected']
if not selected:
    print('ERROR: No feature with status next_selected. Run @next first.')
else:
    print(selected[0]['id'])
"
```

If no feature is found, stop and tell the user to run `@next`.

### 2. Read Feature Context

Read the feature spec from `.kiro/features/{feature-id}.md`. This file contains the description, dependencies, implementation guidance, tasks, and validation checklist. This is your primary input.

Also read:
- `.kiro/steering/tech.md` — for tech stack and architecture patterns
- `.kiro/steering/structure.md` — for directory layout and naming conventions
- Any dependency feature specs listed in the feature's `dependencies` field

### 3. Analyze the Codebase

Examine the current codebase for:
- Existing files relevant to this feature (imports, patterns, integration points)
- Files that will need modification
- Testing patterns already in use
- Configuration and build setup

### 4. Research (if needed)

If the feature involves external libraries or APIs:
- Look up current documentation and version compatibility
- Note any known issues or gotchas
- Find relevant code examples

### 5. Create the Plan

Write the plan to `.kiro/plans/{feature-id}-plan.md` using this structure:

```markdown
# Implementation Plan: {Feature Name}

**Feature ID**: {feature-id}
**Created**: {date}
**Feature Spec**: `.kiro/features/{feature-id}.md`

---

## Overview
Brief description of what this plan implements and the approach.

## Context References

### Files to Read Before Implementing
- `path/to/file.py` (lines X-Y) — why this matters

### Files to Create
- `path/to/new_file.py` — purpose

### Files to Modify
- `path/to/existing.py` — what changes and why

### External Documentation
- [Link](url) — what to look for

## Tasks

Execute in order. Each task is atomic.

### Task 1: {ACTION} {target}
- What to do (specific, not generic)
- Pattern to follow (reference existing code)
- Gotchas to avoid
- **Validate**: `command to verify this task`

### Task 2: ...
(continue for all tasks)

## Testing Strategy
What tests to write, what framework, what to cover.

## Validation Commands
Non-interactive commands to verify the feature works end-to-end.

## Acceptance Criteria
- [ ] Measurable criterion 1
- [ ] Measurable criterion 2
```

**⚠️ Plans must contain ONLY non-interactive commands.** No `npm init`, `git commit` without `-m`, or anything that prompts for input.

### 6. Update Feature Status

After writing the plan file:

1. Read `.kiro/features.json`
2. Set the feature's status from `"next_selected"` to `"planned"`
3. Set `"planned_date"` to the current ISO-8601 timestamp (e.g., `"2026-03-09T17:35:00Z"`)
4. Write the updated `.kiro/features.json`

### 7. Report

```
✅ PLAN CREATED: {feature-id}
   Status: planned
   Plan: .kiro/plans/{feature-id}-plan.md

   Next step: run @execute
```
