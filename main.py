import time
from LoggingUtils import timeit, init_logger, CustomAdapter
import auxiliary
from utils import compute_distance

logger = init_logger("AddressTriangulation")


@timeit
def do_something():
    logger.info("main function started")
    time.sleep(1)


if __name__ == "__main__":
    logger = CustomAdapter(logger, {'userid': str(1224112)})
    do_something()
    logger.info('creating an instance of auxiliary_module.Auxiliary')
    a = auxiliary.Auxiliary()
    logger.info('created an instance of auxiliary_module.Auxiliary')
    logger.info('calling auxiliary_module.Auxiliary.do_something')
    a.do_something()
    logger.info('finished auxiliary_module.Auxiliary.do_something')
    logger.info('calling auxiliary_module.some_function()')
    auxiliary.some_function()
    logger.info('done with auxiliary_module.some_function()')
    compute_distance()
