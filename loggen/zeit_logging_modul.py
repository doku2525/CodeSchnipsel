import logging


# Definieren einer neuen Log-Stufe
TIME_LEVEL = 25
logging.addLevelName(TIME_LEVEL, "TIME")


def create_zeit_logger(filename: str, logger_name: str) -> logging.Logger:
    # Verwenden der neuen Stufe und definieren der log-Funktion
    def time_log(self, message, *args, **kwargs):
        if self.isEnabledFor(TIME_LEVEL):
            self._log(TIME_LEVEL, message, args, **kwargs)

    # Registrieren der log-Funktion im Logger. Der Name muss nicht identisch mit dem Namen der log-Funktion sein.
    logging.Logger.time_log = time_log
    logging.Logger.zeit_log = time_log

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Mit 25 liegt der eigene Logger zwischen INFO und WARNING
    fh = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger
