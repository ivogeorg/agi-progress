# Project Structure

## Directory Layout
```
src/
├── {directory}/     # {Purpose}

assets/              # {Static assets}

tests/
├── unit/
├── integration/
└── data/            # {Test data}

.kiro/
├── data/            # {Project data}
├── design/          # Design research documents to digest with @design-digest
├── documentation/   # Templates, schemas, reference docs
├── features/        # Feature specifications (one per feature)
├── plans/           # Implementation plans (one per feature)
├── prompts/         # @command prompts for canonical workflow
├── scripts/         # Workflow helper scripts
└── steering/        # Product, tech, structure docs (highest authority)
```

## File Naming Conventions
- {Language} modules: {convention}
- Classes: {convention}
- Functions: {convention}
- Constants: {convention}
- Feature IDs: [major-section]-[detail]-[ddddd]

## Module Organization
- {Pattern description}

## Configuration Files
- {File}: {Purpose}

## Documentation Structure
- README.md: Project overview and setup
- DEVLOG.md: Development timeline
- .kiro/features/: Individual feature specs
- .kiro/steering/: Product, tech, structure docs

## Build Artifacts
- {Directory}: {What goes here}

## Environment-Specific Files
- {File}: {Purpose}
