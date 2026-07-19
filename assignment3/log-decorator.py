import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")

        if args:
            logger.info(f"positional parameters: {list(args)}")
        else:
            logger.info("positional parameters: none")

        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        result = func(*args, **kwargs)

        logger.info(f"return: {result}")
        return result

    return wrapper

# Function with no parameters that returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")


# Function with any number of positional arguments that returns True
@logger_decorator
def positional_function(*args):
    return True


# Function with any number of keyword arguments that returns logger_decorator
@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator

say_hello()
positional_function(1, 2, 3, "hello")
keyword_function(name="Joey", assignment=3)