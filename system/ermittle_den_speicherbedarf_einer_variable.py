import sys
from unittest import TestCase
import testen.einfache_tests_in_datei as tmsg


if __name__ == '__main__':
    test = TestCase()

    liste_leer = []
    liste_voll = list(range(100_000))
    range_voll = range(100_000)
    generator_voll = (x for x in range(100_000))
    tuple_leer = tuple()

    box_index = "erster"
    try:
        test.assertGreater(sys.getsizeof(liste_voll), sys.getsizeof(liste_leer))
        test.assertGreater(sys.getsizeof(liste_leer), sys.getsizeof(tuple_leer))
        print(f" Speicherbedarf des leeren Tuples       = {sys.getsizeof(tuple_leer)} Bytes")
        print(f" Speicherbedarf der leeren Liste        = {sys.getsizeof(liste_leer)} Bytes")
        print(f" Speicherbedarf der vollen Liste        = {sys.getsizeof(liste_voll):_} Bytes")
        print(f" Speicherbedarf der vollen Liste        = {sys.getsizeof(liste_voll)/1024} kBytes")
        print(f" Speicherbedarf der vollen Liste        = {sys.getsizeof(liste_voll) / (1024 ** 2)} MBytes")
        print(f" Speicherbedarf der Liste als Range     = {sys.getsizeof(range_voll) / (1024)} kBytes")
        print(f" Speicherbedarf der Liste als Generator = {sys.getsizeof(generator_voll) / (1024)} kBytes")
        tmsg.block_test_msg(box_index)
    except AssertionError as e:
        tmsg.block_test_msg(box_index,e)