from dataclasses import dataclass, field
from typing import Any, Callable
import threading
from concurrent.futures import ThreadPoolExecutor, Future
from loggen.loggerklasse_zum_messen_der_runtime_im_programm import ZeitLogger


logger = ZeitLogger.create('tmp.log', __name__)


@dataclass
class TaskManager:
    value: Any
    auftraege: list = field(default_factory=list)
    executor: ThreadPoolExecutor = ThreadPoolExecutor()
    future: Future = None

    def register_task(self, funktion: Callable) -> None:
        self.auftraege.append(funktion)

    def start(self):
        print(f"{self.auftraege = }")
        logger.start("start")

        def worker():
            logger.start("worker")
            while self.auftraege:
                task = self.auftraege.pop()
                self.future = self.executor.submit(task, self.value)
                self.value = self.future.result()
            logger.fertig("worker")

        # Starte einen neuen Thread für die Aufgabenabarbeitung
        worker_thread = threading.Thread(target=worker)
        worker_thread.start()

    def is_running(self) -> bool:
        return (self.future is not None) and (not self.future.done())
