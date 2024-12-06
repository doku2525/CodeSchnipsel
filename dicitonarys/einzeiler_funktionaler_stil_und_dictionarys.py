
def plus_dicts(dict1, dict2) -> dict:
    # Gleiche Schluessel in dict1 werden durch den entsprechenden Schluessel in dict2 ersetzt
    return dict1 | dict2


def plus_accumulativ_dicts(dict1, dict2) -> dict:
    # Erzeugt die Werte als Liste
    return {key: ([value] if not (d2 := dict2.get(key, False)) else [value, d2]) for key, value in dict1.items()}


def minus_dicts(dict1, dict2) -> dict:
    # Es gibt keine Funktion wie den Concat-operator "|", deshalb muss man Workarounds nehmen
    # Funktioniert nur bei dict2 mit einem item.
    return {key: value for key, value in dict1.items() if {key: value} != dict2}


def minus_dicts_v2(dict1, dict2) -> dict:
    # Funktioniert mit einem beliebig grossen dict2
    return {key: value for key, value in dict1.items() if key in set(dict1.keys()) - set(dict2.keys())}


# Neues dicitoonary aus
if __name__ == "__main__":
    dict_start = {1: 2, 3: 4}
    dict_plus = {5: 6}
    dict_minus = {3: 4}
    print(f" Plus {plus_dicts(dict_start,dict_plus)}")
    print(f" Plus {plus_accumulativ_dicts(dict_start | dict_plus, dict_plus | dict_minus)}")
    print(f"Minus {minus_dicts(dict_start, dict_minus)}")
    print(f"Minus {minus_dicts(dict_start, dict_plus)}")
    print(f"Minus {minus_dicts(dict_start, dict_minus | dict_plus)}")
    print(f"Minus {minus_dicts_v2(dict_start, dict_minus)}")
    print(f"Minus {minus_dicts_v2(dict_start | dict_plus, dict_plus | dict_minus)}")
