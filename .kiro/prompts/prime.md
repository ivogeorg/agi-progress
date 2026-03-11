---
description: "Prime for development - injects the project context into the current session"
---

# Prime: Load Project Context

## Role
You are a chief architect and principal software engineer.

## Brief
This is a spec-driven project with a canonical workflow dictated by `@command` prompts in `.kiro/prompts/`. The project is either (A) an established project with completed design, or (B) a blank template needing initial setup. Detect which case applies and follow the corresponding path.

## Step 1: Detect Project State

```bash
if [ -f ".kiro/features.json" ]; then
  echo "ESTABLISHED_PROJECT"
else
  echo "BLANK_TEMPLATE"
fi
```

- If `ESTABLISHED_PROJECT` → follow **Path A** below
- If `BLANK_TEMPLATE` → follow **Path B** below

---

## Path A: Established Project (load context, produce report)

### A1. Analyze Project Structure
```bash
git branch --show-current
tree -L 3 -I 'node_modules|__pycache__|.git|dist|build'
```

### A2. Read Core Documentation
Read the steering documents (highest authority for project intent):
- `.kiro/steering/product.md` — product overview, chief statement of intent
- `.kiro/steering/structure.md` — directory structure, naming conventions
- `.kiro/steering/tech.md` — tech stack, architecture, deployment, performance
- `.kiro/DEVLOG.md` — up-to-date record of work done

### A3. Identify Key Files
Based on the project structure, read:
- Main entry points (main.py, index.ts, app.py, etc.)
- Configuration files (pyproject.toml, package.json, etc.)
- Key model/schema definitions
- Important service or controller files

### A4. Understand Current State
```bash
git log -10 --oneline
git status
```

### A5. Feature Horizon
```bash
python3 .kiro/scripts/feature_horizon.py --summary
```

### A6. Output Report

Produce a concise, scannable summary with these sections:

**Project Overview** — purpose, primary technologies, current state

**Architecture** — structure, patterns, key directories

**Tech Stack** — languages, frameworks, build tools, testing

**Current State** — active branch, recent changes, observations

**Development Horizon** — output from the horizon script above

**Canonical Workflow Reference** — remind the user of the next steps:
- `@next` → select next feature
- `@plan-feature` → create implementation plan
- `@execute` → implement the plan
- `@devlog-update` → record what was done

**Feature Lifecycle Reference:**
- `not_started` → `next_selected` → `planned` → `in_progress` → `completed`
- At most one feature should be `next_selected` at any time
- `blocked` is not a stored status — it is computed from the dependency graph

---

## Path B: Blank Template (interactive project setup)

The steering documents are empty templates and there is no feature graph. Launch an interactive session to define the project.

### B1. Analyze What Exists
```bash
git branch --show-current 2>/dev/null
tree -L 3 -I 'node_modules|__pycache__|.git|dist|build'
```
Read the steering templates to understand their structure.

### B2. Interactive Project Definition

Guide the user through these questions:
1. **Product**: What is the application? Who are the users? What problem does it solve?
2. **Tech stack**: What languages, frameworks, and infrastructure?
3. **Architecture**: What are the major components? How do they interact?
4. **Structure**: What directory layout? What naming conventions?

### B3. Draft Steering Documents

Based on the user's answers, draft:
- `.kiro/steering/product.md`
- `.kiro/steering/tech.md`
- `.kiro/steering/structure.md`

Present each draft for user review. Iterate until approved.

### B4. Create Feature Graph

After steering documents are finalized, create the feature graph and feature specs by running `@design-digest`. This ensures consistent structure (feature JSON schema, markdown templates, naming conventions, dependency graph) regardless of whether design documents exist.

- If `.kiro/design/` contains research/design documents, `@design-digest` will synthesize them together with the steering documents
- If `.kiro/design/` is empty, `@design-digest` will work from the steering documents and the interactive session context alone

Tell the user:
```
✅ Steering documents created. Next step:

  Run @design-digest to create the feature roadmap.

After that, the project is ready for the canonical workflow:
  @next → @plan-feature → @execute → @devlog-update
```

This is the final step of Path B. `@design-digest` is a separate command the user invokes.
