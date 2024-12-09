import sys
from unittest import TestCase
import testen.einfache_tests_in_datei as tmsg

"""In Python gibt es eine maximale Rekursionstiefe, die erstaunlich gering ist. Allerdings kann man diese
relativ leicht veraendern."""


# Meine einfache rekursive Testfunktion. summiert nicht nur die Zahlen, sondern zeigt auch die Anzahl der Aufrufe
def rekursiver_addierer(x: int) -> int:
    return 1 + rekursiver_addierer(x - 1) if x > 0 else 0


if __name__ == '__main__':
    test = TestCase()

    # Keine Ahnung, ob die Rekursionstiefe je nach System unterschiedlich ist, ich hatte bisher immer unter 4000
    # Erster Test
    block_index = "erster"
    print(f"Ziel: {block_index} Block sollte durchfallen.")
    try:
        print(f"{rekursiver_addierer(5_000) = } ")
        tmsg.block_test_msg(block_index)
    except RecursionError as e:
        tmsg.block_test_msg(block_index, e)

    # Ermittle maximale Rekursionstiefe
    print(f"Maximale Rekursiontiefe : {sys.getrecursionlimit()}")

    # Zweiter Test
    block_index = "zweiter"
    print(f"Ziel: {block_index} Block sollte erfolgreich sein.")
    try:
        print(f" {rekursiver_addierer(sys.getrecursionlimit() - 5) = } ")
        test.assertGreater(5_000, sys.getrecursionlimit())
        tmsg.block_test_msg(block_index)
    except RecursionError as e:
        tmsg.block_test_msg(block_index, e)

    # Veraendern der maximalen Rekursionstiefe
    sys.setrecursionlimit(10_000)

    # Dritter Test
    block_index = "dritter"
    print(f"Ziel: {block_index} Block sollte erfolgreich sein.")
    try:
        print(f"Maximale Rekursiontiefe : {sys.getrecursionlimit()}")
        print(f" {rekursiver_addierer(5_000) = } ")
        print(f" {rekursiver_addierer(sys.getrecursionlimit() - 5) = } ")
        test.assertEqual(10_000, sys.getrecursionlimit())
        tmsg.block_test_msg(block_index)
    except RecursionError as e:
        tmsg.block_test_msg(block_index, e)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)
