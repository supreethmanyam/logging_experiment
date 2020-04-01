import time
import logging
from LoggingUtils import timeit, init_logger, CustomAdapter
import auxiliary
from utils import compute_distance

logger = init_logger("AddressTriangulation")

old_factory = logging.getLogRecordFactory()

@timeit
def do_something():
    logger.info("main function started")
    time.sleep(1)

def get_userid():
    return str(12223112)

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = get_userid()
    return record

if __name__ == "__main__":
#    logger = CustomAdapter(logger, {'userid': str(1224112)})
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
    compute_distance(logger)
    if logger.hasHandlers():
        logger.handlers = []
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(custom_attribute)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
 
#    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(custom_attribute)s - %(message)s')
    logging.setLogRecordFactory(record_factory)
    logger.info('creating new userid')
    #logger = CustomAdapter(logger, {'userid': str(1223112)})
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
    compute_distance(logger)
    print(dir(logger))


