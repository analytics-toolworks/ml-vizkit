"""Visual inspection of already-trained model characteristics."""

from collections.abc import Sequence
from typing import Any

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np


def show_feature_importance(
    model: Any,
    feature_names: Sequence[str],
    *,
    ax: Axes | None = None,
    title: str = "Feature Importance",
) -> Axes:
    """Show model-provided feature importance values.

    Args:
        model: The already-trained model exposing ``feature_importances_``.
        feature_names: The names of the features corresponding to the importance values.
        ax: The Matplotlib Axes to plot on. If None, a new Axes is created.
        title: The title of the plot.

    Returns:
        The Matplotlib Axes containing the plot.

    WHY: Importance values can help analysts investigate which features most
    influenced a fitted model.

    REQ: The model must already expose ``feature_importances_``.
    """
    if not hasattr(model, "feature_importances_"):
        msg = f"{type(model).__name__} does not expose feature_importances_."
        raise ValueError(msg)

    importance = np.asarray(model.feature_importances_, dtype=float)

    if len(importance) != len(feature_names):
        msg = "feature_names must match the model's feature count."
        raise ValueError(msg)

    order = np.argsort(importance)
    ordered_names = np.asarray(feature_names, dtype=str)[order]
    ordered_values = importance[order]

    if ax is None:
        _, ax = plt.subplots()

    ax.barh(ordered_names, ordered_values)
    ax.set_xlabel("Importance")
    ax.set_title(title)
    return ax
