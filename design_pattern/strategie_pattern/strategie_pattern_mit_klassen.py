from abc import ABC, abstractmethod


# Strategie-Interface
class Zahlungsstrategie(ABC):
    @abstractmethod
    def zahle(self, betrag):
        pass


# Konkrete Strategien
class KreditkartenZahlung(Zahlungsstrategie):
    def __init__(self, name, karten_nummer, cvv):
        self.name = name
        self.karten_nummer = karten_nummer
        self.cvv = cvv

    def zahle(self, betrag):
        return f"{betrag} € mit Kreditkarte von {self.name} gezahlt."


class PayPalZahlung(Zahlungsstrategie):
    def __init__(self, email):
        self.email = email

    def zahle(self, betrag):
        return f"{betrag} € mit PayPal von {self.email} gezahlt."


class BitcoinZahlung(Zahlungsstrategie):
    def __init__(self, bitcoin_adresse):
        self.bitcoin_adresse = bitcoin_adresse

    def zahle(self, betrag):
        return f"{betrag} € mit Bitcoin an {self.bitcoin_adresse} gezahlt."


# Context
class Einkaufswagen:
    def __init__(self, zahlungs_strategie: Zahlungsstrategie):
        self._zahlungs_strategie = zahlungs_strategie
        self._artikel = []

    def artikel_hinzufuegen(self, artikel, preis):
        self._artikel.append((artikel, preis))

    def gesamtbetrag(self):
        return sum(preis for _, preis in self._artikel)

    def zahle(self):
        betrag = self.gesamtbetrag()
        print(self._zahlungs_strategie.zahle(betrag))


# Beispielnutzung
if __name__ == "__main__":
    # Erstelle einen Einkaufswagen mit Kreditkarten-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(KreditkartenZahlung("Max Mustermann", "1234-5678-9012-3456", "123"))
    einkaufswagen.artikel_hinzufuegen("Buch", 20)
    einkaufswagen.artikel_hinzufuegen("T-Shirt", 15)
    einkaufswagen.zahle()

    # Wechsle zu PayPal-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(PayPalZahlung("max.mustermann@example.com"))
    einkaufswagen.artikel_hinzufuegen("Schuhe", 50)
    einkaufswagen.zahle()

    # Wechsle zu Bitcoin-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(BitcoinZahlung("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    einkaufswagen.artikel_hinzufuegen("Laptop", 1200)
    einkaufswagen.zahle()