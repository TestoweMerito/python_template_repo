# cli.py
from logic.rectangle import area, perimeter

def main():
    print("Program do obliczania prostokąta")
    width = float(input("Podaj szerokość: "))
    height = float(input("Podaj wysokość: "))

    print(f"Pole prostokąta: {area(width, height)}")
    print(f"Obwód prostokąta: {perimeter(width, height)}")

if __name__ == "__main__":
    main()