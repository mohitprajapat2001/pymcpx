# Releases

## Version Format

PyMCPX uses semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: breaking API changes (tool renames, field removals, removed exports)
- **MINOR**: new tools, new services, backwards-compatible additions
- **PATCH**: bug fixes, documentation, internal refactors

## Release Process

```bash
# 1. Ensure all tests pass
pytest --cov

# 2. Bump version and create tag
# Update version in pyproject.toml manually, then:
git tag v0.1.0
git push origin v0.1.0
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

## PyPI Publishing

To publish to PyPI, configure trusted publishing on PyPI, then:

```bash
pip install hatch
hatch build
hatch publish
```

## Breaking Change Policy

Breaking changes require:
1. Major version bump
2. Deprecation notice in previous minor release (where practical)
3. Migration guide in CHANGELOG.md
