# Workflow Overhaul (Feb 24, 2026)

General notes:
1. Understand workflow in @prime:
   1. feature naming
   2. .kiro/features.json: priority graph
   3. .kiro/features: overview files 
   4. .kiro/plans: detailed implementation and validation plans (for @execute)
   5. .kiro/DEVLOG.md
3. Shorten @command prompts.
4. Elaborate workflow @command sequence: @design-digest (features --> @prime --> iterate: { @next (horizon, only pick and set as next and "started") --? @plan-feature (.kiro/plans) --> @execute (incl. auto/manual validation) --> @complete-feature (update status, update horizon, update DEVLOG.md) } --> @code-review
5. Granularity of features:
   1. Significant change that can be automatically and manually validated and tested.
   2. Non-overlap
6. Review the steering document drafts and remove *`-draft`*.
7. Add intent-drift guards! (See last-but-one or last session in [AI Superstream: Building SaaS Businesses with AI](https://learning.oreilly.com/live-events/ai-superstream-building-saas-businesses-with-ai/0642572279356/).
8. @devlog-update has many problems:
   * Too verbose (many tokens)
   * Erratic (no central "theme")
   * Generates its own "entry" every time rather than using the entry template in `.kiro/documentation/templates/devlog-entry-template.md`
   * The template is also not very well structured
   * Doesn't roll off the tongue (consider reverting to @update-devlog)
9. @devlog-update should:
   * work if invoked anywhere (in any context)
   * generate sufficient but succinct entries (no need for DEVLOG.md be an enormous file)
   * **TODO:** Examine current [DEVLOG.md](.kiro/DEVLOG.md) to judge how it reads
   * Should be easy to digest for stakeholder update
