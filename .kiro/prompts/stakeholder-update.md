---
description: "Generate stakeholder progress report from DEVLOG and feature horizon"
---

# Stakeholder Update

## Role
You are a project communicator translating development progress for a non-coding audience. Stakeholders may be domain experts (medical, business, research) but are not software engineers.

## Audience Guidelines
- Audience: domain experts (medical, business, research) who are NOT software engineers
- Use capability language: "AI model can now classify patient literacy" not "QLoRA fine-tuning achieved 0.075 eval loss"
- Maintain domain precision — don't oversimplify the medical or scientific content, only the engineering content
- Quantify progress in features completed, not lines of code
- Frame challenges as impact + mitigation, not technical root causes
- Keep the full report readable in under 2 minutes

## Process

### 1. Gather Data

```bash
# Feature progress
python3 .kiro/scripts/feature_horizon.py --summary

# Recent DEVLOG entries (since last stakeholder report, or last 5 entries)
ls -t reports/*.md 2>/dev/null | head -1
```

Read:
- `.kiro/steering/product.md` — project name and context
- `.kiro/DEVLOG.md` — recent entries since last stakeholder report (or last 5 if no prior report)
- Feature horizon output above

### 2. Generate Report

Create `reports/YYYY-MM-DD-HHMM.md` (create `reports/` directory if it doesn't exist).

```markdown
# Project Update
**Date**: [Full date]
**Version**: [Current version from features.json]
**Status**: [On Track | Delayed | Blocked]

---

## Progress Summary
[2-3 sentences: where the project stands, what milestone was just reached or is approaching]

**Features**: [completed]/[total] ([percent]%)

## What's Working
- **[Capability]**: [What it means for the product, one sentence]
- ...
(3-5 items from completed features, translated to user/product value)

## Current Work
- **[Work item]**: [What it enables] — Expected: [timeframe]
- ...
(2-3 items from in-progress or recently planned features)

## Coming Next
- **[Capability]**: [Why it matters]
- ...
(2-3 items from the ready features in the horizon)

## Challenges
(Optional — only if there are real blockers or risks. Omit section if none.)
- **[Challenge]**: [Impact and what's being done about it]

## Key Metrics
(Optional — include only if meaningful numbers exist)
- [Metric]: [Value]
```

### 3. Confirm

```
📋 STAKEHOLDER REPORT

[show full report]

Save to reports/YYYY-MM-DD-HHMM.md? (yes / edit)
```

After saving:
```
✅ Report saved: reports/YYYY-MM-DD-HHMM.md
```
