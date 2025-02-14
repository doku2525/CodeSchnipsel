# python_aufgaben_day_003.py
"""
Python Übungsbuch Tag: 3
Thema: Dictionaries, Sets und fortgeschrittene Listenoperationen
Bemerkungen: Aufgaben zur Vertiefung von Dictionaries, Sets und Listenoperationen.
"""

"""
Aufgabe 1: Schreibe eine Funktion, die die Häufigkeit jedes Buchstabens in einem String zählt und als Dictionary zurückgibt.
"""
# Deine Lösung hier
def zaehle_buchstaben(s: str) -> dict[str, int]:
    if s == '':
        return {}
    return zaehle_buchstaben(s[1:]) | {s[0]: zaehle_buchstaben(s[1:]).get(s[0], 0) + 1}

def zaehle_buchstaben2(s: str) -> dict[str, int]:
    from collections import defaultdict
    letters = defaultdict(int)
    for letter in s:
        letters[letter] += 1
    return letters

def zaehle_buchstaben3(s: str) -> dict[str, int]:
    return {letter: s.count(letter) for letter in s}

expected_result_aufgabe_1 = {'H': 1, 'a': 1, 'l': 2, 'o': 1}  # Erwartete Ausgabe für zaehle_buchstaben("Hallo")
assert zaehle_buchstaben("Hallo") == expected_result_aufgabe_1
assert zaehle_buchstaben2("Hallo") == expected_result_aufgabe_1
assert zaehle_buchstaben3("Hallo") == expected_result_aufgabe_1

"""
Aufgabe 2: Schreibe eine Funktion, die zwei Dictionaries zusammenführt. Bei gleichen Schlüsseln sollen die Werte addiert werden.
"""

# Deine Lösung hier
def merge_dicts(d1: dict, d2: dict) -> dict:
    return {k: d1.get(k, 0) + d2.get(k, 0) for k, _ in (d1 | d2).items()}

expected_result_aufgabe_2 = {'a': 3, 'b': 5, 'c': 4}  # Erwartete Ausgabe für merge_dicts({'a': 1, 'b': 2}, {'a': 2, 'b': 3, 'c': 4})
assert merge_dicts({'a': 1, 'b': 2}, {'a': 2, 'b': 3, 'c': 4}) == expected_result_aufgabe_2

"""
Aufgabe 3: Schreibe eine Funktion, die die gemeinsamen Elemente zweier Listen zurückgibt.
"""

# Deine Lösung hier
def gemeinsame_elemente(liste1: list, liste2: list) -> list:
    return [elem for elem in liste1 if elem in liste2]
def gemeinsame_elemente2(liste1: list, liste2: list) -> list:
    return list(set(liste1) & set(liste2))


expected_result_aufgabe_3 = [2, 3]  # Erwartete Ausgabe für gemeinsame_elemente([1, 2, 3], [2, 3, 4])
assert gemeinsame_elemente([1, 2, 3], [2, 3, 4]) == expected_result_aufgabe_3
assert gemeinsame_elemente2([1, 2, 3], [2, 3, 4]) == expected_result_aufgabe_3

"""
Aufgabe 4: Schreibe eine Funktion, die die eindeutigen Elemente einer Liste zurückgibt.
"""

# Deine Lösung hier
def eindeutige_elemente(liste: list) -> list:
    return list(set(liste))

expected_result_aufgabe_4 = [1, 2, 3, 4]  # Erwartete Ausgabe für eindeutige_elemente([1, 2, 2, 3, 4, 4])
assert eindeutige_elemente([1, 2, 2, 3, 4, 4]) == expected_result_aufgabe_4

"""
Aufgabe 5: Schreibe eine Funktion, die prüft, ob ein String alle Buchstaben des Alphabets enthält (ein Pangramm ist).
"""

# Deine Lösung hier
def ist_pangramm(s: str) -> bool:
    return 26 == len([letter for letter in set(s.upper()) if letter.isalpha()])
def ist_pangramm2(s: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(s.lower())

expected_result_aufgabe_5 = True  # Erwartete Ausgabe für ist_pangramm("The quick brown fox jumps over the lazy dog")
assert ist_pangramm("The quick brown fox jumps over the lazy dog") == expected_result_aufgabe_5
assert ist_pangramm2("The quick brown fox jumps over the lazy dog") == expected_result_aufgabe_5

"""
Aufgabe 6: Schreibe eine Funktion, die die Schlüssel und Werte eines Dictionaries vertauscht.
"""

# Deine Lösung hier
def vertausche_schluessel_werte(d: dict) -> dict:
    return {v: k for k, v in d.items()}


expected_result_aufgabe_6 = {1: 'a', 2: 'b', 3: 'c'}  # Erwartete Ausgabe für vertausche_schluessel_werte({'a': 1, 'b': 2, 'c': 3})
assert vertausche_schluessel_werte({'a': 1, 'b': 2, 'c': 3}) == expected_result_aufgabe_6

"""
Aufgabe 7: Schreibe eine Funktion, die die häufigsten Elemente in einer Liste zurückgibt.
"""

# Deine Lösung hier
def haeufigste_elemente(liste: list, n: int) -> list:
    freq_list = [(x, liste.count(x)) for x in set(liste)]
    return sorted([x for x, y in reversed(sorted(freq_list, key=lambda y: y[1]))][:n])
def haeufigste_elemente2(liste: list, n: int) -> list:
    from collections import Counter
    return sorted([element for element, _ in Counter(liste).most_common(n)])


expected_result_aufgabe_7 = [2, 3]  # Erwartete Ausgabe für haeufigste_elemente([1, 2, 2, 3, 3, 3, 4], 2)
assert haeufigste_elemente([1, 2, 2, 3, 3, 3, 4], 2) == expected_result_aufgabe_7
assert haeufigste_elemente2([1, 2, 2, 3, 3, 3, 4], 2) == expected_result_aufgabe_7

"""
Aufgabe 8: Schreibe eine Funktion, die eine Liste von Zahlen in eine Liste von Tupeln umwandelt, wobei jedes Tupel die Zahl und ihr Quadrat enthält.
"""

# Deine Lösung hier
def zahlen_und_quadrate(liste: list[int]) -> list[tuple[int, int]]:
    return [(x, x**2) for x in liste]

expected_result_aufgabe_8 = [(1, 1), (2, 4), (3, 9)]  # Erwartete Ausgabe für zahlen_und_quadrate([1, 2, 3])
assert zahlen_und_quadrate([1, 2, 3]) == expected_result_aufgabe_8

"""
Aufgabe 9: Schreibe eine Funktion, die die Differenz zwischen zwei Listen zurückgibt (Elemente, die nur in der ersten Liste sind).
"""

# Deine Lösung hier
def differenz_listen(liste1: list, liste2: list) -> list:
    return [x for x in liste1 if x not in liste2]
def differenz_listen2(liste1: list, liste2: list) -> list:
    return list(set(liste1) - set(liste2))

expected_result_aufgabe_9 = [1, 2]  # Erwartete Ausgabe für differenz_listen([1, 2, 3, 4], [3, 4, 5, 6])
assert differenz_listen([1, 2, 3, 4], [3, 4, 5, 6]) == expected_result_aufgabe_9
assert differenz_listen2([1, 2, 3, 4], [3, 4, 5, 6]) == expected_result_aufgabe_9

"""
Aufgabe 10: Schreibe eine Funktion, die eine Liste von Dictionaries nach einem bestimmten Schlüssel sortiert.
"""

# Deine Lösung hier
def sortiere_liste_nach_schluessel(liste: list[dict], schluessel: str) -> list[dict]:
    return sorted(liste, key=lambda e: e[schluessel])


expected_result_aufgabe_10 = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]  # Erwartete Ausgabe für sortiere_liste_nach_schluessel([{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 35}], 'age')
assert sortiere_liste_nach_schluessel([{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 35}], 'age') == expected_result_aufgabe_10
