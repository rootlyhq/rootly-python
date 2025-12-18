# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-12-18

### Added
- New Status API endpoints (`get_status`, `list_statuses`)
- New task type: Create sub-incident (`CreateSubIncidentTaskParams`)
- OpenAI chat completion reasoning parameters (`reasoning_effort`, `reasoning_summary`)
- Alert trigger params now support alert field conditions
- Schedule rotation member management with member type support
- Schedule Slack channel configuration

### Changed
- Regenerated client from latest OpenAPI specification
- Simplified communications group models structure

### Removed
- Deprecated communications group member and condition attribute models

### Known Issues
- Escalation path endpoints not generated due to OpenAPI schema issues with union types in `rules_item`

## [1.0.1] - 2025-10-16

### Changed
- Regenerated client from latest OpenAPI specification with literal enums support
- Enabled `literal_enums: true` in OpenAPI generator config to handle duplicate enum keys

### Fixed
- OpenAPI generator duplicate enum key errors by enabling literal enums

## [1.0.0] - 2025-10-16

### Added
- GitHub Actions publishing workflow for automated PyPI releases on git tags
- New API endpoints for alert sources (create, read, update, delete, list)
- Communications API endpoints for groups, stages, templates, and types
- User email addresses and phone numbers management endpoints
- User update endpoint
- Alert fields API endpoints
- New task types: Coda page creation, Anthropic and Google Gemini chat completions
- Enhanced escalation policy paths with time restrictions
- New incident relationship fields (cancelled_by, closed_by, in_triage_by, mitigated_by, resolved_by, started_by)
- Live call router enhancements with paging targets and waiting music
- Phone verification functionality
- Role relationship models

### Changed
- **BREAKING**: Alert source endpoints renamed from `alert_source` to `alerts_source` (plural)
- **BREAKING**: Alert source model files renamed to use plural form
- Enhanced alert groups with conditions support
- Improved alert routing rules with better condition types
- Updated team endpoints with include parameter support
- Enhanced catalog entity updates
- Improved heartbeat error handling (404 and 422 responses)
- Updated alert list endpoint with status filtering
- Enhanced live call router with escalation policy trigger parameters
- Updated various model attributes for better type safety

### Fixed
- GitHub Actions workflow: Added `--system` flag for uv pip install in CI environment
- GitHub Actions workflow: Install package dependencies before testing imports
- Updated httpx dependency constraint to `>=0.20.0,<0.29.0`
- Improved error handling across multiple endpoints
- Better type definitions for various model attributes

### Removed
- **BREAKING**: Old alert source endpoints and models (singular form)
- Deprecated escalation policy trigger parameter models
- Some obsolete alert routing rule destination models

### Known Issues
- AlertSource enum still missing `mobile` value despite it being returned by the API

## Previous Releases

Changes before this version were not systematically tracked in a changelog.