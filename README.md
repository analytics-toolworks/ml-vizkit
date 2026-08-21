# ML VizKit

[![PyPI](https://img.shields.io/pypi/v/ml-vizkit?logo=pypi&label=pypi)](https://pypi.org/project/ml-vizkit/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://analytics-toolworks.github.io/ml-vizkit/)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/analytics-toolworks/ml-vizkit/main/pyproject.toml&logo=python)](https://github.com/analytics-toolworks/ml-vizkit/blob/main/pyproject.toml)
![uv](https://img.shields.io/badge/uv-managed-DE5FE9)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[![CI](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/ml-vizkit/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/analytics-toolworks/ml-vizkit/security)

<img
src="https://raw.githubusercontent.com/analytics-toolworks/ml-vizkit/main/docs/images/profile.png"
alt="profile logo"
width="110">

> Reusable visualizations for inspecting, comparing, and
> explaining trained machine-learning models.

ML VizKit provides high-level Python functions for
common machine-learning visualizations.
It works with trained models, predictions, and experiment
results produced by libraries such as scikit-learn.

The package does not train models, select features,
choose algorithms, or make analytical decisions.

## Design

- Accept already-trained models, predictions, or completed experiment results.
- Reuse established visualization primitives from scikit-learn when they exist.
- Add small higher-level visualizations where the underlying libraries do not.
- Return Matplotlib `Axes` objects.
- Never call `plt.show()`.
- Keep analytical choices visible to the caller.
- Keep the implementation readable and replaceable.

## Install

```shell
uv add ml-vizkit
```

## Example

```python
from ml_vizkit import show_confusion_matrix

ax = show_confusion_matrix(y_test, y_pred)
ax.set_title("Penguin Species Classification")
```

The caller controls display and composition. In a script, for example:

```python
import matplotlib.pyplot as plt

ax = show_confusion_matrix(y_test, y_pred)
plt.show()
```

## Initial API

Classification:

- `show_decision_boundary()`
- `show_confusion_matrix()`
- `show_prediction_errors()`
- `show_class_distribution()`

Regression:

- `show_actual_vs_predicted()`
- `show_residuals()`

Model inspection:

- `show_feature_importance()`

Experiment inspection:

- `show_train_test_split()`
- `compare_splits()`
- `compare_models()`

Output:

- `save_chart()`

## Example: Classification

```python
from ml_vizkit import show_confusion_matrix

ax = show_confusion_matrix(
    y_test,
    y_pred,
)
```

## Example: Regression

```python
from ml_vizkit import show_actual_vs_predicted

ax = show_actual_vs_predicted(
    y_test,
    y_pred,
)
```

## Example: Model Inspection

```python
from ml_vizkit import show_feature_importance

ax = show_feature_importance(
    model,
    feature_names,
)
```

## Example: Save Chart

```python
from ml_vizkit import save_chart, show_confusion_matrix

ax = show_confusion_matrix(
    y_test,
    y_pred,
)

save_chart(
    ax,
    "docs/images/confusion-matrix.png",
)
```

## Example: Show Chart

```python
import matplotlib.pyplot as plt

plt.show()
```

## Developer Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/analytics-toolworks/ml-vizkit

cd ml-vizkit
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

# types, tests, docs
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Documentation

- [Documentation](https://analytics-toolworks.github.io/ml-vizkit)

## Annotations

[.annotations/annotations.md](./.annotations/annotations.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
