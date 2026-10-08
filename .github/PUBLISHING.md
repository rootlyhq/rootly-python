# Publishing to PyPI

This repository uses GitHub Actions to automatically publish packages to PyPI when a new version tag is pushed.

## Setup Instructions

### 1. PyPI Trusted Publisher

The `rootly` project uses PyPI Trusted Publishing with these values:

- **Owner**: `rootlyhq`
- **Repository**: `rootly-python`
- **Workflow**: `publish.yml`
- **Environment**: `pypi`

The GitHub `pypi` environment requires approval and only permits tags matching `v*`. The publishing job obtains a short-lived PyPI credential through OpenID Connect, so no long-lived PyPI token is stored in GitHub.

### 2. Publishing a New Version

To publish a new version:

1. **Review the Release Drafter draft**:
   - Label merged pull requests `breaking` for a major version or `enhancement` for a minor version; unlabelled changes default to patch.
   - Review the draft release notes and OpenAPI diff; do not edit `CHANGELOG.md`.

2. **Create and push a version tag**:
   ```bash
   # Create a new version tag (e.g., v1.2.3)
   git tag -a v1.2.3 -m "<highlights>"
   
   # Push the tag to trigger the workflow
   git push origin v1.2.3
   ```

3. **Monitor the workflow**:
   - Go to the "Actions" tab in your GitHub repository
   - Watch the "Publish Python 🐍 distribution 📦 to PyPI on tag" workflow run
   - The workflow will:
     - Install build tools (uv and build)
     - Test the SDK imports
     - Build the package using Python build
     - Wait for approval on the `pypi` environment
     - Publish to PyPI using a short-lived Trusted Publishing credential
     - Publish the most recent Release Drafter draft regardless of its current tag, rename it to the pushed tag, and prepend the annotated tag message under "Highlights"; or create a release with generated notes if no draft exists

### 3. Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes (e.g., `v2.0.0`)
- **MINOR**: New functionality, backward compatible (e.g., `v1.1.0`)
- **PATCH**: Bug fixes, backward compatible (e.g., `v1.0.1`)

### 4. Workflow Details

The GitHub Action workflow (`.github/workflows/publish.yml`) will:

1. **Trigger**: On version tag pushes (pattern `v*`)
2. **Environment**: Blacksmith Ubuntu 24.04 runner with Python 3.12
3. **Dependencies**: Install uv and build
4. **Testing**: Verify SDK imports correctly
5. **Build**: Create distribution packages using Python build
6. **Publish**: Upload to PyPI using Trusted Publishing after environment approval

### 5. Manual Publishing (Alternative)

If you need to publish manually:

```bash
# Install dependencies
poetry install

# Update version in pyproject.toml
poetry version 1.2.3

# Build the package
poetry build

# Publish to PyPI
poetry publish
```

### 6. Testing on Test PyPI

For testing the publishing process, you can use Test PyPI:

1. Create a TestPyPI account
2. Register a TestPyPI trusted publisher using a `testpypi` GitHub environment
3. Add a publishing job using `repository-url: https://test.pypi.org/legacy/`

### 7. Troubleshooting

**Common Issues:**

- **Permission denied**: Ensure the PyPI publisher values match the workflow and `pypi` environment exactly
- **Version conflict**: Make sure the version tag doesn't already exist on PyPI
- **Import errors**: Check that all dependencies are correctly specified in `pyproject.toml`
- **Build failures**: Verify the package structure and ensure all required files are included

**Workflow Monitoring:**
- Check the Actions tab for detailed logs
- Review the workflow output for specific error messages
- Ensure the tag format matches the expected pattern (`v*`)

## Security Notes

- Keep the build and publishing jobs separate
- Require approval on the production `pypi` environment
- Restrict production deployments to version tags
- Do not add a long-lived PyPI API token to GitHub
