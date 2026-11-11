<!--
Use a Conventional Commit PR title: <type>(<optional scope>): <description>

Examples:
  feat(incidents): add incident search support [PRF-3498]
  fix(client): preserve configured request timeout [TER-227]
  docs: clarify SDK configuration
  chore(deps): update dependencies

Use feat for new features, fix for bug fixes, and ! before the colon for
breaking changes, e.g. feat!: remove a deprecated client method.

Release Please uses commit messages for release notes and version bumps.
When squash-merging, ensure the final commit title follows this format too.
Keep relevant Linear issue IDs as a title suffix, as shown above, and link
the ticket in the description. The title must start with the Conventional
Commit type, not the ticket ID (e.g. avoid [PRF-3498] feat(...): ...).
-->

## Description

<!-- What changes are being made in this PR? -->

## Motivation

<!-- Why are we making this change? What problem does it solve? Link any related issues. -->

## Testing

- [ ] Added new tests for this functionality
- [ ] Existing tests cover this change
- [ ] No tests needed (explain why below)

## Risk Assessment

<!-- Describe the risk level (low/medium/high) and any rollout considerations. -->
