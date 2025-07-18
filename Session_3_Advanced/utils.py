from validation import validate_bmi_inputs

def calculate_bmi(height, weight):
    """Return Body-Mass Index rounded to 2 dp or ``None`` if inputs are invalid.
    
    Parameters
    ----------
    height, weight : int | float | str
        Inputs convertible to float and > 0.
    """
    try:
        height_f, weight_f = validate_bmi_inputs(height, weight)
        return round(weight_f / (height_f ** 2), 2)
    except (ValueError, ZeroDivisionError):
        return None
