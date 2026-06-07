# ...existing code...
import argparse
import math
from typing import Dict, Any


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)


def triangle_type(a: float, b: float, c: float) -> str:
    if not is_valid_triangle(a, b, c):
        return "niepoprawny"
    if a == b == c:
        return "równoboczny"
    if a == b or b == c or a == c:
        return "równoramienny"
    return "różnoboczny"


def triangle_area(a: float, b: float, c: float) -> float:
    if not is_valid_triangle(a, b, c):
        raise ValueError("Boki nie tworzą trójkąta")
    s = (a + b + c) / 2.0
    return math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))


def triangle_info(a: float, b: float, c: float) -> Dict[str, Any]:
    valid = is_valid_triangle(a, b, c)
    return {
        "valid": valid,
        "sides": (a, b, c),
        "perimeter": (a + b + c) if valid else None,
        "area": triangle_area(a, b, c) if valid else None,
        "type": triangle_type(a, b, c),
    }


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CLI do obliczeń trójkąta (boki).")
    p.add_argument("a", type=float, help="długość boku a")
    p.add_argument("b", type=float, help="długość boku b")
    p.add_argument("c", type=float, help="długość boku c")
    return p


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    info = triangle_info(args.a, args.b, args.c)

    if not info["valid"]:
        print("Boki nie tworzą poprawnego trójkąta.")
        return

    print(f"Boki: {info['sides']}")
    print(f"Obwód: {info['perimeter']}")
    print(f"Pole: {info['area']:.6f}")
    print(f"Typ: {info['type']}")


if __name__ == "__main__":
    main()
# ...existing code...
