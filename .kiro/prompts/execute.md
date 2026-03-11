---
description: "Execute an implementation plan for a planned feature"
---

# Execute: Implement from Plan

## Role
You are a senior software engineer implementing a feature from a detailed plan.

## Prerequisite
`@plan-feature` has been run and at least one feature has status `"planned"` in `.kiro/features.json`.

## Core Principle
Follow the plan. The plan contains everything needed for one-pass implementation. Do not skip validation steps.

**⚠️ NO INTERACTIVE COMMANDS.** All commands must be non-interactive (use `-y`, `--yes`, `--force` flags). Interactive commands hang because prompts don't display to the user.

## Process

### 1. Find the Target Feature

```bash
python3 -c "
import json
with open('.kiro/features.json') as f:
    features = json.load(f)['features']
planned = [f for f in features.values() if f.get('status') == 'planned']
if not planned:
    print('ERROR: No feature with status planned. Run @plan-feature first.')
elif len(planned) == 1:
    print(planned[0]['id'])
else:
    planned.sort(key=lambda f: f.get('planned_date') or '')
    print('MULTIPLE PLANNED FEATURES (oldest first):')
    for i, f in enumerate(planned, 1):
        print(f\"  [{i}] {f['id']} - {f['name']} (planned: {f.get('planned_date', 'unknown')})\")
"
```

- If no planned feature exists, stop and tell the user to run `@plan-feature`.
- If exactly one, proceed with it.
- If multiple, present the list (sorted by `planned_date`, oldest first) and ask the user which one to execute.

### 2. Read the Plan

Read `.kiro/plans/{feature-id}-plan.md`. Read the entire plan before starting:
- Understand all tasks and their order
- Note validation commands
- Note files to read before implementing

### 3. Update Status to In-Progress

1. Read `.kiro/features.json`
2. Set the feature's status to `"in_progress"`
3. Set `"started_date"` to the current ISO-8601 timestamp (if not already set)
4. Write the updated `.kiro/features.json`

### 4. Execute Tasks in Order

For each task in the plan:

1. Read any prerequisite files mentioned
2. Implement the task exactly as specified
3. Run the task's validation command (if provided)
4. If validation fails, fix and re-validate before moving on

Maintain consistency with existing code patterns, type hints, and project conventions.

### 5. Run Validation Commands

Execute ALL validation commands from the plan's validation section. If any fail, fix the issue and re-run until all pass.

### 6. Manual Validation

Stop and prompt the user:

```
🧪 AUTOMATED VALIDATION COMPLETE

Please review:
1. Files created/modified (list them)
2. Test results
3. Manual testing if applicable

Did manual validation succeed? (yes/no)
```

If no: ask what failed, fix, return to validation. Do NOT proceed until confirmed.

### 7. Update Feature Status to Completed

After user confirms:

1. Read `.kiro/features.json`
2. Set the feature's status to `"completed"`
3. Set `"completed_date"` to the current ISO-8601 timestamp
4. Write the updated `.kiro/features.json`
5. Update the feature spec `.kiro/features/{feature-id}.md`:
   - Set frontmatter `status: completed`
   - Set frontmatter `completed_date: {ISO-8601 now}`
   - Set frontmatter `started_date` if not already set
   - Check off completed validation checklist items

### 8. Report

```
✅ FEATURE COMPLETED: {feature-id} - {Feature Name}

### Files Created
- list of new files

### Files Modified
- list of modified files

### Validation Results
- summary of what passed

Next step: run @devlog-update to record this work
```
