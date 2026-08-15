# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.0.1] - 2026-08-15

- initial versioned release

---

## Notes on Versioning and Releases

- We use **SemVer**:
  - **MAJOR** - breaking changes
  - **MINOR** - backward-compatible
  - **PATCH** - fixes, documentation, tooling
- Versions are driven by git tags. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

## Release Procedure (Required)

Follow these steps exactly when creating a new release.

### Task 1. Update release metadata (manual edits)

1. Update `CITATION.cff`: change `version` and `date-released`
2. Update `CHANGELOG.md`: move from unreleased, add entry, update links
3. Update `pyproject.toml`: update `[tool.hatch.version] fallback-version`

### Task 2. Validate

```shell
uvx pup-clean@latest --delete
uvx pup-up@latest --write
.\sit.ps1

# OR

uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

# optional: generate and check CODEOWNERS
# based on roles defined in .accountability/surfaces.toml
uvx se-codeowners generate --strict --output .github/CODEOWNERS
uvx se-codeowners check

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

npx markdownlint-cli2 --fix
uvx cffconvert --validate

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Task 3. Commit, push, tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

### Task 4. Verify tag consistency

```shell
uvx se-manifest-schema check-version --require-tag
```

Confirms CITATION.cff version matches the pushed git tag.
Run this after `git push origin vX.Y.Z`; it will fail before that point.

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/analytics-toolworks/ml-vizkit/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/analytics-toolworks/ml-vizkit/releases/tag/v0.0.1

<!-- markdownlint-enable MD024 -->
