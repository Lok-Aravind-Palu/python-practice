import logging

logger = logging.getLogger(__name__)


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    logger.info("This is the given number of expression %s" % exp)
    return raise_to_exp


square = raise_to(2)
print(square(4))
print(square(3))

cube = raise_to(3)
print(cube(3))
print(cube(9))
