import logging
from LoggingUtils import timeit, init_logger, CustomAdapter

logger = logging.getLogger("AddressTriangulation.utils.Geoutils")
#logger = CustomAdapter.logger("AddressTriangulation.utils.Geoutils")


def compute_distance():
    logger.info("Calculating distance")
