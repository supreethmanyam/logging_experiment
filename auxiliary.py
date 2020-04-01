import logging

# create logger
module_logger = logging.getLogger('FeatureManagementService.auxiliary')


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('FeatureManagementService.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info(f'done doing something and result={a}')


def some_function():
    module_logger.info('received a call to "some_function"')
