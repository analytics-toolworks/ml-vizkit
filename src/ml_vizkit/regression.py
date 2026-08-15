"""Regression visualizations for completed predictions."""

from collections.abc import Sequence

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import PredictionErrorDisplay

type Numeric1D = Sequence[float] | np.ndarray | pd.Series


def _new_axes(ax: Axes | None) -> Axes:
    """Return caller-provided axes or create new axes without rendering."""
    if ax is not None:
        return ax
    _, new_ax = plt.subplots()
    return new_ax


def show_actual_vs_predicted(
    y_true: Numeric1D,
    y_pred: Numeric1D,
    *,
    ax: Axes | None = None,
    title: str = "Actual vs. Predicted",
) -> Axes:
    """Show actual versus predicted regression values.

    WHY: Good predictions should generally fall near the identity line.

    The implementation delegates to scikit-learn's PredictionErrorDisplay.
    """
    plot_ax = _new_axes(ax)

    PredictionErrorDisplay.from_predictions(
        y_true,
        y_pred,
        kind="actual_vs_predicted",
        ax=plot_ax,
    )
    plot_ax.set_title(title)
    return plot_ax


def show_residuals(
    y_true: Numeric1D,
    y_pred: Numeric1D,
    *,
    ax: Axes | None = None,
    title: str = "Residuals vs. Predicted",
) -> Axes:
    """Show regression residuals against predicted values.

    WHY: Residual plots can reveal systematic error patterns, changing
    variance, and unusual observations.

    The implementation delegates to scikit-learn's PredictionErrorDisplay.
    """
    plot_ax = _new_axes(ax)

    PredictionErrorDisplay.from_predictions(
        y_true,
        y_pred,
        kind="residual_vs_predicted",
        ax=plot_ax,
    )
    plot_ax.set_title(title)
    return plot_ax
