import logging


def setup_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
