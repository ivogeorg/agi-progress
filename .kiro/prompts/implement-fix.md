---
description: "Implement fix from RCA document for a GitHub issue"
argument-hint: "[github-issue-id]"
---

# Implement Fix: GitHub Issue #$ARGUMENTS

## Role
You are a senior engineer implementing a bug fix from an RCA document.

## Prerequisites
- RCA document exists at `.kiro/rca/issue-$ARGUMENTS.md`
- If not, tell the user to run `@rca $ARGUMENTS` first

## Process

### 1. Read the RCA

Read `.kiro/rca/issue-$ARGUMENTS.md` in full. Understand:
- Root cause and affected files
- Proposed fix strategy
- Testing requirements

### 2. Verify Current State

Confirm the issue still exists by checking the affected code locations from the RCA.

### 3. Implement the Fix

For each file in the RCA's "Files to Modify" section:
1. Read the file in full for context
2. Apply the fix as described
3. Maintain existing code style and conventions
4. Add comments if the fix is non-obvious

### 4. Run Validation

Execute all validation commands from the RCA. If any fail, fix and re-run.

### 5. Manual Verification

```
🧪 FIX IMPLEMENTED

Files modified:
  • [list]

Validation results:
  • [results]

Please verify the fix resolves the issue. Confirmed? (yes/no)
```

If no: ask what's wrong, fix, re-validate.

### 6. Report

```
✅ FIX COMPLETE: Issue #$ARGUMENTS

Files modified:
  • [list]

Suggested commit message:
  fix: [description] (closes #$ARGUMENTS)

Next step: run @devlog-update if this was significant work
```
