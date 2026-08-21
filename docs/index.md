# ml-vizkit

<img
src="https://raw.githubusercontent.com/analytics-toolworks/ml-vizkit/main/docs/images/profile.png"
alt="profile logo"
width="110">

`ml-vizkit` provides small, reusable visualization utilities for inspecting,
comparing, and explaining trained machine-learning models and completed
experiments.

It is designed for analysts who want clear, consistent visual evidence without
rewriting common plotting mechanics for every project.

## Purpose

Applied machine-learning work repeatedly uses the same kinds of visualizations:

- decision boundaries
- confusion matrices
- prediction errors
- class distributions
- actual-versus-predicted plots
- residual plots
- feature importance
- train/test splits
- model comparisons
- split comparisons

`ml-vizkit` provides concise functions for these common views so analysts can
spend more time interpreting models and experimental results.

## Design

`ml-vizkit` follows a small set of design rules:

- work with already-trained models, predictions, and completed experiment results
- do not train models or choose models, features, metrics, or experimental settings
- use established Python visualization and machine-learning libraries underneath
- return Matplotlib `Axes` objects rather than rendering automatically
- provide `save_chart()` for convenient chart export
- keep visualizations inspectable, adaptable, and easy to replace
- automate plotting mechanics without reducing analytical agency

The caller retains control over display, composition, annotation, export, and
interactive use.

## Example

```python
import matplotlib.pyplot as plt

from ml_vizkit import save_chart, show_decision_boundary

ax = show_decision_boundary(
    model,
    X_test,
    y_test,
)

ax.set_title("Penguin Species Decision Boundary")

save_chart(
    ax,
    "docs/images/decision-boundary.png",
)

plt.show()
```

## See Also

- [API](./api.md)
