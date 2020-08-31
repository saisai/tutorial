import logging
import getpass

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.warning("Hello")

    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': getpass.getuser()}
    logger = logging.getLogger('tcpserver')
    logger.warning('Protocol problem: %s', 'connection reset', extra=d)
