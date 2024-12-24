from unittest import TestCase
from typing import Any, Callable
import inspect


class Foo:

    def _helper(self, x: int, y: int) -> int:
        return x + y


def get_private_methode(objekt: Any, methode_name: str) -> Callable:
    """Funktion liefert die private Methode, dann aufgerufen werden kann oder NotImplementedError"""
    if len(res := [funktion
                   for member_name, funktion
                   in inspect.getmembers(objekt) if member_name == methode_name]) != 0:
        return res[0]
    else:
        raise NotImplementedError


class test_Foo(TestCase):

    def test_helper(self):

        obj = Foo()
        print(f"{inspect.getmembers(obj) = }")
        self.assertRaises(NotImplementedError, get_private_methode, *(obj, "_helpers"))
        helper = get_private_methode(obj, "_helper")
        self.assertEqual(3, helper(1, 2))
        self.assertEqual(3, get_private_methode(obj, "_helper")(1, 2))
