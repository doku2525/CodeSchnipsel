# python_aufgaben_day_007.py
"""
Python Übungsbuch Tag: 7
Thema: Dateiverarbeitung, JSON und CSV
Bemerkungen: Aufgaben zur Verarbeitung von Dateien, JSON und CSV-Dateien.
"""

"""
Aufgabe 1: Schreibe eine Funktion, die den Inhalt einer Textdatei einliest und als String zurückgibt.
"""

# Deine Lösung hier
def lies_datei(dateiname: str) -> str:
    with open(f"data/data_007/{dateiname}") as datei:
        return datei.readlines()[0]

expected_result_aufgabe_1 = "Hallo, Welt!"  # Erwartete Ausgabe für lies_datei("test.txt") (angenommen, die Datei enthält "Hallo, Welt!")
assert lies_datei("test.txt") == expected_result_aufgabe_1

"""
Aufgabe 2: Schreibe eine Funktion, die eine Liste von Strings in eine Textdatei schreibt, wobei jeder String in einer neuen Zeile steht.
"""

# Deine Lösung hier
def schreibe_zeilen(dateiname: str, zeilen: list[str]) -> None:
    with open(f"data/data_007/{dateiname}", "w") as datei:
        datei.writelines('\n'.join(zeilen))

# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Datei manuell.
schreibe_zeilen("ausgabe.txt", ["Zeile 1", "Zeile 2", "Zeile 3"])

"""
Aufgabe 3: Schreibe eine Funktion, die den Inhalt einer JSON-Datei einliest und als Python-Dictionary zurückgibt.
"""

# Deine Lösung hier
import json
def lies_json(dateiname: str) -> dict:
    with open(f"data/data_007/{dateiname}") as datei:
        return json.load(datei)


expected_result_aufgabe_3 = {"name": "Max", "alter": 30}  # Erwartete Ausgabe für lies_json("daten.json") (angenommen, die Datei enthält {"name": "Max", "alter": 30})
assert lies_json("daten.json") == expected_result_aufgabe_3

"""
Aufgabe 4: Schreibe eine Funktion, die ein Python-Dictionary in eine JSON-Datei schreibt.
"""

# Deine Lösung hier
import json
def schreibe_json(dateiname: str, daten: dict) -> None:
    with open(f"data/data_007/{dateiname}", "w") as datei:
        json.dump(daten, datei)


# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Datei manuell.
schreibe_json("ausgabe.json", {"name": "Anna", "alter": 25})
assert lies_json("ausgabe.json") == {"name": "Anna", "alter": 25}

"""
Aufgabe 5: Schreibe eine Funktion, die den Inhalt einer CSV-Datei einliest und als Liste von Dictionaries zurückgibt.
"""

# Deine Lösung hier
import csv
def lies_csv(dateiname: str) -> list[dict]:
     with open(f"data/data_007/{dateiname}") as datei:
         return list(csv.DictReader(datei))

expected_result_aufgabe_5 = [{"name": "Max", "alter": "30"}, {"name": "Anna", "alter": "25"}]  # Erwartete Ausgabe für lies_csv("daten.csv") (angenommen, die Datei enthält die entsprechenden Daten)
assert lies_csv("daten.csv") == expected_result_aufgabe_5

"""
Aufgabe 6: Schreibe eine Funktion, die eine Liste von Dictionaries in eine CSV-Datei schreibt.
"""

# Deine Lösung hier
import csv
def schreibe_csv(dateiname: str, daten: list[dict]) -> None:
    with open(f"data/data_007/{dateiname}", "w") as datei:
        writer = csv.DictWriter(datei, fieldnames=daten[0].keys())
        writer.writeheader()
        writer.writerows(daten)


# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Datei manuell.
schreibe_csv("ausgabe.csv", [{"name": "Max", "alter": "30"}, {"name": "Anna", "alter": "25"}])

"""
Aufgabe 7: Schreibe eine Funktion, die den Inhalt einer Textdatei zeilenweise einliest und die Anzahl der Zeilen zurückgibt.
"""

# Deine Lösung hier
def zaehle_zeilen(dateiname: str) -> int:
    with open(f"data/tag_004/{dateiname}") as datei:
        return len(list(datei.readlines()))


expected_result_aufgabe_7 = 3  # Erwartete Ausgabe für zaehle_zeilen("test.txt") (angenommen, die Datei enthält 3 Zeilen)
assert zaehle_zeilen("test.txt") == expected_result_aufgabe_7

"""
Aufgabe 8: Schreibe eine Funktion, die den Inhalt einer Textdatei zeilenweise einliest und die längste Zeile zurückgibt.
"""

# Deine Lösung hier
def finde_laengste_zeile(dateiname: str) -> str:
    with open(f"data/tag_004/{dateiname}") as datei:
        return max([row for row in datei.readlines()], key=lambda x: len(x)).strip()

expected_result_aufgabe_8 = "Dies ist die längste Zeile"  # Erwartete Ausgabe für finde_laengste_zeile("test.txt") (angenommen, die Datei enthält diese Zeile)
assert finde_laengste_zeile("test2.txt") == expected_result_aufgabe_8

"""
Aufgabe 9: Schreibe eine Funktion, die den Inhalt einer Textdatei zeilenweise einliest und alle Zeilen, die einen bestimmten Suchstring enthalten, zurückgibt.
"""

# Deine Lösung hier
def finde_zeilen_mit_suchstring(dateiname: str, suchstring: str) -> list[str]:
    with open(f"data/tag_004/{dateiname}") as datei:
        return [row.strip() for row in datei.readlines() if suchstring in row]


expected_result_aufgabe_9 = ["Zeile mit Suchstring"]  # Erwartete Ausgabe für finde_zeilen_mit_suchstring("test.txt", "Suchstring")
assert finde_zeilen_mit_suchstring("test2.txt", "Suchstring") == expected_result_aufgabe_9

"""
Aufgabe 10: Schreibe eine Funktion, die den Inhalt einer Textdatei zeilenweise einliest und die Zeilen in einer neuen Datei speichert, wobei jede Zeile in umgekehrter Reihenfolge geschrieben wird.
"""

# Deine Lösung hier
def speichere_zeilen_rueckwaerts(quelle: str, ziel: str) -> None:
    with open(f"data/tag_004/{quelle}") as in_file:
        with open(f"data/data_007/{ziel}", "w") as out_file:
            [out_file.write(f"{row.strip()}\n") for row in reversed(in_file.readlines())]


# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Zieldatei manuell.
speichere_zeilen_rueckwaerts("test.txt", "rueckwaerts.txt")