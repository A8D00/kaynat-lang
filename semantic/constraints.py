def ensure_numeric(value):
    if not isinstance(value, int):
        raise TypeError("القيمة يجب أن تكون عددية")
