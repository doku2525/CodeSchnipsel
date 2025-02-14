# python_aufgaben_day_001.py

""" 
Python Übungsbuch Tag: 1
Thema: Grundlagen
Bemerkungen: Einfache Aufgaben zur Wiederholung von Grundkonzepten.
"""

"""
Aufgabe 1: Schreibe eine Funktion, die die Summe zweier Zahlen berechnet.
"""


# Deine Lösung hier
def summe(x: int, y:int) -> int:
    return x + y


expected_result_aufgabe_1 = 7  # Erwartete Ausgabe für summe(3, 4)
assert summe(3,4) == expected_result_aufgabe_1, f"Aufgabe 1 falsch!"


"""
Aufgabe 2: Schreibe eine Funktion, die prüft, ob eine Zahl gerade ist.
"""
# Deine Lösung hier
def ist_gerade(x: int) -> bool:
    return x % 2 == 0

expected_result_aufgabe_2 = True  # Erwartete Ausgabe für ist_gerade(10)
assert ist_gerade(10) == expected_result_aufgabe_2, "Aufgabe 2 falsch!"


"""
Aufgabe 3: Schreibe eine Funktion, die den größeren von zwei Zahlen zurückgibt.
"""
# Deine Lösung hier
def groessere_zahl(x: int, y: int) -> int:
    return max(x, y)

expected_result_aufgabe_3 = 9  # Erwartete Ausgabe für groessere_zahl(5, 9)
assert groessere_zahl(5, 9) == expected_result_aufgabe_3, f"Aufgabe 3 falsch!"


"""
Aufgabe 4: Schreibe eine Funktion, die eine Liste von Zahlen in umgekehrter Reihenfolge zurückgibt.
"""

# Deine Lösung hier
def umgekehrte_liste(liste: list[int]) -> list[int]:
    return list(reversed(liste))  # reversed liefert keine Liste, sondern eine Iterator

expected_result_aufgabe_4 = [4, 3, 2, 1]  # Erwartete Ausgabe für umgekehrte_liste([1, 2, 3, 4])
assert umgekehrte_liste([1, 2, 3, 4]) == expected_result_aufgabe_4, f"Aufgabe 4 falsch!"


"""
Aufgabe 5: Schreibe eine Funktion, die prüft, ob ein String ein Palindrom ist.
"""
# Deine Lösung hier
def ist_palindrom(wort: str) -> bool:
    return all([a == b for a, b in zip(wort, list(reversed(wort)))])

expected_result_aufgabe_5 = True  # Erwartete Ausgabe für ist_palindrom("anna")
assert ist_palindrom("anna") == expected_result_aufgabe_5


"""
Aufgabe 6: Schreibe eine Funktion, die die Fakultät einer Zahl berechnet.
"""
# Deine Lösung hier
def fakultaet(x: int) -> int:
    match x:
        case 0: return 1
        case _: return x * fakultaet(x-1)

expected_result_aufgabe_6 = 120  # Erwartete Ausgabe für fakultaet(5)
assert fakultaet(5) == expected_result_aufgabe_6


"""
Aufgabe 7: Schreibe eine Funktion, die die Anzahl der Vokale in einem String zählt.
"""

# Deine Lösung hier
def zaehle_vokale(text: str) -> int:
    vokale = "aeuio".upper()
    if text == '':
        return 0
    if text[0].upper() in vokale:
        return 1 + zaehle_vokale(text[1:])
    return zaehle_vokale(text[1:])

def zaehle_vokale2(text: str) -> int:
    vokale = "aeuio".upper()
    return sum(1 for letter in text if letter.upper() in vokale)

expected_result_aufgabe_7 = 3  # Erwartete Ausgabe für zaehle_vokale("Hallo Welt")
assert zaehle_vokale("Hallo Welt") == expected_result_aufgabe_7
assert zaehle_vokale2("Hallo Welt") == expected_result_aufgabe_7


"""
Aufgabe 8: Schreibe eine Funktion, die eine Liste von Zahlen in eine Liste ihrer Quadrate umwandelt.
"""
# Deine Lösung hier
def quadrate(liste: list[int]) -> list[int]:
    return list(map(lambda x: x * x, liste))

def quadrate2(liste: list[int]) -> list[int]:
    return [x * x for x in liste]

expected_result_aufgabe_8 = [1, 4, 9, 16]  # Erwartete Ausgabe für quadrate([1, 2, 3, 4])
assert quadrate([1, 2, 3, 4]) == expected_result_aufgabe_8
assert quadrate2([1, 2, 3, 4]) == expected_result_aufgabe_8


"""
Aufgabe 9: Schreibe eine Funktion, die eine Liste von Strings alphabetisch sortiert.
"""

# Deine Lösung hier
def sortiere_strings(liste:list[str]) -> list[str]:
    return sorted(liste)

expected_result_aufgabe_9 = ['Apfel', 'Banane', 'Zitrone']  # Erwartete Ausgabe für sortiere_strings(["Banane", "Apfel", "Zitrone"])
assert sortiere_strings(["Banane", "Apfel", "Zitrone"]) == expected_result_aufgabe_9

"""
Aufgabe 10: Schreibe eine Funktion, die die ersten n Zahlen der Fibonacci-Folge zurückgibt.
"""

# Deine Lösung hier
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

expected_result_aufgabe_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Erwartete Ausgabe für fibonacci(10)
assert fibonacci(10) == expected_result_aufgabe_10