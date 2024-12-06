from dataclasses import dataclass, field

"""
Problem: Ein Attribut wird per default auf None gesetzt, aber eigentlich soll es abhaengig von einem anderen
            Attribut ein Wert erhalten. Es kann aber nicht einfach geaendert werden,
            weil es eine frozen dataclass ist
Loesung: In der Methode __post_init__(self) mit __setattr__() das Objekt veraendern.
"""


@dataclass(frozen=True)
class Foo:
    x: int = field(default_factory=int)
    y: list = None

    def __post_init__(self):
        object.__setattr__(self,
                           'y',
                           [self.x] * 3 if self.x > 5 else [self.x])


if __name__ == "__main__":
    print(f"\n{ Foo().y == [0]       = }",
          f"\n{Foo(3).y == [3]       = }",
          f"\n{Foo(6).y == [6, 6, 6] = }")
