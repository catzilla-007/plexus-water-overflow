from src.errors.liters_conversion_error import LitersConversionError


def liter_to_ml(liter: int) -> int:
    if liter < 0:
        raise LitersConversionError
    return liter * 1000
