# Week 8: Unit Testing
# Calculate Tax

def calculate_tax(amount):
    """
    Calculate 15% tax on an amount.
    """

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    tax = amount * 0.15

    return tax