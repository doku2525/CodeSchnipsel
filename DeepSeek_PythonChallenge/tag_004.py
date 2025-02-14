# python_aufgaben_day_004.py
"""
Python Übungsbuch Tag: 4
Thema: Dateiverarbeitung, Fehlerbehandlung und fortgeschrittene Funktionen
Bemerkungen: Aufgaben zur Dateiverarbeitung, Fehlerbehandlung und fortgeschrittenen Funktionen.
"""

"""
Aufgabe 1: Schreibe eine Funktion, die den Inhalt einer Textdatei zeilenweise einliest und als Liste von Strings zurückgibt.
"""

# Deine Lösung hier
def lies_datei(dateiname: str) -> list[str]:
    # result = []
    with open(dateiname) as datei:  # "r" ist der default_modus
        result = datei.readlines()  # In den Zeilen wird das "\n" mit eingelesen
    return [zeile.strip() for zeile in result]
def lies_datei2(dateiname: str) -> list[str]:
    # result = []
    with open(dateiname) as datei:  # "r" ist der default_modus
        return [zeile.strip() for zeile in datei.readlines()]  # In den Zeilen wird das "\n" mit eingelesen

expected_result_aufgabe_1 = ["Zeile 1", "Zeile 2", "Zeile 3"]  # Erwartete Ausgabe für lies_datei("test.txt") (angenommen, die Datei enthält diese Zeilen)
assert lies_datei("data/tag_004/test.txt") == expected_result_aufgabe_1
assert lies_datei2("data/tag_004/test.txt") == expected_result_aufgabe_1

"""
Aufgabe 2: Schreibe eine Funktion, die den Inhalt einer Textdatei in eine andere Datei kopiert.
"""

# Deine Lösung hier
def kopiere_datei(quelle: str, ziel: str) -> None:
    with open(quelle) as q:
        with open(ziel, "w") as z:
            z.writelines(q.readlines())


# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Zieldatei manuell.
kopiere_datei("data/tag_004/test.txt", "data/tag_004/kopie.txt")
assert lies_datei("data/tag_004/kopie.txt") == expected_result_aufgabe_1

"""
Aufgabe 3: Schreibe eine Funktion, die eine Liste von Zahlen in eine Datei schreibt, wobei jede Zahl in einer neuen Zeile steht.
"""

# Deine Lösung hier
def schreibe_zahlen_in_datei(dateiname: str, zahlen: list[int]) -> None:
    with open(dateiname, "w") as datei:
        datei.write(''.join([f"{zahl}\n" for zahl in zahlen]).strip())

# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Datei manuell.
expected_result_aufgabe_3 = [1, 2, 3, 4, 5]
schreibe_zahlen_in_datei("data/tag_004/zahlen.txt", [1, 2, 3, 4, 5])
assert [int(zahl) for zahl in lies_datei("data/tag_004/zahlen.txt")] == expected_result_aufgabe_3

"""
Aufgabe 4: Schreibe eine Funktion, die eine Datei zeilenweise einliest und die Anzahl der Zeilen zurückgibt.
"""

# Deine Lösung hier
def zaehle_zeilen(dateiname: str) -> int:
    with open(dateiname) as datei:
        result = 0
        while inhalt := datei.readline():
            result += 1
    return result
def zaehle_zeilen2(dateiname: str) -> int:
    with open(dateiname) as datei:
        return [index for index, _ in enumerate(datei.readlines(), 1)][-1]

expected_result_aufgabe_4 = 3  # Erwartete Ausgabe für zaehle_zeilen("test.txt") (angenommen, die Datei enthält 3 Zeilen)
assert zaehle_zeilen("data/tag_004/test.txt") == expected_result_aufgabe_4
assert zaehle_zeilen2("data/tag_004/test.txt") == expected_result_aufgabe_4

"""
Aufgabe 5: Schreibe eine Funktion, die eine Datei einliest und die Anzahl der Wörter in der Datei zurückgibt.
"""

# Deine Lösung hier
def zaehle_woerter_in_datei(dateiname: str) -> int:
    with open(dateiname) as datei:
        return sum([len(zeile.split()) for zeile in datei.readlines()])


expected_result_aufgabe_5 = 6  # Erwartete Ausgabe für zaehle_woerter_in_datei("test.txt") (angenommen, die Datei enthält 6 Wörter)
assert zaehle_woerter_in_datei("data/tag_004/test.txt") == expected_result_aufgabe_5

"""
Aufgabe 6: Schreibe eine Funktion, die eine Datei einliest und die Anzahl der Zeichen (inkl. Leerzeichen) zurückgibt.
"""

# Deine Lösung hier
def zaehle_zeichen_in_datei(dateiname: str) -> int:
    with open(dateiname) as datei:
        return sum([len(zeile.strip()) for zeile in datei.readlines()])

expected_result_aufgabe_6 = 21  # Erwartete Ausgabe für zaehle_zeichen_in_datei("test.txt") (angenommen, die Datei enthält 20 Zeichen)
assert zaehle_zeichen_in_datei("data/tag_004/test.txt") == expected_result_aufgabe_6

"""
Aufgabe 7: Schreibe eine Funktion, die eine Datei einliest und die längste Zeile zurückgibt.
"""

# Deine Lösung hier
def finde_laengste_zeile(dateiname: str) -> str:
    with open(dateiname) as datei:
        return sorted([(len(zeile), zeile.strip()) for zeile in datei.readlines()],
                      key=lambda x: x[0],
                      reverse=True
                      )[0][1]

expected_result_aufgabe_7 = "Dies ist die längste Zeile"  # Erwartete Ausgabe für finde_laengste_zeile("test.txt") (angenommen, die Datei enthält diese Zeile)
assert finde_laengste_zeile("data/tag_004/test2.txt") == expected_result_aufgabe_7

"""
Aufgabe 8: Schreibe eine Funktion, die eine Datei einliest und alle Zeilen, die einen bestimmten Suchstring enthalten, zurückgibt.
"""

# Deine Lösung hier
def finde_zeilen_mit_suchstring(dateiname: str, suchstring: str) -> list[str]:
    with open(dateiname) as datei:
        return [zeile.strip() for zeile in datei.readlines() if suchstring in zeile]

expected_result_aufgabe_8 = ["Zeile mit Suchstring"]  # Erwartete Ausgabe für finde_zeilen_mit_suchstring("test.txt", "Suchstring")
assert finde_zeilen_mit_suchstring("data/tag_004/test2.txt", "Suchstring") == expected_result_aufgabe_8

"""
Aufgabe 9: Schreibe eine Funktion, die eine Datei einliest und alle Zeilen in umgekehrter Reihenfolge zurückgibt.
"""

# Deine Lösung hier
def lies_datei_rueckwaerts(dateiname: str) -> list[str]:
    with open(dateiname) as datei:
        return list(reversed([zeile.strip() for zeile in datei.readlines()]))


expected_result_aufgabe_9 = ["Zeile 3", "Zeile 2", "Zeile 1"]  # Erwartete Ausgabe für lies_datei_rueckwaerts("test.txt") (angenommen, die Datei enthält diese Zeilen)
assert lies_datei_rueckwaerts("data/tag_004/test.txt") == expected_result_aufgabe_9

"""
Aufgabe 10: Schreibe eine Funktion, die eine Datei einliest und die Zeilen in einer neuen Datei speichert, wobei jede Zeile in umgekehrter Reihenfolge geschrieben wird.
"""

# Deine Lösung hier
def speichere_zeilen_rueckwaerts(quelle: str, ziel: str) -> None:
    with open(quelle) as datei:
        liste = [zeile.strip() for zeile in datei.readlines()]
    with open(ziel, "w") as datei:
        datei.writelines('\n'.join(reversed(liste)).strip())


# Keine erwartete Ausgabe, da die Funktion keine Rückgabe hat. Überprüfe die Zieldatei manuell.
speichere_zeilen_rueckwaerts("data/tag_004/test.txt", "data/tag_004/rueckwaerts.txt")
assert lies_datei("data/tag_004/rueckwaerts.txt") == expected_result_aufgabe_9