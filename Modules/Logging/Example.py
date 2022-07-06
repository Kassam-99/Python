import logging

'''
There is also other option to get complete information about the exception. The logging module provides the exception() method,
which logs a message with ERROR and attaches the exception information.
To use it, call the logging.exception() method same as calling logging.error(exc_info = True).
'''




logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler("math.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)


logger.addHandler(file_handler)


def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def divide(x, y):
    """Subtract Function"""
    try:
        result =  x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by Zero")
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

div_result = divide(num_1, num_2)
logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
