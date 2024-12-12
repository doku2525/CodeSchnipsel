"""Problem: Ich schreibe immer wieder in den Dateien die gleichen Test mit
try:except:-Bloecke. Das leasst sich doch bestimmt vereinfachen.
test = TestCase()
block_index = "erster|zweiter|dritter usw.
try:
   machetwas
   tmsg.block_test_msg(block_index)
except AssertionError as e:
   tmsg.block_test_msg(block_index, e)
"""

from unittest import TestCase
import testen.einfache_tests_in_datei as tmsg


"""Loesung: decorator"""


def mein_test_simple(func):
    """Dekoratoraufruf ohne Argumente"""
    globals()['test'] = TestCase()

    def wrapper(*args, **kwargs):
        funktions_name = func.__name__
        try:
            # dekorierte Funktion ausfuehren
            func(*args, **kwargs)
            tmsg.func_test_msg(funktions_name)
        except AssertionError as e:
            tmsg.func_test_msg(block_index, e)
    return wrapper


def mein_test_mit_prognose(ziel: bool | None = None):
    """Dekorator aufruf mit Ziel"""
    globals()['test'] = TestCase()

    def decorator(func):
        def wrapper(*args, **kwargs):
            funktions_name = func.__name__
            ziel_arg = True if ziel is None else ziel
            ziel_text = (f"Funktion {funktions_name}() muesste" +
                         (f" erfolgreich sein!" if ziel_arg else f" durchfallen!"))
            print(f"{ziel_text}")
            try:
                # dekorierte Funktion ausfuehren
                func(*args, **kwargs)
                print("\t\t Wie erwartet!" if ziel_arg else "\t\t Das ist unerwartet!")
                tmsg.func_test_msg(funktions_name)
            except AssertionError as e:
                print("\tWie erwartet!" if not ziel_arg else "\tDas ist unerwartet!")
                tmsg.func_test_msg(block_index, e)
        return wrapper
    return decorator


def erster_test():
    a = 5
    b = 4
    print(f"\t{a+b = }")
    print(f"\t{a*b = }")
    test.assertEqual(9, a + b)


@mein_test_simple
def einfacher_test():
    erster_test()


@mein_test_mit_prognose(False)
def pronostizierter_test():
    erster_test()


if __name__ == "__main__":
    einfacher_test()
    print("________________")
    pronostizierter_test()
