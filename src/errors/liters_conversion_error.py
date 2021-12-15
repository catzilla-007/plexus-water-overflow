class LitersConversionError(ValueError):
    def __init__(self, message="Liters should be a non-negative number"):
        super().__init__(message)
