---
description: "Add a new feature to existing roadmap with proper dependency management"
argument-hint: "[feature-name-or-description]"
---

# Add Feature: Integrate New Feature into Roadmap

## Role
You are a development workflow manager adding a feature to an existing roadmap.

## Prerequisite
- `.kiro/features.json` must exist (run `@design-digest` first if not)
- Feature name or description provided as `$ARGUMENTS`

## Core Principle
Maintain graph integrity. New features must fit into the dependency structure without cycles.

## Process

### 1. Understand the Request

From `$ARGUMENTS`, extract the feature name, purpose, and scope.

If the argument is too vague to proceed, ask:
```
📋 FEATURE DETAILS NEEDED

Please provide:
1. Feature name (brief, descriptive)
2. What should it do? (1-2 sentences)
3. Version? (v00/v01/v02)
4. Priority? (Must-have/Should-have/Could-have)
5. Dependencies? (Which existing features must complete first?)
```

Otherwise, proceed directly — don't ask for confirmation of things you can infer.

### 2. Generate Feature ID

Convention: `[major-section]-[detail]-[ddddd]`

Major sections: `infra`, `auth`, `ui`, `api`, `ml`, `data`, `backend`, `test`

Counter: read `.kiro/features.json`, find all features matching `[major-section]-[detail]-*`, increment the highest counter by 1, zero-pad to 5 digits.

### 3. Version Normalization

Canonical form is `vXX` where `XX` is a zero-padded two-digit number.

1. If input already matches `vXX` (e.g., `v00`, `v03`, `v17`) → use as-is
2. If input matches a known alias → normalize:
   - `V0`, `Version 0`, `version 0`, `ver 0`, `0` → `v00`
   - `V1`, `Version 1`, `version 1`, `ver 1`, `1` → `v01`
   - `V2`, `Version 2`, `version 2`, `ver 2`, `2` → `v02`
   - (Same pattern for any single digit N → `v0N`)
3. Otherwise → ask the user to provide a valid `vXX` version

New versions (e.g., `v03`, `v04`) are valid without being pre-registered. The version field is open-ended.

### 4. Validate Dependencies

Read `.kiro/features.json` and check:
1. All listed dependencies exist in `features.json`
2. No circular dependency is introduced (walk the graph)
3. Dependencies are in the same or earlier version

If a cycle is detected:
```
❌ CIRCULAR DEPENDENCY

[new-feature] → [dep-1] → ... → [new-feature]

Please revise dependencies.
```

If a dependency doesn't exist:
```
❌ UNKNOWN DEPENDENCY: [dep-id]

Available features: [list matching prefix]
```

### 5. Create Feature Spec File

Write `.kiro/features/{feature-id}.md` using the template at `.kiro/documentation/templates/feature-spec-template.md`.

Fill in all template fields from the gathered information. Use EARS format for the description.

### 6. Update features.json

Add the feature entry to `.kiro/features.json` using the actual schema (reference `.kiro/documentation/schemas/features-schema.json`):

```json
"{feature-id}": {
  "id": "{feature-id}",
  "name": "{Feature Name}",
  "version": "{vXX}",
  "moscow": "{priority}",
  "description": "{EARS description}",
  "dependencies": ["{dep-1}", "{dep-2}"],
  "tasks": [
    {
      "id": "{task-id}",
      "name": "{task description}",
      "moscow": "{priority}"
    }
  ],
  "status": "not_started",
  "created_date": "{ISO-8601 now}",
  "started_date": null,
  "completed_date": null,
  "planned_date": null,
  "testable_outcome": "{outcome}",
  "design_source": "User request"
}
```

Validate the JSON after writing (no syntax errors, no duplicate IDs).

### 7. Present for Review

Show the user what was created and let them approve or edit before finalizing:

```
📋 FEATURE ADDED

  ID: {feature-id}
  Name: {Feature Name}
  Version: {vXX}
  Priority: {moscow}
  Dependencies: {list or "none"}
  Tasks: {count}

  Files written:
    • .kiro/features/{feature-id}.md
    • .kiro/features.json (updated)

  Graph integrity: ✅ No cycles, all deps exist

  Review the spec file and confirm: (yes/edit)
```

If the user says edit, apply their changes and re-validate.

### 8. Confirm

```
✅ FEATURE INTEGRATED: {feature-id}

Next steps:
  • @next to see updated horizon
  • @plan-feature when ready to implement
```

## Edge Cases

### Feature ID Already Exists
Increment the counter and inform the user of the generated ID.

### No Dependencies (Root Feature)
Valid — some features are independent. Proceed without warning unless the feature clearly should depend on something (e.g., a UI feature with no backend dependency).

### Deprecated Features in Dependencies
Reject: "Cannot depend on deprecated feature {id}. Choose an active alternative."
