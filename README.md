1. Quick Start (Uruchomienie lokalne)
Aby odpalić ten projekt na swoim komputerze, wykonaj poniższe komendy w terminalu:

Stwórz wirtualne środowisko:
python -m venv venv

Aktywuj środowisko:
Windows (PowerShell): .\venv\Scripts\Activate.ps1
Mac / Linux: source venv/bin/activate

Zainstaluj wymagane biblioteki:
pip install -r requirements.txt

2. Instrukcja uruchamiania Lint i Testów
Możesz sprawdzić poprawność kodu lokalnie za pomocą następujących komend:

Uruchomienie Lintera (Flake8):
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

Uruchomienie Testów Jednostkowych (Pytest):
PYTHONPATH=. pytest