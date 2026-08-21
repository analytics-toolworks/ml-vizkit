"""Visualizations for already-created train/test partitions."""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd


def show_train_test_split(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    *,
    ax: Axes | None = None,
    title: str = "Train/Test Split",
) -> Axes:
    """Show which observations were assigned to training and testing.

    Args:
        X_train: The training feature DataFrame containing exactly two numeric features.
        X_test: The testing feature DataFrame containing exactly two numeric features.
        ax: The Matplotlib Axes to plot on. If None, a new Axes is created.
        title: The title of the plot.

    Returns:
        The Matplotlib Axes containing the plot.

    WHY: Seeing the actual partition makes random splitting concrete instead
    of treating the random seed as unexplained boilerplate.

    REQ: Both frames must contain the same two numeric features.
    """
    if X_train.shape[1] != 2 or X_test.shape[1] != 2:
        msg = "Train/test split plots require exactly two features."
        raise ValueError(msg)

    if list(X_train.columns) != list(X_test.columns):
        msg = "Training and test data must contain the same features in the same order."
        raise ValueError(msg)

    if ax is None:
        _, ax = plt.subplots()

    feature_x, feature_y = X_train.columns

    ax.scatter(
        X_train[feature_x],
        X_train[feature_y],
        marker="o",
        label="Train",
        alpha=0.65,
    )
    ax.scatter(
        X_test[feature_x],
        X_test[feature_y],
        marker="x",
        label="Test",
        alpha=0.95,
    )

    ax.set_xlabel(str(feature_x))
    ax.set_ylabel(str(feature_y))
    ax.set_title(title)
    ax.legend()
    return ax
