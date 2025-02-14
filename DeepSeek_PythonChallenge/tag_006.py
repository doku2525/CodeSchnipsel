# python_aufgaben_day_006.py
"""
Python Übungsbuch Tag: 6
Thema: Module, Pakete und fortgeschrittene Python-Konzepte
Bemerkungen: Aufgaben zur Verwendung von Modulen, Paketen und fortgeschrittenen Python-Konzepten.
"""

"""
Aufgabe 1: Importiere das `math`-Modul und berechne die Quadratwurzel von 16.
"""

# Deine Lösung hier
import math
ergebnis = math.sqrt(16)


expected_result_aufgabe_1 = 4.0  # Erwartete Ausgabe für math.sqrt(16)
assert ergebnis == expected_result_aufgabe_1

"""
Aufgabe 2: Importiere das `random`-Modul und generiere eine zufällige Ganzzahl zwischen 1 und 10.
"""

# Deine Lösung hier
import random
zufallszahl = random.randint(1,10)


# Keine erwartete Ausgabe, da die Zahl zufällig ist. Überprüfe die Ausgabe manuell.
print(zufallszahl)

"""
Aufgabe 3: Importiere das `datetime`-Modul und gib das aktuelle Datum und die aktuelle Uhrzeit aus.
"""

# Deine Lösung hier
import datetime
jetzt = datetime.datetime.now()


# Keine erwartete Ausgabe, da das aktuelle Datum und die Uhrzeit dynamisch sind. Überprüfe die Ausgabe manuell.
print(jetzt)

"""
Aufgabe 4: Erstelle ein eigenes Modul `mein_modul.py` mit einer Funktion `gruessen`, die "Hallo, Welt!" zurückgibt. Importiere und verwende diese Funktion.
"""

# Deine Lösung hier
from data.data_006.mein_modul import gruessen
gruß = gruessen()

expected_result_aufgabe_4 = "Hallo, Welt!"  # Erwartete Ausgabe für gruessen()
assert gruß == expected_result_aufgabe_4

"""
Aufgabe 5: Importiere die Funktion `sqrt` aus dem `math`-Modul und berechne die Quadratwurzel von 25.
"""

# Deine Lösung hier
from math import sqrt
ergebnis = sqrt(25)


expected_result_aufgabe_5 = 5.0  # Erwartete Ausgabe für sqrt(25)
assert ergebnis == expected_result_aufgabe_5

"""
Aufgabe 6: Importiere das `os`-Modul und gib das aktuelle Arbeitsverzeichnis aus.
"""

# Deine Lösung hier
import os
aktuelles_verzeichnis = os.getcwd()


# Keine erwartete Ausgabe, da das Arbeitsverzeichnis dynamisch ist. Überprüfe die Ausgabe manuell.
print(aktuelles_verzeichnis)

"""
Aufgabe 7: Importiere das `sys`-Modul und gib die Python-Version aus.
"""

# Deine Lösung hier
import sys
python_version = sys.version


# Keine erwartete Ausgabe, da die Python-Version vom System abhängt. Überprüfe die Ausgabe manuell.
print(python_version)

"""
Aufgabe 8: Erstelle ein Paket `mein_paket` mit einem Modul `mein_modul.py`, das eine Funktion `verdoppeln` enthält, die eine Zahl verdoppelt. Importiere und verwende diese Funktion.
"""

# Deine Lösung hier
from data.data_006.mein_modul import verdoppeln
ergebnis = verdoppeln(5)


expected_result_aufgabe_8 = 10  # Erwartete Ausgabe für verdoppeln(5)
assert ergebnis == expected_result_aufgabe_8

"""
Aufgabe 9: Importiere das `collections`-Modul und verwende `defaultdict`, um ein Wörterbuch zu erstellen, das Standardwerte für nicht vorhandene Schlüssel zurückgibt.
"""

# Deine Lösung hier
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] += 1

expected_result_aufgabe_9 = 1  # Erwartete Ausgabe für default_dict['a']
assert default_dict['a'] == expected_result_aufgabe_9

"""
Aufgabe 10: Importiere das `itertools`-Modul und verwende `itertools.cycle`, um eine unendliche Schleife über eine Liste zu erstellen. Gib die ersten 5 Elemente aus.
"""

# Deine Lösung hier
import itertools
schleife = itertools.cycle([1, 2, 3])
erste_fuenf = [next(schleife) for _ in range(5)]


expected_result_aufgabe_10 = [1, 2, 3, 1, 2]  # Erwartete Ausgabe für die ersten 5 Elemente
assert erste_fuenf == expected_result_aufgabe_10