"""Smoke tests for the public return-value contract."""

import matplotlib

matplotlib.use("Agg")

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

from ml_vizkit import (
    compare_models,
    show_actual_vs_predicted,
    show_class_distribution,
    show_confusion_matrix,
    show_decision_boundary,
    show_residuals,
    show_train_test_split,
)


def test_classification_helpers_return_axes() -> None:
    """Classification helpers return Axes and do not call plt.show()."""
    iris = load_iris(as_frame=True)
    X = iris.data.iloc[:, :2]
    y = iris.target

    model = LogisticRegression().fit(X, y)
    pred = model.predict(X)

    assert isinstance(show_decision_boundary(model, X, y), Axes)
    assert isinstance(show_confusion_matrix(y, pred), Axes)
    assert isinstance(show_class_distribution(y), Axes)

    plt.close("all")


def test_regression_helpers_return_axes() -> None:
    """Regression helpers return Axes."""
    X = pd.DataFrame({"x": [1.0, 2.0, 3.0, 4.0, 5.0]})
    y = pd.Series([2.0, 4.1, 5.8, 8.2, 10.1])

    model = LinearRegression().fit(X, y)
    pred = model.predict(X)

    assert isinstance(show_actual_vs_predicted(y, pred), Axes)
    assert isinstance(show_residuals(y, pred), Axes)

    plt.close("all")


def test_split_and_model_comparison_return_axes() -> None:
    """Split and comparison helpers return Axes."""
    X = pd.DataFrame(
        {
            "x": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            "y": [1.5, 2.5, 2.0, 4.5, 5.5, 5.0],
        }
    )

    X_train, X_test = train_test_split(X, test_size=0.33, random_state=42)

    assert isinstance(show_train_test_split(X_train, X_test), Axes)
    assert isinstance(compare_models({"baseline": 0.70, "candidate": 0.85}), Axes)

    plt.close("all")
