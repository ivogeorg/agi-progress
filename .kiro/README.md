# Spec-Driven Development Workflow

A structured, AI-assisted development workflow using `@command` prompts. Each prompt is a self-contained instruction set that drives one step of the development process. The user is the sequencer — prompts suggest the next step but never chain automatically.

## Quick Start

1. Run `@prime` to load project context
2. Run `@next` to pick a feature
3. Run `@plan-feature` to create the implementation plan
4. Run `@execute` to implement it
5. Run `@devlog-update` to record what was done
6. Repeat from step 2

For a new project, `@prime` detects the blank state and walks you through initial setup, ending with `@design-digest` to create the feature roadmap.

## Directory Structure

```
.kiro/
├── steering/           # Highest authority — what the project IS
│   ├── product.md      # Product purpose, users, features, objectives
│   ├── tech.md         # Technology stack, architecture, constraints
│   └── structure.md    # Directory layout, naming conventions
│
├── features/           # One spec per feature (created by @design-digest or @add-feature)
│   └── {feature-id}.md
│
├── features.json       # Feature graph — statuses, dependencies, metadata
│
├── plans/              # Implementation plans (created by @plan-feature)
│   └── {feature-id}-plan.md
│
├── prompts/            # @command prompts (this workflow)
│   ├── archived/       # Retired prompts (preserved for history)
│   └── *.md
│
├── scripts/            # Workflow helper scripts
│   └── feature_horizon.py
│
├── design/             # Research/design docs (input to @design-digest)
│
├── documentation/      # Templates, schemas, reference docs
│   ├── templates/      # Steering doc, feature spec, DEVLOG entry templates
│   └── schemas/        # features.json schema
│
├── data/               # Project data (training data, test data, etc.)
│
├── DEVLOG.md           # Development log — chronological record of all work
│
├── code-reviews/       # Output from @code-review
├── system-reviews/     # Output from @system-review and @check-intent-drift
├── rca/                # Root cause analysis documents
└── reports/            # Stakeholder reports (at project root: reports/)
```

## Feature Lifecycle

```
not_started → next_selected → planned → in_progress → completed
```

- At most one feature is `next_selected` at any time
- `blocked` is not stored — it's computed from the dependency graph
- `deprecated` removes a feature from the active graph

## Canonical Workflow (Backbone)

These prompts run in sequence for each feature. They are the core development loop.

| Step | Prompt | What it does | Input | Output |
|------|--------|-------------|-------|--------|
| 0 | `@prime` | Load project context, produce status report | Steering docs, DEVLOG, git | Session context |
| 0 | `@design-digest` | Synthesize design docs into feature roadmap | `.kiro/design/*.md`, steering docs | `features.json`, feature specs |
| 1 | `@next` | Show horizon, user picks next feature | `features.json` | Status → `next_selected` |
| 2 | `@plan-feature` | Create implementation plan | Feature spec, codebase | Plan file, status → `planned` |
| 3 | `@execute` | Implement the plan | Plan file | Working code, status → `completed` |
| 4 | `@devlog-update` | Record what was done | Git history, feature specs | DEVLOG entry |

`@prime` and `@design-digest` run once at project start (or when new design docs are added). Steps 1-4 repeat for each feature.

## Off-Backbone Prompts

These run independently, outside the feature lifecycle. They don't change feature statuses.

### Feature Management
| Prompt | Purpose |
|--------|---------|
| `@add-feature` | Add a new feature to the roadmap (status: `not_started`) |

### Code Quality
| Prompt | Purpose |
|--------|---------|
| `@code-review` | Technical review of code (scoped to feature or uncommitted changes) |
| `@code-review-fix` | Fix issues found by `@code-review` |

### Bug Investigation
| Prompt | Purpose |
|--------|---------|
| `@rca` | Root cause analysis for a GitHub issue |
| `@implement-fix` | Implement fix from an RCA document |

### Process Analysis
| Prompt | Purpose |
|--------|---------|
| `@system-review` | Compare implementation vs plan — find process bugs |
| `@check-intent-drift` | Check if project is drifting from original intent |
| `@stakeholder-update` | Generate progress report for non-technical audience |

## Steering Documents

The three files in `.kiro/steering/` are the highest authority for project intent. All prompts reference them. They define:

- **product.md** — What the project is, who it's for, what it does, why it matters
- **tech.md** — How it's built, what technologies, what constraints
- **structure.md** — Where things go, naming conventions, module organization

Templates for new projects are in `.kiro/documentation/templates/`.

## Feature Graph (`features.json`)

Flat JSON structure with dependency edges. Each feature has:

```json
{
  "id": "ml-medgemma-setup-00001",
  "name": "MedGemma 27B Setup",
  "version": "v00",
  "moscow": "Must-have",
  "description": "EARS-formatted requirement",
  "dependencies": ["other-feature-id"],
  "tasks": [{"id": "task-id", "name": "description", "moscow": "Must-have"}],
  "status": "not_started",
  "created_date": null,
  "started_date": null,
  "planned_date": null,
  "completed_date": null,
  "testable_outcome": "Clear success criterion",
  "design_source": "source document or User request"
}
```

Feature IDs follow the convention: `[major-section]-[detail]-[ddddd]`
- Major sections: `infra`, `auth`, `ui`, `api`, `ml`, `data`, `backend`, `test`
- Versions: `vXX` (zero-padded, open-ended: v00, v01, v02, ...)

## DEVLOG

Chronological development record in `.kiro/DEVLOG.md`. Each entry follows the template in `.kiro/documentation/templates/devlog-entry-template.md`. Entries are added after feature completion or significant non-feature work.

The DEVLOG serves as input to `@stakeholder-update` and `@check-intent-drift`.

## Horizon Script

`python3 .kiro/scripts/feature_horizon.py` analyzes the feature graph:
- `--summary` mode: compact status for `@prime`
- Default (detail) mode: scored recommendation for `@next`

It computes which features are ready (all dependencies met), which are blocked, and recommends the next feature based on priority, unblock potential, and complexity.

## Starting a New Project

1. Copy the `.kiro/` directory structure (prompts, scripts, templates, empty directories)
2. Run `@prime` — it detects the blank state and guides you through:
   - Interactive product/tech/structure definition
   - Drafting the three steering documents
3. Run `@design-digest` to create the feature roadmap
4. Begin the canonical workflow: `@next` → `@plan-feature` → `@execute` → `@devlog-update`
