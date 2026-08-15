"""ML VizKit public API.

Reusable visualizations for inspecting, comparing, and explaining trained
machine-learning models.
"""

from ml_vizkit.classification import (
    show_class_distribution,
    show_confusion_matrix,
    show_decision_boundary,
    show_prediction_errors,
)
from ml_vizkit.comparison import compare_models, compare_splits
from ml_vizkit.inspection import show_feature_importance
from ml_vizkit.regression import show_actual_vs_predicted, show_residuals
from ml_vizkit.splits import show_train_test_split

__all__ = [
    "compare_models",
    "compare_splits",
    "show_actual_vs_predicted",
    "show_class_distribution",
    "show_confusion_matrix",
    "show_decision_boundary",
    "show_feature_importance",
    "show_prediction_errors",
    "show_residuals",
    "show_train_test_split",
]
