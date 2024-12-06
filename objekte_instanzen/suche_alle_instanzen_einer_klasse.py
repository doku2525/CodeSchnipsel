from typing import Any, Type
import gc


class Foo:
    pass


def suche_instanzen(klasse: Type[Any]):
    return [objekt for objekt in gc.get_objects() if isinstance(objekt, klasse)]


if __name__ == "__main__":
    x = Foo()
    liste_aller_foos = suche_instanzen(Foo)
    print(f" Anzahl der Foos: {1 == len(liste_aller_foos) = }")

    # Nochmal 3 Foos erzeugen. Macht insgesamt 4.
    liste = [Foo() for _ in range(2, 5)]
    liste_aller_foos = suche_instanzen(Foo)
    print(f" Anzahl der Foos: {4 == len(liste_aller_foos) = }")
