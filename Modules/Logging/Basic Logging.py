import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO, filename="test.log", format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logging.debug("It is used to provide detailed information and only use it when there is diagnosing problems.")
logging.info("It provides the information regarding that things are working as we want.")
logging.warning("It is used to warn that something happened unexpectedly, or we will face the problem in the upcoming time")
logging.error("It is used to inform when we are in some serious trouble, the software hasn't executed some programs.")
logging.critical("It specifies the serious error, the program itself may be incapable of remaining executing.")
