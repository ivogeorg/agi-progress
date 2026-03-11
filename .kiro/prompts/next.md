---
description: "Select next feature - shows development horizon with recommendation, user picks, status updated to next_selected"
---

# Next: Select Next Feature

## Role
You are a development workflow manager.

## Prerequisite
`@prime` has already been run in this session, so full project context is loaded.

## Process

### 1. Show the Development Horizon

Run the feature horizon script in detail mode:

```bash
python3 .kiro/scripts/feature_horizon.py
```

Present the output to the user as-is. The script shows:
- Progress stats
- Recommended feature with justification
- Other ready features (numbered)
- Blocked features

### 2. Prompt the User

Ask the user to select a feature:

```
SELECT FEATURE:
  [R] Recommended: [recommended-feature-id]
  [1-N] Other ready feature by number
  [Q] Quit without selecting
```

Wait for the user's response. Default (empty input or "R") selects the recommended feature.

### 3. Update Feature Status

After the user selects a feature:

1. Read `.kiro/features.json`
2. Set **any** feature with status `"next_selected"` back to `"not_started"` (enforce single-selection invariant)
3. Set the selected feature's status to `"next_selected"`
4. Write the updated `.kiro/features.json`
5. Confirm:
   ```
   ✅ SELECTED: [feature-id] - [Feature Name]
   Status: next_selected

   Next step: run @plan-feature
   ```
