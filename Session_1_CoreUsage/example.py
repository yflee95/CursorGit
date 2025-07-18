def get_discounted_price(price, discount_percent):
    """
    Calculate the final price after applying a percentage discount.

    The function now uses a try/except pattern so that *eight* common
    error scenarios are handled gracefully by returning ``0`` instead of
    raising an exception:

    1. ``price`` is ``None``.
    2. ``discount_percent`` is ``None``.
    3. ``price`` cannot be converted to ``float`` (e.g., a non-numeric string).
    4. ``discount_percent`` cannot be converted to ``float``.
    5. ``price`` is less than or equal to ``0``.
    6. ``discount_percent`` is negative.
    7. ``discount_percent`` is greater than ``100`` (more than a 100 % discount).
    8. Any other unexpected error during the calculation (captured by a
       catch-all ``Exception`` clause).

    Parameters
    ----------
    price : float | int | str | None
        The original price of the item. Accepts any value that can be cast
        to ``float`` and is greater than ``0``.
    discount_percent : float | int | str | None
        Discount to apply, expressed as a percentage (e.g., ``20`` for 20 %).
        Accepts any value that can be cast to ``float`` and is between
        ``0`` and ``100`` (inclusive).

    Returns
    -------
    float
        The price after the discount has been applied, **or ``0`` if any of
        the above error cases occur**.
    """
    try:
        # Attempt to coerce inputs to float to support numeric strings, etc.
        price = float(price)
        discount_percent = float(discount_percent)

        # Logical validations
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        if discount_percent < 0:
            raise ValueError("Discount percent must be non-negative")
        if discount_percent > 100:
            raise ValueError("Discount percent cannot exceed 100")

        return price - (price * discount_percent / 100)

    # Handle conversion failures and logical validation failures
    except (TypeError, ValueError):
        return 0
    # Catch-all for any other unforeseen errors
    except Exception:
        return 0
