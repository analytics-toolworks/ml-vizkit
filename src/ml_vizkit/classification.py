"""Classification visualizations.

These functions visualize trained classifiers and completed predictions.
They do not fit models or choose analytical settings.
"""

from collections.abc import Sequence
from typing import Any

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.metrics import ConfusionMatrixDisplay


def _new_axes(ax: Axes | None) -> Axes:
    """Return caller-provided axes or create new axes without rendering."""
    if ax is not None:
        return ax
    _, new_ax = plt.subplots()
    return new_ax


def show_decision_boundary(
    model: Any,
    X: pd.DataFrame,
    y: Sequence[Any] | None = None,
    *,
    ax: Axes | None = None,
    response_method: str = "auto",
    plot_method: str = "contourf",
    title: str = "Decision Boundary",
    alpha: float = 0.25,
) -> Axes:
    """Show the decision boundary for an already-trained classifier.

    WHY: A decision boundary makes the classifier's learned separation of
    feature space visible.

    REQ: X must contain exactly two numeric features.
    REQ: model must already be fitted.

    The implementation delegates boundary construction to scikit-learn's
    DecisionBoundaryDisplay and returns the Matplotlib Axes to the caller.
    """
    if X.shape[1] != 2:
        msg = "Decision-boundary plots require exactly two features."
        raise ValueError(msg)

    plot_ax = _new_axes(ax)

    DecisionBoundaryDisplay.from_estimator(
        model,
        X,
        response_method=response_method,
        plot_method=plot_method,
        alpha=alpha,
        ax=plot_ax,
    )

    # Overlay observed samples when labels are supplied. The boundary itself is
    # produced by scikit-learn; this layer makes the result easier to inspect.
    if y is not None:
        values = np.asarray(y)
        classes, codes = np.unique(values, return_inverse=True)
        plot_ax.scatter(
            X.iloc[:, 0],
            X.iloc[:, 1],
            c=codes,
            edgecolors="black",
            alpha=0.85,
        )

        # A compact legend makes class identity available without dictating
        # styling beyond the default Matplotlib color cycle.
        handles = []
        for code, label in enumerate(classes):
            handles.append(
                plt.Line2D(
                    [],
                    [],
                    marker="o",
                    linestyle="",
                    label=str(label),
                    markerfacecolor=f"C{code % 10}",
                    markeredgecolor="black",
                )
            )
        plot_ax.legend(handles=handles, title="Class")

    plot_ax.set_title(title)
    return plot_ax


def show_confusion_matrix(
    y_true: Sequence[Any],
    y_pred: Sequence[Any],
    *,
    labels: Sequence[Any] | None = None,
    normalize: str | None = None,
    ax: Axes | None = None,
    title: str = "Confusion Matrix",
) -> Axes:
    """Show a confusion matrix from completed classification predictions.

    WHY: Overall accuracy can hide which classes are being confused.

    This function delegates the matrix visualization to scikit-learn and
    returns the Matplotlib Axes.
    """
    plot_ax = _new_axes(ax)

    ConfusionMatrixDisplay.from_predictions(
        y_true,
        y_pred,
        labels=labels,
        normalize=normalize,
        ax=plot_ax,
    )
    plot_ax.set_title(title)
    return plot_ax


def show_prediction_errors(
    X: pd.DataFrame,
    y_true: Sequence[Any],
    y_pred: Sequence[Any],
    *,
    ax: Axes | None = None,
    title: str = "Classification Prediction Errors",
) -> Axes:
    """Show correct and incorrect classifications in two-feature space.

    WHY: Looking directly at mistakes can reveal overlap, unusual observations,
    and regions where a classifier struggles.

    REQ: X must contain exactly two numeric features.
    """
    if X.shape[1] != 2:
        msg = "Prediction-error plots require exactly two features."
        raise ValueError(msg)

    actual = np.asarray(y_true)
    predicted = np.asarray(y_pred)

    if len(X) != len(actual) or len(actual) != len(predicted):
        msg = "X, y_true, and y_pred must contain the same number of observations."
        raise ValueError(msg)

    correct = actual == predicted
    plot_ax = _new_axes(ax)

    plot_ax.scatter(
        X.iloc[correct, 0],
        X.iloc[correct, 1],
        marker="o",
        label="Correct",
        alpha=0.65,
    )
    plot_ax.scatter(
        X.iloc[~correct, 0],
        X.iloc[~correct, 1],
        marker="x",
        label="Incorrect",
        alpha=0.95,
    )

    plot_ax.set_xlabel(str(X.columns[0]))
    plot_ax.set_ylabel(str(X.columns[1]))
    plot_ax.set_title(title)
    plot_ax.legend()
    return plot_ax


def show_class_distribution(
    y: Sequence[Any],
    *,
    ax: Axes | None = None,
    title: str = "Class Distribution",
    x_label: str = "Class",
) -> Axes:
    """Show the number of observations in each target class.

    WHY: Class imbalance can affect training, evaluation, and interpretation.
    """
    counts = pd.Series(y).value_counts(dropna=False).sort_index()
    plot_ax = _new_axes(ax)

    plot_ax.bar(counts.index.astype(str), counts.to_numpy())
    plot_ax.set_xlabel(x_label)
    plot_ax.set_ylabel("Count")
    plot_ax.set_title(title)
    return plot_ax
