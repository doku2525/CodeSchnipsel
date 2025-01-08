import logging
import time

import zeit_logging_modul as zeit_logging
from loggerklasse_zum_messen_der_runtime_im_programm import ZeitLogger

"""
Eigene Logger erstellen.
"""
# Definieren einer neuen Log-Stufe. So wie die vordefinierten Konstanten logging.DEBUG(=10) usw.
TIME_LEVEL = 25
# Registriere die neue Stufe im Modul
logging.addLevelName(TIME_LEVEL, "TIME")


# Verwenden der neuen Stufe und definieren der log-Funktion. Keine Ahnung, was die Funktion genau macht,
# aber anscheinend wird abgefragt, ob wir die Stufe registriert haben und ruft dann _log() auf.
def time_log(self, message, *args, **kwargs):
    if self.isEnabledFor(TIME_LEVEL):
        self._log(TIME_LEVEL, message, args, **kwargs)


# Registrieren der log-Funktion im Logger.
logging.Logger.time_log = time_log
# Der Name, unter dem die Funktion im Logger registriert ist, muss nicht identisch mit dem Namen der log-Funktion sein.
logging.Logger.zeit_log = time_log


if __name__ == '__main__':
    print(f"Level der vordefinierten LEVELS:\n" +
          f"\t{logging.DEBUG = }\n" +
          f"\t{logging.INFO = }\n" +
          f"\t{logging.WARNING = }\n" +
          f"\t{logging.ERROR = }\n" +
          f"\t{logging.CRITICAL = }\n"
          )

    # Benutzen unseres Loggers
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Mit 25 liegt der eigene Logger zwischen INFO und WARNING
    fh = logging.FileHandler('debug.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.zeit_log('Gemessene Zeit')
    logger.time_log('Gemessene Zeit')
    logger.debug('Debug-Nachricht')
    logger.info('Info-Nachricht')
    logger.warning('Warnhinweis')
    logger.error('Fehlermeldung')
    logger.critical('Schwerer Fehler')

    # Unseren im Modul selbst definierten Logger benuzten.
    mein_logger = zeit_logging.create_zeit_logger('zeit.log', 'PERFORMANCE')
    print(f"{mein_logger.level = }")
    mein_logger.setLevel(zeit_logging.TIME_LEVEL)
    mein_logger.zeit_log('Gemessene Zeit')
    mein_logger.time_log('Gemessene Zeit')
    mein_logger.debug('Debug-Nachricht')
    mein_logger.info('Info-Nachricht')
    mein_logger.warning('Warnhinweis')
    mein_logger.error('Fehlermeldung')
    mein_logger.critical('Schwerer Fehler')

    zeit_logger = ZeitLogger.create('zeit.log', __name__)
    zeit_logger.start()
    time.sleep(1)
    zeit_logger.fertig("Time.sleep ausgefuehrt,")
