"""Problem: Ungenauigkeiten bei wirklich einfachen Floatzahlen
Z.B.: 4 // 0.4 => 9.0  Was???
        Was daran liegt, dass 4 % 0.4 => 0.3999999... ergibt"""

from unittest import TestCase
import testen.einfache_tests_in_datei as tmsg

import decimal

if __name__ == '__main__':

    test = TestCase()

    block_index = "erster"
    print(f"Tests mit den normalen Zahlen")
    try:
        print(f"\t{4.0 / 0.4  = } \n"
              f"\t{4.0 // 0.4 = } \n"
              f"\t{4.0 % 0.4  = }")
        test.assertEqual(10.0, 4.0 / 0.4)
        test.assertEqual(9.0, 4.0 // 0.4, "Sollte 10 ergeben")
        test.assertEqual(0.0, 4.0 % 0.4, "Sollte 0 ergeben")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)

    block_index = "zweiter"
    print(f"Loesung mit import Decimal")
    # Praezision der Zahlen definieren
    decimal.getcontext().prec = 2
    a = decimal.Decimal('4.0')
    b = decimal.Decimal('0.4')
    try:
        print(f"\t{decimal.Decimal('4.0') / decimal.Decimal('0.4')  = } \n"
              f"\t{decimal.Decimal('4.0') // decimal.Decimal('0.4') = } \n"
              f"\t{decimal.Decimal('4.0') % decimal.Decimal('0.4')  = }")
        test.assertEqual(10.0, a / b)
        test.assertEqual(10.0, a // b, "Sollte 10 ergeben")
        test.assertEqual(0.0, a % b, "Sollte 0 ergeben")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)

    block_index = "dritter"
    print(f"Loesung ohne Importe")
    # Mit einem genuegend grossen Faktor die Zahlen in Integer umwandeln
    faktor = 1000
    a = 4.0 * faktor
    b = 0.4 * faktor
    try:
        print(f"\t{(4.0 * 1000) / (0.4 * 1000)  = } \n"
              f"\t{(4.0 * 1000) // (0.4 * 1000) = } \n"
              f"\t{(4.0 * 1000) % (0.4 * 1000)  = }")
        test.assertEqual(10.0, a / b)
        test.assertEqual(10.0, a // b, "Sollte 10 ergeben")
        test.assertEqual(0.0, a % b, "Sollte 0 ergeben")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)

    block_index = "vierter"
    print(f"Ermitteln der Nachkommastellen zum Definieren des Faktors oder Praezision")
    # Einfache Stringoperation
    float_zahl = 0.4
    faktor = 10 ** len(str(float_zahl).split(".")[1:])
    a = 4.0 * faktor
    b = 0.4 * faktor
    try:
        print(f"\t{(4.0 * faktor) / (0.4 * faktor)  = }\t{faktor =}\n"
              f"\t{(4.0 * faktor) // (0.4 * faktor) = }\t{faktor =}\n"
              f"\t{(4.0 * faktor) % (0.4 * faktor)  = }\t{faktor =}")
        test.assertEqual(10.0, a / b)
        test.assertEqual(10.0, a // b, "Sollte 10 ergeben")
        test.assertEqual(0.0, a % b, "Sollte 0 ergeben")
        tmsg.block_test_msg(block_index)
    except AssertionError as e:
        tmsg.block_test_msg(block_index, e)
