# Releases

## Version Format

PyMCPX uses semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: breaking API changes (tool renames, field removals, removed exports)
- **MINOR**: new tools, new services, backwards-compatible additions
- **PATCH**: bug fixes, documentation, internal refactors

## Release Process

```bash
# 1. Ensure all tests pass
python scripts/test.py --cov

# 2. Bump version and create tag
python scripts/release.py patch   # or minor / major
python scripts/release.py --dry-run minor  # preview first

# 3. GitHub Actions publish.yml triggers automatically on tag push
```

## Changelog

Maintain `CHANGELOG.md` with entries for each release:

```markdown
## [0.2.0] - 2024-07-01
### Added
- Slack service with SlackSendMessageTool

### Changed
- GitHubConfig now accepts optional base_url for enterprise

## [0.1.0] - 2024-06-01
### Added
- Initial release with GitHub service
```

## PyPI Trusted Publishing

The `publish.yml` workflow uses PyPI's **trusted publishing** (OIDC).
No `PYPI_TOKEN` secret is needed.
Setup once at: https://pypi.org/manage/account/publishing/

## Breaking Change Policy

Breaking changes require:
1. Major version bump
2. Deprecation notice in previous minor release (where practical)
3. Migration guide in CHANGELOG.md
4. Regression test updates to match new contract
