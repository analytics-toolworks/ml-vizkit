# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.1.0] - 2026-08-20

### Added

- Added `save_chart()` for saving Matplotlib `Axes` to a specified path.
- Added documentation and examples for the create / save / show workflow.
- Added additional public API docstrings.

---

## [0.0.2] - 2026-08-16

## Added

- Add copy/paste leakage check

## Fixed

- README.md links

---

## [0.0.1] - 2026-08-15

### Added

- Initial public release of `ml-vizkit`.
- Added reusable visualization utilities for inspecting, comparing, and
  explaining trained machine-learning models and completed experiments.
- Added classification visualizations:
  - `show_decision_boundary()`
  - `show_confusion_matrix()`
  - `show_prediction_errors()`
  - `show_class_distribution()`
- Added regression visualizations:
  - `show_actual_vs_predicted()`
  - `show_residuals()`
- Added model inspection with `show_feature_importance()`.
- Added experiment visualizations:
  - `show_train_test_split()`
  - `compare_splits()`
  - `compare_models()`
- Visualization functions return Matplotlib `Axes` objects so callers retain
  control over rendering, composition, annotation, and export.
- Added typed public package support with `py.typed`.
- Added tests verifying the visualization return contract.
- Added project documentation and API documentation.
- Added Python 3.14 project configuration.
- Added Ruff, ty, pytest, pre-commit, and CI validation.
- Added Zensical documentation configuration and deployment workflows.
- Added PyPI release and pre-release workflows.

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
.\sit.ps1

# OR

uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

npx markdownlint-cli2 --fix
uvx cffconvert --validate

uv run ty check
uv run python -m pytest
uv run python -m zensical build

uv run python -c "import shutil; from pathlib import Path; shutil.rmtree(Path('dist'), ignore_errors=True)"

uv build
uvx twine check dist/*
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

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/analytics-toolworks/ml-vizkit/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/analytics-toolworks/ml-vizkit/releases/tag/v0.1.0
[0.0.2]: https://github.com/analytics-toolworks/ml-vizkit/releases/tag/v0.0.2
[0.0.1]: https://github.com/analytics-toolworks/ml-vizkit/releases/tag/v0.0.1

<!-- markdownlint-enable MD024 -->
