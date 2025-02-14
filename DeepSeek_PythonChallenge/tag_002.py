# python_aufgaben_day_002.py
"""
Python Übungsbuch Tag: 2
Thema: Listen, Strings und Funktionen
Bemerkungen: Aufgaben zur Vertiefung von Listen, Strings und Funktionen.
"""

"""
Aufgabe 1: Schreibe eine Funktion, die das größte Element in einer Liste von Zahlen zurückgibt.
"""

# Deine Lösung hier
def finde_maximum(liste: list[int]) -> int:
    return max(liste)

expected_result_aufgabe_1 = 9  # Erwartete Ausgabe für finde_maximum([3, 7, 2, 9, 5])
assert finde_maximum([3, 7, 2, 9, 5]) == expected_result_aufgabe_1

"""
Aufgabe 2: Schreibe eine Funktion, die die Anzahl der Wörter in einem String zählt.
"""

# Deine Lösung hier
def zaehle_woerter(s: str) -> int:
    return len(s.split())

expected_result_aufgabe_2 = 4  # Erwartete Ausgabe für zaehle_woerter("Das ist ein Test")
assert zaehle_woerter("Das ist ein Test") == expected_result_aufgabe_2

"""
Aufgabe 3: Schreibe eine Funktion, die alle geraden Zahlen aus einer Liste filtert.
"""

# Deine Lösung hier
def filtere_gerade_zahlen(liste: list[int]) -> list[int]:
    return [x for x in liste if x % 2 == 0]

expected_result_aufgabe_3 = [2, 4, 6]  # Erwartete Ausgabe für filtere_gerade_zahlen([1, 2, 3, 4, 5, 6])
assert filtere_gerade_zahlen([1, 2, 3, 4, 5, 6]) == expected_result_aufgabe_3


"""
Aufgabe 4: Schreibe eine Funktion, die prüft, ob ein String mit einem bestimmten Präfix beginnt.
"""

# Deine Lösung hier
def beginnt_mit(s: str, praefix: str) -> bool:
    return praefix == s[0:len(praefix)]

expected_result_aufgabe_4 = True  # Erwartete Ausgabe für beginnt_mit("Hallo Welt", "Hallo")
assert beginnt_mit("Hallo Welt", "Hallo") == expected_result_aufgabe_4

"""
Aufgabe 5: Schreibe eine Funktion, die eine Liste von Zahlen in aufsteigender Reihenfolge sortiert.
"""

# Deine Lösung hier
def sortiere_liste(liste: list[int]) -> list[int]:
    return sorted(liste)


expected_result_aufgabe_5 = [1, 2, 3, 4, 5]  # Erwartete Ausgabe für sortiere_liste([5, 3, 1, 4, 2])
assert sortiere_liste([5, 3, 1, 4, 2]) == expected_result_aufgabe_5

"""
Aufgabe 6: Schreibe eine Funktion, die die Summe aller Elemente in einer Liste von Zahlen berechnet.
"""

# Deine Lösung hier
def berechne_summe(liste: list[int]) -> int:
    return sum(liste)

expected_result_aufgabe_6 = 15  # Erwartete Ausgabe für berechne_summe([1, 2, 3, 4, 5])
assert berechne_summe([1, 2, 3, 4, 5]) == expected_result_aufgabe_6

"""
Aufgabe 7: Schreibe eine Funktion, die eine Liste von Strings in eine Liste ihrer Längen umwandelt.
"""

# Deine Lösung hier
def string_laengen(liste: list[str]) -> list[int]:
    return [len(wort) for wort in liste]


expected_result_aufgabe_7 = [5, 4, 6]  # Erwartete Ausgabe für string_laengen(["Hallo", "Welt", "Python"])
assert string_laengen(["Hallo", "Welt", "Python"]) == expected_result_aufgabe_7

"""
Aufgabe 8: Schreibe eine Funktion, die eine Liste von Zahlen in eine Liste ihrer Quadratwurzeln umwandelt.
"""

# Deine Lösung hier
import math
def quadratwurzeln(liste: list[int]) -> list[float]:
    return [math.sqrt(x) for x in liste]

expected_result_aufgabe_8 = [1.0, 2.0, 3.0]  # Erwartete Ausgabe für quadratwurzeln([1, 4, 9])
assert quadratwurzeln([1, 4, 9]) == expected_result_aufgabe_8

"""
Aufgabe 9: Schreibe eine Funktion, die eine Liste von Strings alphabetisch sortiert.
"""

# Deine Lösung hier
def sortiere_strings(liste: list[str]) -> list[str]:
    return sorted(liste)


expected_result_aufgabe_9 = ['Apfel', 'Banane', 'Zitrone']  # Erwartete Ausgabe für sortiere_strings(["Banane", "Apfel", "Zitrone"])
assert sortiere_strings(["Banane", "Apfel", "Zitrone"]) == expected_result_aufgabe_9

"""
Aufgabe 10: Schreibe eine Funktion, die die ersten n Primzahlen zurückgibt.
"""

# Deine Lösung hier
def erste_primzahlen(n: int) -> list[int]:
    pass

expected_result_aufgabe_10 = [2, 3, 5, 7, 11]  # Erwartete Ausgabe für erste_primzahlen(5)
# assert erste_primzahlen(5) == expected_result_aufgabe_10