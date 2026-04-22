# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2026-04-21

### Added
- New Escalation Paths endpoints (create, read, update, delete, list) with typed rule models (alert urgency, working hour, JSON path, field, service, deferral window)
- New API Keys endpoints (create, read, update, delete, list, rotate)
- New SLA endpoints (create, read, update, delete, list)
- New On-Call endpoints (list on-call users)
- New On-Call Pay Reports endpoints (create, read, update, delete, list)
- New Meeting Recordings endpoints (read, list)
- New Catalog Checklist Templates endpoints (create, read, update, delete, list)
- New Catalog Entity Checklists endpoints (read, list)
- New Catalog Properties endpoints (create, read, update, delete, list) — replaces Catalog Fields
- Catalog property endpoints for causes, environments, functionalities, incident types, services, and teams
- New incident actions: `detach_from_parent_incident`, `unmark_as_duplicate_incident`
- New workflow task type: `PageJsmopsOnCallRespondersTaskParams` — page JSM Ops on-call responders
- New workflow task type: `CreateJsmopsAlertTaskParams` — create JSM Ops alerts
- New role permission types: catalogs, communication, edge connectors, incident communication, paging, SLAs, sub-statuses
- Alert trigger params: alert condition urgency support
- Status page: CNAME records and section ordering support
- Page Rootly on-call responders: functionality target support
- GitHub issue task params: issue type and labels support
- Zoom meeting: global dial-in numbers support

### Changed
- Regenerated client from latest OpenAPI specification
- **BREAKING**: Catalog Fields renamed to Catalog Properties across all endpoints and models
- **BREAKING**: Minimum Python version bumped to 3.10

### Removed
- Catalog Fields endpoints and models (replaced by Catalog Properties)
- Some escalation policy path rule type models (consolidated in upstream spec)

### Fixed
- Applied nullable enum fix to 1,348 model files via `tools/fix_nullable_enums.py`
- Escalation path endpoints now fully generated — added `tools/fix_openapi_escalation_paths.py` to patch inline `oneOf` variants into named `$ref` schemas ([upstream bug](https://github.com/openapi-generators/openapi-python-client/issues/1428))

## [1.2.1] - 2025-03-02

### Fixed
- Fix nullable enum handling for UPDATE path models (e.g., `UpdateAlertsSourceDataAttributes`)
  - The v1.2.0 fix only covered GET/list response models, not update request models
  - Updated `fix_nullable_enums.py` to handle multi-line `if (value in ...)` patterns

## [1.2.0] - 2025-02-25

### Fixed
- Nullable enum properties now correctly handle `null` values from the API ([#1405](https://github.com/openapi-generators/openapi-python-client/issues/1405))
  - Added post-generation fix script (`tools/fix_nullable_enums.py`) to patch enum check functions
  - Resolves `TypeError: Unexpected value None` when API returns null for nullable enum fields like `conditionable_type`

### Added
- New incident list filters: `filter[functionality_names]`, `filter[service_names]`, `filter[team_names]`
- New workflow task types:
  - `AddMicrosoftTeamsChatTabTaskParams` - Add tabs to Microsoft Teams chats
  - `SendMicrosoftTeamsChatMessageTaskParams` - Send messages to Microsoft Teams chats
  - `UpdateConfluencePageTaskParams` - Update Confluence pages
  - `UpdateDatadogNotebookTaskParams` - Update Datadog notebooks
  - `UpdateDropboxPaperPageTaskParams` - Update Dropbox Paper pages
  - `UpdateQuipPageTaskParams` - Update Quip pages
  - `UpdateSharepointPageTaskParams` - Update SharePoint pages
- Alert route and alert group endpoint enhancements

### Changed
- Regenerated client from latest OpenAPI specification
- Updated Makefile to automatically apply nullable enum fix after regeneration

### Deprecated
- Catalog Entity Property endpoints - use `fields` attribute on catalog entities or native catalog endpoints instead

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