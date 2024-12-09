from typing import Any, Type
import gc
from unittest import TestCase
import testen.einfache_tests_in_datei as tmsg


class Foo:
    pass


def suche_instanzen(klasse: Type[Any]):
    return [objekt for objekt in gc.get_objects() if isinstance(objekt, klasse)]


if __name__ == "__main__":
    teste = TestCase()

    block_index = "erster"
    try:
        # ein Foo erzeugen
        x = Foo()
        liste_aller_foos = suche_instanzen(Foo)
        print(f"Anzahl der Foos sollte 1 sein => {len(liste_aller_foos)}")
        # Teste
        teste.assertEqual(1, len(liste_aller_foos))
        teste.assertIsInstance(liste_aller_foos[0], Foo, "Es ist auch wirklich Foo in der Liste")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)

    block_index = "zweiter"
    try:
        # Nochmal 3 Foos erzeugen. Macht insgesamt 4 Foos.
        liste = [Foo() for _ in range(2, 5)]
        liste_aller_foos = suche_instanzen(Foo)
        print(f"Anzahl der Foos sollte 4 sein => {len(liste_aller_foos)}")
        # Teste
        teste.assertEqual(4, len(liste_aller_foos))
        teste.assertIsInstance(liste_aller_foos[0], Foo, "Es ist auch wirklich Foo in der Liste")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)
