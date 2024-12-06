from __future__ import annotations
from dataclasses import dataclass, field, asdict, replace
from enum import Enum
import json
from typing import cast


class Status(Enum):
    NEU = 0
    ALT = 1

    @classmethod
    def from_dict(cls, name: str) -> cls:
        return cls[name]


@dataclass(frozen=True)
class Punkt:
    x: int = 0
    y: int = 0


@dataclass(frozen=True)
class Auto:
    preis: int = 0
    zustand: Status = field(default_factory=Status)


def meine_asdict_factory(items) -> dict:
    return {key: (
        value.name if isinstance(value, Enum) else
        value)
        for key, value in items}


if __name__ == '__main__':
    obj = Punkt()
    als_dictionary = asdict(Punkt())
    print(f" Punkt als dict = {als_dictionary}")
    print(f" Dictionary als Punkt = {Punkt(**als_dictionary)}")

    objekt = Auto(zustand=Status.ALT)
    als_dictionary = asdict(objekt)
    print(f"\n\n Auto als dict = {als_dictionary}")
    print(f" Dictionary als Auto = {Auto(**als_dictionary)}")
    try:
        s = json.dumps(als_dictionary)
        print(f" Unser Auto als JSON: {s}")
    except Exception as e:
        print(f" JSON kann Typen Status nicht umwandeln. Siehe: {e}")

    als_dictionary = asdict(objekt, dict_factory=meine_asdict_factory)
    try:
        s = json.dumps(als_dictionary)
        print(f" Unser Auto als JSON: {s}")
    except Exception as e:
        print(f" JSON kann Typen Status nicht umwandeln. Siehe: {e}")

    print(f"\n\n Auto als dict = {als_dictionary}")
    print(f" Dictionary als Auto = {Auto(**als_dictionary)}")
    halbes_auto = Auto(**als_dictionary)
    print(f" Dictionary als Auto =",
          f"{replace(halbes_auto, zustand=Status.from_dict(cast(str,halbes_auto.zustand)))}")
    print(f" Dictionary als Auto =",
          f"{Auto(**(als_dictionary | {'zustand': Status.from_dict(als_dictionary.get('zustand', 'NEU'))}))}")
