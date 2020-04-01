import logging
import sys
import time
from functools import wraps

logger = logging.getLogger("FeatureManagementService.utils.LoggingUtils")


class LoggingUtils:

    def __init__(self, name, log_level="INFO", log_record_factory_func=None):
        self.name = name
        self.log_level = log_level
        self.log_record_factory_func = log_record_factory_func

    def add_handlers(self, logger, log_format=None):
        if self.log_level.upper() == "INFO":
            logger.setLevel(logging.INFO)
        elif self.log_level.upper() == "DEBUG":
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        logger.propagate = False
        handler = logging.StreamHandler(sys.stdout)
        if self.log_level.upper() == "INFO":
            handler.setLevel(logging.INFO)
        elif self.log_level.upper() == "DEBUG":
            handler.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)
        if log_format and log_format is not None:
            formatter = logging.Formatter(log_format)
        else:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s:  %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def init_logger(self, log_format=None):
        logger = logging.getLogger(self.name)
        if logger.hasHandlers():
            logger.handlers = []
        logger = self.add_handlers(logger, log_format=log_format)
        return logger

    def record_and_set_factory(self):

        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            if self.log_record_factory_func is not None:
                record.custom_attribute = self.log_record_factory_func()
            else:
                record.custom_attribute = str("Missing")
            return record

        logging.setLogRecordFactory(record_factory)

    def init_logger_with_attribute(self, attribute_name):
        self.record_and_set_factory()
        log_format = f'%(asctime)s - [{attribute_name} %(custom_attribute)s] - %(levelname)s - %(name)s:  %(message)s'
        return self.init_logger(log_format)


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Total elapsed for {func.__name__} method: {int((end-start) // 60)}m {(end-start) % 60:.0f}s...")
        return result
    return wrapper
