import logging
import argparse
import time

# parser = argparse.ArgumentParser()
# parser.add_argument("-l", "--log", type=str, default="WARNING")
# parser.add_argument("-f", "--file", default=None)
# args = parser.parse_args()
#
# # logging.basicConfig(filename=args.file, level=args.log)
#
# # logging.basicConfig(format='%(asctime)s %(message)s')
# logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s %(message)s')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

logger = logging.getLogger('new_logger')
logger.setLevel(logging.DEBUG)
file = logging.FileHandler('logs.log')
logger.addHandler(file)

logger.info('')