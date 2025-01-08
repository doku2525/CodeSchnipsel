from __future__ import annotations
from dataclasses import dataclass, field, replace
from functools import reduce
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time
from loggen.loggerklasse_zum_messen_der_runtime_im_programm import ZeitLogger
from kleiner_task_manager import TaskManager

logger = ZeitLogger.create('tmp.log', __name__)
logger.starte_logging()


@dataclass(frozen=True)
class Foo:
    liste: list = field(default_factory=list)

    def ersetze_element(self, alt: int, neu: int) -> Foo:
        time.sleep(1)
        return replace(self, liste=[element if element != alt else neu for element in self.liste])


def chain_ersetze(obj, changes):
    return reduce(lambda objekt, change: objekt.ersetze_element(*change), changes, obj)


def main() -> None:
    foo = Foo([1, 2, 3, 4, 5])
    return_value = []
    logger.start()
    for index in range(1, 6):
        foo = foo.ersetze_element(index, index * 100)
        print(f"\t {index} {foo}")
    logger.fertig("1")
    print(f"1. {foo = }")
    logger.start()
    foo2 = Foo([6, 7, 8, 9, 10])
    # result = chain_ersetze(foo2, [(x, x*1000) for x in range(6, 11)])
    result = chain_ersetze_parallel_neu_neu(foo2, [(x, x*1000) for x in range(6, 11)])
    print(f"{result = }")
    logger.fertig(f"2 {foo2 = }")


if __name__ == '__main__':
    # main()
    foo3 = Foo([1, 2, 3, 4, 5])
    tm = TaskManager(foo3)
    for i in range(1, 6):
        tm.register_task((lambda alt, neu: lambda fun: fun.ersetze_element(alt, neu))(i, i * 200))
    print(f"Registriert {tm.value = }")
    print(f"{tm.value = } {len(tm.auftraege) = }")
    logger.start()
    tm.start()
    logger.fertig("tm.start()")
    print(f"Gestartet {tm.value = }")
    while tm.is_running() or tm.auftraege:
        print(f"{tm.value = } {len(tm.auftraege) = }")
        time.sleep(0.5)
    print(f"Beendet {tm.value}")
