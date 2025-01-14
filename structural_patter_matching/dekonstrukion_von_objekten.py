from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import NamedTuple


class TuplePunkt3D(NamedTuple):
    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class DataPunkt3D:
    x: int = 0
    y: int = 0
    z: int = 0


def my_test1(punkt):
    match punkt:
        case TuplePunkt3D() if punkt == TuplePunkt3D(): print(f"Nullpunkt {punkt = }")
        case TuplePunkt3D(str(), str(), str()): print(f"String: {punkt.x = } {punkt.y = } {punkt.z = }")
        case TuplePunkt3D(x, y, z): print(f"{x = } {y = } { z = }")
        case _: print(f"Nichts gefunden")


def my_test2(punkt):
    match punkt:
        case TuplePunkt3D() if values := punkt._asdict().values(): print(f"Tuple {values}")
        case DataPunkt3D() if values := asdict(punkt).values(): print(f"Data {values}")
        case _: print(f"Nichts gefunden")


def my_test3(punkt):
    match punkt:
        case DataPunkt3D() | TuplePunkt3D(): print(f"Gesamt: {punkt.x =} {punkt.y =} {punkt.z =}")
        case DataPunkt3D() if values := punkt._asdict().values(): print(f"Tuple {values}")
        case TuplePunkt3D() if values := asdict(punkt).values(): print(f"Data {values}")
        case _: print(f"Nichts gefunden")


def sum_list(liste) -> int:
    match liste:
        case []: return 0
        case [car, *cdr]: return car + sum_list(cdr)

def sum_list_list(liste) -> list[int]:
    match liste:
        case [car]: return [car]
        case [car, cadr, *cdr]: return sum_list_list([car + cadr] + cdr)

@dataclass(frozen=True)
class MeineListe:
    value: int | None
    child: MeineListe | None


def sum_meine_liste(liste: MeineListe) -> int:
    match liste:
        case MeineListe(None, None): return 0
        case MeineListe(value, None): return value
        case MeineListe(None, child): return 0 + sum_meine_liste(child)
        case MeineListe(value, child): return value + sum_meine_liste(child)

def berechne_irgendwas_geometrisch_wichtiges(g_obj) -> str:
    match g_obj:
        case {'farbe': ('rot' | 'blau')}:return "Ich glaenze schoen rot oder blau"
        case {"typ": "kreis", "radius": r, "farbe": _}: return f" Ich bin ein Kreis {r = }"
        case {'typ': 'quadrat', 'hoehe': wert}: return f" Ich bin ein Quadrat {wert = }"
        case _: return "Ich bin from- und farblos"

if __name__ == '__main__':
    punkt = DataPunkt3D()
    my_test3(punkt)
    geometrie_objekte_kreis = {'typ': 'kreis', 'radius': 5}
    geometrie_objekte_quadrat = {'typ': 'quadrat', 'hoehe': 3}
    print(f"{ sum_list_list([1,2,3,4,5]) =}")
    print(f"{ sum_list_list([1,2,3,4,5]) =}")
    print(f"{ sum_meine_liste(MeineListe(1, MeineListe(2, MeineListe(3, None)))) = }")
    print(f"{ berechne_irgendwas_geometrisch_wichtiges(geometrie_objekte_kreis | {'farbe': 'gruen'}) = }")