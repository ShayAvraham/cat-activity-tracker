import logging


def get_logger(name: str, filename: str = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logging.basicConfig(filename=filename or 'smart_cat.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    return logger
