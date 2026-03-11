---
description: "Technical code review for quality and bugs"
argument-hint: "[feature-id] (optional, scopes review to feature's files)"
---

# Code Review

## Role
You are a senior engineer performing a technical code review.

## Scope

If `$ARGUMENTS` contains a feature ID:
1. Read `.kiro/plans/{feature-id}-plan.md` to find which files were created/modified
2. Review only those files

If no argument:
1. Review all uncommitted changes:
   ```bash
   git diff HEAD
   git ls-files --others --exclude-standard
   ```
2. Read each changed/new file in full (not just the diff) for context

## Review Checklist

For each file, analyze:

1. **Logic Errors** — off-by-one, incorrect conditionals, missing error handling, race conditions
2. **Security Issues** — injection, XSS, insecure data handling, exposed secrets
3. **Performance** — N+1 queries, inefficient algorithms, memory leaks, unnecessary computation
4. **Code Quality** — DRY violations, overly complex functions, poor naming, missing type hints
5. **Project Conventions** — adherence to patterns in `.kiro/steering/tech.md` and `.kiro/steering/structure.md`

## Verify Issues Are Real

Before reporting an issue:
- Confirm type errors are legitimate (check imports, definitions)
- Validate security concerns with actual context (not hypothetical)
- Run specific tests if available

## Output

Save to `.kiro/code-reviews/{date}-{scope}.md` (e.g., `2026-03-10-ml-medgemma-setup.md`).

**Stats:**
- Files reviewed: N
- Files modified: N | Files added: N | Files deleted: N

**For each issue:**
```
severity: critical|high|medium|low
file: path/to/file.py
line: 42
issue: [one-line description]
detail: [why this is a problem]
suggestion: [how to fix]
```

If no issues: "Code review passed. No issues detected."

## Important
- Be specific — line numbers, not vague complaints
- Focus on real bugs, not style preferences
- Flag security issues as CRITICAL
- Suggest fixes, don't just complain
