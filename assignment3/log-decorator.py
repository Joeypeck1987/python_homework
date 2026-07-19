# Task 1: Writing and Testing a Decorator

import logging


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("./decorator.log", "w")
logger.addHandler(file_handler)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional_parameters = list(args) if args else "none"
        keyword_parameters = kwargs if kwargs else "none"

        logger.info(f"function: {func.__name__}")
        logger.info(
            f"positional parameters: {positional_parameters}"
        )
        logger.info(
            f"keyword parameters: {keyword_parameters}"
        )
        logger.info(f"return: {result}")

        return result

    return wrapper


# No parameters and no return value
@logger_decorator
def no_parameters():
    print("Hello, World!")


# Variable number of positional arguments; returns True
@logger_decorator
def positional_parameters(*args):
    return True


# No positional arguments; variable keyword arguments;
# returns logger_decorator
@logger_decorator
def keyword_parameters(**kwargs):
    return logger_decorator


# Mainline code
no_parameters()
positional_parameters(1, 2, 3)
keyword_parameters(name="Joey", course="Python")