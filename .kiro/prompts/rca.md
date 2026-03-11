---
description: "Analyze and document root cause for a GitHub issue"
argument-hint: "[github-issue-id]"
---

# Root Cause Analysis: GitHub Issue #$ARGUMENTS

## Role
You are a senior engineer investigating a bug report.

## Prerequisites
- GitHub CLI installed and authenticated (`gh auth status`)
- Valid GitHub issue ID from this repository

## Process

### 1. Fetch Issue Details

```bash
gh issue view $ARGUMENTS
```

Extract: title, description, reproduction steps, labels, comments.

### 2. Search Codebase

Find code related to the issue:
- Search for error messages, component names, function names mentioned in the issue
- Check recent changes to affected areas: `git log --oneline -20 -- [relevant-paths]`
- Read affected files in full for context

### 3. Identify Root Cause

Determine:
- What is the actual bug?
- Why is it happening? (logic error, edge case, missing validation, race condition, etc.)
- What was the original intent of the code?
- How widespread is the impact?

### 4. Propose Fix

Design the solution:
- Which files need modification?
- What's the fix strategy?
- What are the risks or side effects?
- What tests are needed to verify?

### 5. Write RCA Document

Save to `.kiro/rca/issue-$ARGUMENTS.md`:

```markdown
# RCA: Issue #$ARGUMENTS — [Title]

**Severity**: Critical|High|Medium|Low
**Status**: [Open|In Progress]

## Problem
[What's happening vs what should happen]

## Root Cause

**Files**: [affected file paths]
**Code location**: [file:line]

[Explanation of why this occurs]

## Impact
- [Scope and affected features]
- [Data/security concerns if any]

## Proposed Fix

### Files to Modify
1. **[file-path]** — [what changes and why]

### Testing Requirements
1. [Test case to verify fix]
2. [Regression test]

### Validation Commands
```bash
[commands to verify]
```

## Next Step
Run `@implement-fix $ARGUMENTS` to implement this fix.
```

### 6. Confirm

```
✅ RCA COMPLETE: Issue #$ARGUMENTS

Saved: .kiro/rca/issue-$ARGUMENTS.md
Severity: [level]

Next step: run @implement-fix $ARGUMENTS
```
