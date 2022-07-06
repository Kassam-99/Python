import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

logger.addHandler(file_handler)


logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error("And non-ASCII stuff, too, like Øresund and Malmö")
