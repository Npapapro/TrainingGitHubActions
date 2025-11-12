"""Basic sanity checks for project dependencies."""

import numpy as np
import mlflow


def test_dependencies_available() -> None:
    """Ensure core dependencies are importable and expose a version."""
    assert np.__version__
    assert mlflow.__version__