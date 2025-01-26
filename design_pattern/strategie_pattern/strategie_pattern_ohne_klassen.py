from typing import TypeVar, Callable

# Interface
Zahlungsstrategie = TypeVar('Zahlungsstrategie', bound=Callable[[float], str])


# Konkrete Strategien
def kreditkarten_zahlung(name: str, karten_nummer: str, cvv: str) -> Zahlungsstrategie:
    def zahle(betrag: float): return f"{betrag} € mit Kreditkarte von {name} gezahlt."
    return zahle


def paypal_zahlung(email: str) -> Zahlungsstrategie:
    def zahle(betrag: float): return f"{betrag} € mit PayPal von {email} gezahlt."
    return zahle


def bitcoin_zahlung(bitcoin_adresse: str) -> Zahlungsstrategie:
    def zahle(betrag: float): return f"{betrag} € mit Bitcoin an {bitcoin_adresse} gezahlt."
    return zahle


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
        print(self._zahlungs_strategie(betrag))


# Beispielnutzung
if __name__ == "__main__":
    # Erstelle einen Einkaufswagen mit Kreditkarten-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(kreditkarten_zahlung("Max Mustermann", "1234-5678-9012-3456", "123"))
    einkaufswagen.artikel_hinzufuegen("Buch", 20)
    einkaufswagen.artikel_hinzufuegen("T-Shirt", 15)
    einkaufswagen.zahle()

    # Wechsle zu PayPal-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(paypal_zahlung("max.mustermann@example.com"))
    einkaufswagen.artikel_hinzufuegen("Schuhe", 50)
    einkaufswagen.zahle()

    # Wechsle zu Bitcoin-Zahlungsstrategie
    einkaufswagen = Einkaufswagen(bitcoin_zahlung("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
    einkaufswagen.artikel_hinzufuegen("Laptop", 1200)
    einkaufswagen.zahle()