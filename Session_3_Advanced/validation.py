"""Validation utilities for BMI calculations."""

from typing import Tuple, Optional


def _to_positive_float(value, name: str) -> float:
    """Convert *value* to float and ensure it is positive (>0).

    Parameters
    ----------
    value : Any
        The raw value to convert.
    name : str
        The name of the parameter (for error messages).

    Returns
    -------
    float
        The validated positive float.

    Raises
    ------
    ValueError
        If conversion fails or the number is not positive.
    """
    try:
        converted = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a number, got {value!r}") from None

    if converted <= 0:
        raise ValueError(f"{name} must be > 0, got {converted}")

    return converted


def validate_bmi_inputs(height, weight) -> Tuple[float, float]:
    """Validate and convert BMI *height* and *weight* inputs.

    Both inputs must be convertible to ``float`` and strictly greater than 0.

    Returns the converted (height, weight) tuple.
    """
    return _to_positive_float(height, "height"), _to_positive_float(weight, "weight") 