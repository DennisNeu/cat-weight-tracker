from django.core.exceptions import ValidationError
from django.utils.timezone import now


def validate_not_in_future(value):
    """Validator to ensure the date is not in the future."""
    if value > now().date():
        raise ValidationError("Date of birth cannot be in the future.")
