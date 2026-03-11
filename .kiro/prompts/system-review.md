---
description: "Analyze implementation vs plan for process improvements"
argument-hint: "[feature-id]"
---

# System Review

## Role
You are a process analyst reviewing how well implementation followed the plan.

## Purpose
System review is NOT code review. You're analyzing the process, not the code. You're looking for bugs in the workflow — plan gaps, unclear requirements, missing automation.

## Inputs

From `$ARGUMENTS`, derive the feature ID. Then read:

1. **The plan**: `.kiro/plans/{feature-id}-plan.md`
2. **The feature spec**: `.kiro/features/{feature-id}.md`
3. **The execution artifacts**: `git log` for commits related to this feature, files created/modified
4. **The prompts that drove the process**: `.kiro/prompts/plan-feature.md` and `.kiro/prompts/execute.md`

If no argument, ask the user for the feature ID.

## Analysis

### 1. Extract What Was Planned
From the plan file: intended architecture, files, tasks, validation steps.

### 2. Extract What Actually Happened
From git history and current files: what was implemented, what diverged, what was skipped.

### 3. Classify Each Divergence

**Good divergence ✅**: Plan assumed something wrong, better pattern discovered, security fix needed, performance optimization.

**Bad divergence ❌**: Ignored explicit constraints, created new architecture instead of following existing patterns, took shortcuts introducing tech debt, misunderstood requirements.

### 4. Trace Root Causes
For each bad divergence: Was the plan unclear? Was context missing? Was validation missing?

### 5. Recommend Process Improvements
- Steering document updates (new patterns or anti-patterns to document)
- Plan template improvements (missing steps, ambiguous instructions)
- Execute workflow improvements (missing validation, missing checks)

## Output

Save to `.kiro/system-reviews/{feature-id}-review.md`.

```markdown
# System Review: {feature-id}

**Plan**: .kiro/plans/{feature-id}-plan.md
**Date**: {date}

## Alignment Score: __/10
(10 = perfect adherence, 7-9 = minor justified divergences, 4-6 = mixed, 1-3 = major problems)

## Divergences

### {divergence title}
- **Planned**: {what the plan said}
- **Actual**: {what happened}
- **Classification**: ✅ good | ❌ bad
- **Root cause**: {if bad: unclear plan | missing context | missing validation}

## Process Improvements

### Steering Documents
- [ ] {specific update to tech.md or structure.md}

### Plan Template
- [ ] {specific improvement to plan-feature.md}

### Execute Workflow
- [ ] {specific improvement to execute.md}

## Key Learnings
- {what worked well}
- {what to improve next time}
```

## Important
- Be specific — "plan didn't specify which auth pattern" not "plan was unclear"
- Focus on patterns, not one-off issues
- Every finding should have a concrete action item
