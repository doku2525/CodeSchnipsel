"""Problem: Datum liegt im ISO-Format vor und
ich moechte Jahre, Tage, Stunden addieren oder subtrahieren"""

import datetime
from decoratoren.vereinfache_meine_try_except_bloecke import mein_test_mit_prognose, test


# String mit ISO-Fromat in Datum, mit dem wir rechnen koennen, umwandeln.
iso_string = "2000-01-01 00:00:00"
datum = datetime.datetime.fromisoformat(iso_string)
zeit_wochen = datetime.timedelta(weeks=1)
zeit_tage = datetime.timedelta(days=2)
zeit_stunden = datetime.timedelta(hours=1)


@mein_test_mit_prognose(True)
def rechnen_mit_zeitspannen():
    print(f" {zeit_stunden * 48 = }")
    print(f" {zeit_stunden * 48 == zeit_tage = }")
    print(f" {datetime.timedelta(hours=7*24) == datetime.timedelta(weeks=1) = }")
    print(f" {datetime.timedelta(hours=24) * 7 == datetime.timedelta(weeks=1) = }")
    print(f" {datetime.timedelta(minutes=1) == datetime.timedelta(weeks=1/7/24/60) = }")
    print(f" {datetime.timedelta(weeks=1) / 2 = }")
    print(f" {datetime.timedelta(weeks=1) / 2 == datetime.timedelta(days=1) * 3.5 = }")
    test.assertEqual(zeit_stunden * 48, zeit_tage)
    test.assertEqual(datetime.timedelta(hours=7*24), datetime.timedelta(weeks=1))
    test.assertEqual(datetime.timedelta(hours=24) * 7, datetime.timedelta(weeks=1))
    test.assertEqual(datetime.timedelta(minutes=1), datetime.timedelta(weeks=1/7/24/60))
    test.assertEqual(datetime.timedelta(weeks=1) / 2, datetime.timedelta(days=1) * 3.5)


@mein_test_mit_prognose(True)
def rechnen_mit_datumsangaben():
    neues_datum = datetime.datetime.fromisoformat("2001-01-01 00:00:00")
    try:
        print(f" {iso_string - iso_string = }")
    except TypeError as e:
        print(f" Fehler: {e}")
    print(f" {datum - neues_datum = }")
    print(f" {datum - neues_datum == datetime.timedelta(days=-366) = }")
    try:
        print(f" {datum + neues_datum = }")
    except TypeError as e:
        print(f" Fehler: {e}")
    # Anscheinend Schaltjahr, deshalb wohl auch keine Jahre oder Monate als timedelta
    test.assertIsInstance(datum, datetime.datetime)
    test.assertIsInstance(datum - neues_datum, datetime.timedelta)
    test.assertEqual(datum - neues_datum, datetime.timedelta(days=-366))


@mein_test_mit_prognose(True)
def elemente_der_zeitspanne():
    mein_timedelta = datetime.timedelta(weeks=1) / 2
    print(f" {mein_timedelta.days == 3 =} =")
    print(f" {mein_timedelta.seconds == 0.5*24*60*60 = } =")
    print(f" {mein_timedelta.microseconds == 0 = } =")
    print(f" {mein_timedelta.total_seconds() == 3.5*24*60*60 = } =")
    test.assertEqual(3, mein_timedelta.days)
    test.assertEqual(0.5*24*60*60, mein_timedelta.seconds)
    test.assertEqual(0, mein_timedelta.microseconds)
    test.assertEqual(3.5 * 24 * 60 * 60, mein_timedelta.total_seconds())

@mein_test_mit_prognose(True)
def rechnen_mit_datum_und_zeitspanne_und_ausgabe_als_isostring():
    print(f" {datum + zeit_stunden = }")
    print(f" {(datum + zeit_stunden).isoformat() = }")
    print(f" {(datum + zeit_stunden).strftime('%Y-%m-%d %H:%M:%S') = }")
    print(f" {(datum + zeit_stunden) = :%Y-%m-%d %H:%M:%S}")
    print(f" {datetime.timedelta.max = } ")
    try:
        print(f" {(datum + datetime.timedelta.max) = :%Y-%m-%d %H:%M:%S}")
    except OverflowError as e:
        print(f" Fehler: {e}")
    try:
        print(f" {datetime.datetime.fromtimestamp(86400000000000) = } ")
    except ValueError as e:
        print(f" Fehler: {e}")

    test.assertIsInstance(datum + zeit_stunden, datetime.datetime)
    test.assertIsInstance((datum + zeit_stunden).isoformat(), str)
    test.assertNotEqual((datum + zeit_stunden).isoformat(), "2000-01-01 01:00:00")
    test.assertEqual((datum + zeit_stunden).strftime('%Y-%m-%d %H:%M:%S'),
                        "2000-01-01 01:00:00")
    test.assertEqual(f"{datum + zeit_stunden:%Y-%m-%d %H:%M:%S}", "2000-01-01 01:00:00")


if __name__ == "__main__":
    # rechnen_mit_zeitspannen()
    # print(f"{'* ' * 20} \n")
    # rechnen_mit_datumsangaben()
    # elemente_der_zeitspanne()
    rechnen_mit_datum_und_zeitspanne_und_ausgabe_als_isostring()