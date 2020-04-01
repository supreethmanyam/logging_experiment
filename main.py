import time
from LoggingUtils import LoggingUtils, timeit
import auxiliary
from utils import compute_distance


def get_user_id():
    return str(657476578)


@timeit
def do_something():
    logger.info("main function started")
    time.sleep(1)


if __name__ == "__main__":
    logging_utils = LoggingUtils(
        name="FeatureManagementService",
        log_level="INFO",
        log_record_factory_func=get_user_id
    )
    logger = logging_utils.init_logger_with_attribute("USERID")
    # logger = logging_utils.init_logger()
    logger.info('creating new userid')
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
