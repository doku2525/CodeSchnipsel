# python_aufgaben_day_005.py
"""
Python Übungsbuch Tag: 5
Thema: Klassen, Objektorientierte Programmierung (OOP) und Vererbung
Bemerkungen: Aufgaben zur Erstellung von Klassen, Methoden und Vererbung.
"""
import math

"""
Aufgabe 1: Erstelle eine Klasse `Person` mit den Attributen `name` und `alter`. Füge eine Methode `vorstellen` hinzu, die eine Vorstellung der Person zurückgibt.
"""

# Deine Lösung hier
class Person:
    def __init__(self, name: str, alter: int) -> None:
        self.name = name
        self.alter = alter

    def vorstellen(self) -> str:
        return f"Mein Name ist {self.name} und ich bin {self.alter} Jahre alt."

expected_result_aufgabe_1 = "Mein Name ist Max und ich bin 30 Jahre alt."  # Erwartete Ausgabe für Person("Max", 30).vorstellen()
assert Person("Max", 30).vorstellen() == expected_result_aufgabe_1

"""
Aufgabe 2: Erstelle eine Klasse `Auto` mit den Attributen `marke`, `modell` und `baujahr`. Füge eine Methode `beschreibung` hinzu, die eine Beschreibung des Autos zurückgibt.
"""

# Deine Lösung hier
class Auto:
    def __init__(self, marke: str, modell: str, baujahr: int):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def beschreibung(self) -> str:
        return f"Dies ist ein {self.marke} {self.modell} aus dem Jahr {self.baujahr}."

expected_result_aufgabe_2 = "Dies ist ein VW Golf aus dem Jahr 2015."  # Erwartete Ausgabe für Auto("VW", "Golf", 2015).beschreibung()
assert Auto("VW", "Golf", 2015).beschreibung() == expected_result_aufgabe_2

"""
Aufgabe 3: Erstelle eine Klasse `Konto` mit den Attributen `kontonummer` und `kontostand`. Füge Methoden `einzahlen` und `abheben` hinzu, die den Kontostand aktualisieren.
"""

# Deine Lösung hier
class Konto:
    def __init__(self, kontonummer: str, kontostand: float = 0.0):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, betrag: float) -> None:
        self.kontostand += betrag

    def abheben(self, betrag: float) -> None:
        self.kontostand -= betrag


expected_result_aufgabe_3 = 500.0  # Erwarteter Kontostand nach Konto("12345").einzahlen(1000).abheben(500)
konto = Konto("12345")
konto.einzahlen(1000)
konto.abheben(500)
assert konto.kontostand == expected_result_aufgabe_3

"""
Aufgabe 4: Erstelle eine Klasse `Student`, die von `Person` erbt. Füge ein Attribut `matrikelnummer` hinzu und überschreibe die Methode `vorstellen`, um die Matrikelnummer einzubeziehen.
"""

# Deine Lösung hier
class Student(Person):
    def __init__(self, name: str, alter: int, matrikelnummer: str):
        super().__init__(name, alter)
        self.matrikelnummer = matrikelnummer

    def vorstellen(self) -> str:
        return f"Mein Name ist {self.name}, ich bin {self.alter} Jahre alt und meine Matrikelnummer ist {self.matrikelnummer}."


expected_result_aufgabe_4 = "Mein Name ist Anna, ich bin 22 Jahre alt und meine Matrikelnummer ist 123456."  # Erwartete Ausgabe für Student("Anna", 22, "123456").vorstellen()
assert Student("Anna", 22, "123456").vorstellen() == expected_result_aufgabe_4

"""
Aufgabe 5: Erstelle eine Klasse `Rechteck` mit den Attributen `breite` und `hoehe`. Füge Methoden `flaeche` und `umfang` hinzu, die die Fläche und den Umfang des Rechtecks berechnen.
"""

# Deine Lösung hier
class Rechteck:
    def __init__(self, breite: int, hoehe: int):
        self.breite = breite
        self.hoehe = hoehe

    def flaeche(self) -> float:
        return self.breite * self.hoehe

    def umfang(self) -> float:
        return 2 * self.breite + 2 * self.hoehe

expected_result_aufgabe_5 = (20.0, 18.0)  # Erwartete Ausgabe für (Rechteck(5, 4).flaeche(), Rechteck(5, 4).umfang())
rechteck = Rechteck(5, 4)
assert (rechteck.flaeche(), rechteck.umfang()) == expected_result_aufgabe_5

"""
Aufgabe 6: Erstelle eine Klasse `Kreis` mit dem Attribut `radius`. Füge Methoden `flaeche` und `umfang` hinzu, die die Fläche und den Umfang des Kreises berechnen.
"""

# Deine Lösung hier
class Kreis:
    import math
    def __init__(self, radius: int):
        self.radius = radius

    def flaeche(self) -> float:
        return math.pi * self.radius**2

    def umfang(self) -> float:
        return 2 * math.pi * self.radius

expected_result_aufgabe_6 = (78.53981633974483, 31.41592653589793)  # Erwartete Ausgabe für (Kreis(5).flaeche(), Kreis(5).umfang())
kreis = Kreis(5)
assert (kreis.flaeche(), kreis.umfang()) == expected_result_aufgabe_6

"""
Aufgabe 7: Erstelle eine Klasse `Wuerfel`, die von `Rechteck` erbt. Füge eine Methode `volumen` hinzu, die das Volumen des Würfels berechnet.
"""

# Deine Lösung hier
class Wuerfel(Rechteck):
    def __init__(self, breite: int):
        super().__init__(breite, breite)

    def volumen(self) -> float:
        return self.breite ** 3


expected_result_aufgabe_7 = 125.0  # Erwartete Ausgabe für Wuerfel(5).volumen()
assert Wuerfel(5).volumen() == expected_result_aufgabe_7

"""
Aufgabe 8: Erstelle eine Klasse `Bank`, die eine Liste von `Konto`-Objekten verwaltet. Füge Methoden `konto_hinzufuegen` und `gesamter_kontostand` hinzu.
"""

# Deine Lösung hier
class Bank:
    def __init__(self):
        self.konten = []

    def konto_hinzufuegen(self, konto: Konto) -> None:
        self.konten.append(konto)

    def gesamter_kontostand(self) -> float:
        return sum(konto.kontostand for konto in self.konten)


expected_result_aufgabe_8 = 1500.0  # Erwarteter Gesamtkontostand nach Hinzufügen von zwei Konten mit 1000 und 500
bank = Bank()
bank.konto_hinzufuegen(Konto("12345", 1000))
bank.konto_hinzufuegen(Konto("67890", 500))
assert bank.gesamter_kontostand() == expected_result_aufgabe_8

"""
Aufgabe 9: Erstelle eine Klasse `Tier` mit den Attributen `name` und `alter`. Füge eine Methode `geraeusch` hinzu, die ein tierartspezifisches Geräusch zurückgibt.
"""

# Deine Lösung hier
class Tier:
    def __init__(self, name: str, alter: int):
        self.name = name
        self.alter = alter

    def geraeusch(self) -> str:
        return "Wuff!"


expected_result_aufgabe_9 = "Wuff!"  # Erwartete Ausgabe für Tier("Bello", 3).geraeusch()
assert Tier("Bello", 3).geraeusch() == expected_result_aufgabe_9

"""
Aufgabe 10: Erstelle eine Klasse `Hund`, die von `Tier` erbt. Überschreibe die Methode `geraeusch`, um "Wuff!" zurückzugeben.
"""

# Deine Lösung hier
class Hund(Tier):
    def __init__(self, name: str, alter: int):
        super().__init__(name, alter)

    def geraeusch(self) -> str:
        return "Wuff!"

expected_result_aufgabe_10 = "Wuff!"  # Erwartete Ausgabe für Hund("Bello", 3).geraeusch()
assert Hund("Bello", 3).geraeusch() == expected_result_aufgabe_10