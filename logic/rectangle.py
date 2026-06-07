# def area(width: float, height: float) -> float:
#     """Oblicza pole prostokąta."""
#     return width * height

# def perimeter(width: float, height: float) -> float:
#     """Oblicza obwód prostokąta."""
#     return 2 * (width + height)

# ...existing code...


def area(width: float, height: float) -> float:
    """Oblicza pole prostokąta."""
    return width * height


def perimeter(width: float, height: float) -> float:
    """Oblicza obwód prostokąta."""
    return 2 * (width + height)


# dodatkowy przykład użycia CLI-owej funkcji z main.py
try:
    from main import triangle_info  # zakłada, że projekt root jest na PYTHONPATH
except Exception:
    triangle_info = None  # bezpieczne fallback, żeby moduł się importował


def example_triangle_call():
    if triangle_info is None:
        print("triangle_info niedostępne (nie zaimportowano).")
        return
    info = triangle_info(3.0, 4.0, 5.0)
    print(info)
# ...existing code...
