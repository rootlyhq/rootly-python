.PHONY: bump-major bump-minor bump-patch regenerate test

# Get current version from pyproject.toml
CURRENT_VERSION := $(shell grep -E '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
MAJOR := $(shell echo $(CURRENT_VERSION) | cut -d. -f1)
MINOR := $(shell echo $(CURRENT_VERSION) | cut -d. -f2)
PATCH := $(shell echo $(CURRENT_VERSION) | cut -d. -f3)

# Calculate new versions
NEW_MAJOR := $(shell echo $$(($(MAJOR) + 1))).0.0
NEW_MINOR := $(MAJOR).$(shell echo $$(($(MINOR) + 1))).0
NEW_PATCH := $(MAJOR).$(MINOR).$(shell echo $$(($(PATCH) + 1)))

# Today's date
TODAY := $(shell date +%Y-%m-%d)
RUFF_VERSION := 0.16.3
OPENAPI_PYTHON_CLIENT_VERSION := 0.29.0

bump-major:
	@echo "Bumping version: $(CURRENT_VERSION) -> $(NEW_MAJOR)"
	@sed -i '' 's/version = "$(CURRENT_VERSION)"/version = "$(NEW_MAJOR)"/' pyproject.toml
	@echo "Version bumped to $(NEW_MAJOR)"

bump-minor:
	@echo "Bumping version: $(CURRENT_VERSION) -> $(NEW_MINOR)"
	@sed -i '' 's/version = "$(CURRENT_VERSION)"/version = "$(NEW_MINOR)"/' pyproject.toml
	@echo "Version bumped to $(NEW_MINOR)"

bump-patch:
	@echo "Bumping version: $(CURRENT_VERSION) -> $(NEW_PATCH)"
	@sed -i '' 's/version = "$(CURRENT_VERSION)"/version = "$(NEW_PATCH)"/' pyproject.toml
	@echo "Version bumped to $(NEW_PATCH)"

regenerate:
	curl -fsSL https://rootly-heroku.s3.amazonaws.com/swagger/v1/swagger.json -o tools/swagger.json
	python tools/fix_openapi_escalation_paths.py tools/swagger.json
	python tools/fix_nullable_severity.py tools/swagger.json
	uvx --from openapi-python-client==$(OPENAPI_PYTHON_CLIENT_VERSION) openapi-python-client generate \
		--path tools/swagger.json \
		--no-fail-on-warning \
		--output-path . \
		--overwrite \
		--config tools/config.yaml
	@echo "Applying nullable enum fix..."
	@python tools/fix_nullable_enums.py
	@echo "Fixing lint errors..."
	@uvx --from ruff==$(RUFF_VERSION) ruff check --fix .
	@echo "Formatting patched files..."
	@uvx --from ruff==$(RUFF_VERSION) ruff format .

test:
	python -m unittest discover -s tests
	python -c "import rootly_sdk; print('SDK imports successfully')"
