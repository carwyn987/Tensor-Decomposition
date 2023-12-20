import logging
import logging.config
import argparse
import sys
import os

# Add lib to modules path irrespective of cwd
sys.path.insert(0, os.path.join("/", *os.path.realpath(__file__).split("/")[:-2]))
from lib import convert


def project_name(args, logger):
    pass


if __name__ == "__main__":

    # Configure argument parser
    parser = argparse.ArgumentParser(
        prog="Project_Name",
        description="Does project things",
        epilog="in-development",
    )
    parser.add_argument(
        "--filename",
        default="data/data.txt",
        help="The filename of a data file (.txt) to process.",
        required=False,
    )
    args = parser.parse_args()

    # Configure logger
    logging.config.fileConfig(
        "config/temp.conf", defaults={"logfilename": "logs/main_log.log"}
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    project_name(args, logger)

    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warning("Its a Warning")
    logger.error("Did you try to divide by zero")
    logger.critical("Internet is down")
