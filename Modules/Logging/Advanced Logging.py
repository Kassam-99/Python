import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler("sample.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)


logger.addHandler(file_handler)



logging.debug("It is used to provide detailed information and only use it when there is diagnosing problems.")
logging.info("It provides the information regarding that things are working as we want.")
logging.warning("It is used to warn that something happened unexpectedly, or we will face the problem in the upcoming time")
logging.error("It is used to inform when we are in some serious trouble, the software hasn't executed some programs.")
logging.critical("It specifies the serious error, the program itself may be incapable of remaining executing.")

