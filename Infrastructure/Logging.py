import logging
import logging.config

class Logging:
    """     Esta clase se encarga principalmente configurar el logger
            configuracion extraida de:    https://michaelheap.com/using-ini-config-with-python-logger/
    """
    logger = None

    def __init__(self):
        logging.config.fileConfig('/home/parzival/Documents/Tesis/API/InterOperabilidad_API/config.ini')
        self.logger = logging.getLogger('sLogger')

    def debug(self, deb):
        print(deb)
        self.logger.debug(deb)

    def info(self, inf):
        self.logger.info(inf)

    def warn(self, war):
        self.logger.warn(war)

    def error(self, err):
        self.logger.error(err)

    def critical(self, cri):
        self.logger.critical(cri)
