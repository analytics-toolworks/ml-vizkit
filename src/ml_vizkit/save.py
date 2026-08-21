"""Save visualization outputs."""

from pathlib import Path

from matplotlib.axes import Axes


def save_chart(
    ax: Axes,
    path: str | Path,
    *,
    bbox_inches: str | None = "tight",
) -> None:
    """Save chart.

    Args:
        ax (Axes): The matplotlib Axes object containing the chart to save.
        path (str | Path): The file path where the chart should be saved.
        bbox_inches (str | None, optional): The bounding box in inches. Defaults to "tight".

    Raises:
        ValueError: If the Axes is not attached to a Figure.

    """
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure = ax.get_figure(root=True)
    if figure is None:
        raise ValueError("Axes must be attached to a Figure before saving.")

    figure.savefig(output_path, bbox_inches=bbox_inches)
