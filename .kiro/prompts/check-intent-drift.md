---
description: "Check alignment between original product intent and actual project trajectory"
---

# Check Intent Drift

## Role
You are a product strategist auditing a project for alignment between stated intent and actual execution.

## Purpose
Projects drift. Small pragmatic decisions accumulate across sessions — features get added, priorities shift, workarounds become permanent, original objectives fade. This prompt is a periodic health check that compares what the project *said* it would build against what it *is actually* building, and flags the gaps.

Drift is not inherently bad. Intentional pivots are healthy. The danger is *unnoticed* drift — when the project gradually becomes something different from what the steering documents describe, and nobody updated the docs.

## When to Run
- After every 3-5 features completed
- Before major planning sessions
- When returning after a long break
- When something feels "off" about project direction

## Process

### 1. Establish the Intent Anchor

Read the steering documents — these define what the project *should* be:

- `.kiro/steering/product.md` — product purpose, target users, key features, business objectives, success criteria, user journey. **The Product Purpose section is the most stable anchor.** Everything else can evolve, but if the product purpose no longer describes what you're building, that's a major drift signal.
- `.kiro/steering/tech.md` — technology choices, architecture, constraints
- `.kiro/steering/structure.md` — project organization

Extract and list:
- **Core mission** (1 sentence from Product Purpose)
- **Stated business objectives** (numbered list)
- **Stated success criteria** (numbered list)
- **Key features promised** (numbered list)
- **Target users** (who the product is for)

### 2. Map the Actual Trajectory

Read the execution record — this shows what the project *actually did*:

- `.kiro/DEVLOG.md` — full development history, decisions made, pivots taken
- `.kiro/features.json` — feature statuses, what's completed vs planned

```bash
python3 .kiro/scripts/feature_horizon.py --summary
```

From these sources, extract:
- **What has been built** (completed features, in chronological order)
- **What is being built now** (in-progress, planned, next_selected)
- **What was added after initial design** (features not in the original roadmap)
- **What was deferred or dropped** (features that lost priority or were deprecated)
- **Time allocation** (from DEVLOG: how much time went to infrastructure/workflow vs. product features)

### 3. Alignment Analysis

Compare intent (step 1) against trajectory (step 2) across these dimensions:

**A. Mission Alignment**
Does the work done and planned still serve the core mission? Or has the project drifted toward a different problem?

**B. Objective Coverage**
For each stated business objective: is there completed or planned work that addresses it? Are any objectives orphaned (no features serve them)?

**C. Feature Fidelity**
Compare the key features promised in product.md against the feature graph. What's delivered? What's missing? What was added that wasn't originally planned?

**D. User Focus**
Is the work still oriented toward the stated target users? Or has the focus shifted (e.g., from patient-facing to developer-facing)?

**E. Scope Creep vs. Scope Shrink**
Has the project grown beyond its original boundaries? Or has it contracted, dropping promised capabilities?

**F. Technology Alignment**
Are the technology choices in tech.md still reflected in the implementation? Any unplanned technology additions or abandonments?

**G. Time Allocation**
What fraction of total development time has gone to product features vs. infrastructure, tooling, and workflow? Is this ratio healthy for the project's stage?

### 4. Classify Each Drift

For every drift identified, classify it:

- **Intentional pivot** 📐 — documented in DEVLOG with rationale. Steering docs may need updating to match.
- **Pragmatic adaptation** 🔧 — reasonable response to a constraint (hardware, time, tooling). May or may not need steering doc updates.
- **Unnoticed drift** ⚠️ — no documented decision, the project just gradually moved. Needs attention.
- **Scope creep** 📈 — work added without corresponding steering doc update or priority justification.
- **Abandoned intent** 🚫 — something promised in steering docs that has no path to delivery and no documented decision to drop it.

### 5. Write the Report

Save to `.kiro/system-reviews/intent-drift-YYYY-MM-DD.md`:

```markdown
# Intent Drift Report — YYYY-MM-DD

## Mission Check
**Core mission**: [1 sentence from product.md]
**Alignment**: ✅ On track | ⚠️ Drifting | 🚫 Misaligned
**Summary**: [2-3 sentences on overall alignment]

## Drift Map

### [Drift title]
- **Dimension**: [Mission | Objectives | Features | Users | Scope | Technology | Time]
- **Classification**: [📐 Intentional | 🔧 Pragmatic | ⚠️ Unnoticed | 📈 Scope creep | 🚫 Abandoned]
- **Evidence**: [Specific DEVLOG entries, features, or commits]
- **Impact**: [How this affects the product]
- **Recommendation**: [Update steering docs | Course-correct | Accept and document | Investigate]

(Repeat for each drift identified. If no drift found in a dimension, omit it.)

## Objective Scorecard

| # | Business Objective | Status | Evidence |
|---|-------------------|--------|----------|
| 1 | [objective] | ✅ Addressed / ⚠️ Partial / 🚫 Orphaned | [features or work] |
| 2 | ... | ... | ... |

## Time Allocation
- **Product features**: ~X hours (Y%)
- **Infrastructure/tooling**: ~X hours (Y%)
- **Workflow/process**: ~X hours (Y%)
- **Assessment**: [Healthy | Front-loaded infra (expected early) | Concerning]

## Recommendations

### Steering Document Updates
- [ ] [Specific update to product.md, tech.md, or structure.md]

### Course Corrections
- [ ] [Specific action to realign with intent]

### Accepted Divergences
- [ ] [Drift that is fine — document it and move on]

## Summary for DEVLOG

> **@check-intent-drift [YYYY-MM-DD]**: [2-3 sentence summary suitable for direct inclusion in a DEVLOG entry. State overall alignment, key drifts found, and top recommendation.]
```

### 6. Present for Review

```
📋 INTENT DRIFT REPORT

[show full report]

Save to .kiro/system-reviews/intent-drift-YYYY-MM-DD.md? (yes / edit)
```

After saving:
```
✅ Report saved: .kiro/system-reviews/intent-drift-YYYY-MM-DD.md

The "Summary for DEVLOG" section at the bottom is ready to paste into a @devlog-update entry.
```
