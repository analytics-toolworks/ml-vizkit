"""Higher-level visual comparisons of completed ML experiments."""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

from ml_vizkit.splits import show_train_test_split


@dataclass(frozen=True, slots=True)
class SplitView:
    """Data needed to visualize one already-created train/test split."""

    label: str
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    score: float | None = None


def compare_splits(
    splits: Sequence[SplitView],
) -> tuple[Axes, ...]:
    """Create one train/test visualization per completed split.

    WHY: Comparing several partitions makes sampling variability visible.

    This function does not create splits or train models. Each visualization is
    created in its own figure, and all Axes are returned to the caller.
    """
    axes: list[Axes] = []

    for split in splits:
        _, ax = plt.subplots()

        title = split.label
        if split.score is not None:
            title = f"{title} | score={split.score:.3f}"

        show_train_test_split(
            split.X_train,
            split.X_test,
            ax=ax,
            title=title,
        )
        axes.append(ax)

    return tuple(axes)


def compare_models(
    scores: Mapping[str, float],
    *,
    ax: Axes | None = None,
    metric_name: str = "Score",
    title: str = "Model Comparison",
) -> Axes:
    """Compare evaluation scores from already-completed model experiments.

    WHY: A consistent visual basis helps analysts compare models evaluated with
    the same metric and experimental conditions.

    NOTE: This function assumes the caller has already established that the
    supplied scores are meaningfully comparable.
    """
    if not scores:
        msg = "scores must contain at least one model result."
        raise ValueError(msg)

    if ax is None:
        _, ax = plt.subplots()

    names = list(scores)
    values = [scores[name] for name in names]

    ax.bar(names, values)
    ax.set_ylabel(metric_name)
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=30)
    return ax
