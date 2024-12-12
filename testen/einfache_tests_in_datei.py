from unittest import TestCase


def block_test_msg(block_index: str, fehler: Exception = None) -> None:
    # Wenn fehler, dann wurde eine Exception geworfen, also ist der Test nicht erfolgreich gewesen.
    print(
        f"v_v' Fehler im {block_index} Block ! << {fehler} >>\n"
    ) if fehler else print(
        f"\^_^/ Tests im {block_index} Block bestanden!\n"
    )

def func_test_msg(func_name: str, fehler: Exception = None) -> None:
    # Wenn fehler, dann wurde eine Exception geworfen, also ist der Test nicht erfolgreich gewesen.
    print(
        f"v_v' Fehler in Funktion {func_name}()! << {fehler} >>\n"
    ) if fehler else print(
        f"\^_^/ Tests in Funktion {func_name}() bestanden!\n"
    )


if __name__ == '__main__':
    # Erstelle TestCase
    test = TestCase()

    # Benutze einen try-Block, da sonst TestCase() sonst das Programm mit einer Exception beendet.
    block_index = "erster"
    print(f"\nZiel: {block_index} Block soll erfolgreich sein!")
    try:
        test.assertEqual(1, 1)
        test.assertIsInstance(test, TestCase, "Pruefe, ob test eine Instance von TestCase ist")
        block_test_msg(block_index)
    except AssertionError as e:     # TestCase wirf AssertionError.
        block_test_msg(block_index, e=e)

    block_index = "zweiter"
    print(f"Ziel: {block_index} Block soll durchfallen!")
    try:
        test.assertEqual(2, 1)
        test.assertIsInstance(test, list, "Pruefe, ob test eine Instance von TestCase ist")
        block_test_msg(block_index)
    except AssertionError as e:  # TestCase wirf AssertionError nach dem ersten durchgefallenen Test.
        block_test_msg(block_index, e)  # 2 != 1

    block_index = "dritter"
    print(f"Ziel: {block_index} Block soll erfolgreich sein!")
    try:    # Pruefe, ob assertEqual den erwarteten Fehler wirft
        test.assertRaises(AssertionError, test.assertEqual, *(1, 2))
        block_test_msg(block_index)
    except AssertionError as e:
        block_test_msg(block_index, e)
