---
description: "Fix issues found in a code review"
argument-hint: "[path-to-review-file]"
---

# Code Review Fix

## Role
You are a senior engineer fixing issues identified in a code review.

## Process

### 1. Read the Review

Read the code review file from `$ARGUMENTS` (e.g., `.kiro/code-reviews/2026-03-10-ml-medgemma-setup.md`).

If no argument provided, list available reviews:
```bash
ls -t .kiro/code-reviews/*.md
```
Ask the user which one to fix.

### 2. Fix Each Issue

For each issue in the review, in order of severity (critical → high → medium → low):

1. Read the affected file in full for context
2. Explain what's wrong (1-2 sentences)
3. Apply the fix
4. Run the relevant validation command from the feature's plan if available

### 3. Summary

After all fixes:
```
✅ CODE REVIEW FIXES APPLIED

Fixed: N issues (X critical, Y high, Z medium, W low)
Skipped: N issues (with justification for each)

Files modified:
  • path/to/file.py — [what changed]

Next step: re-run @code-review to verify
```
