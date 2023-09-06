# logger.py
import logging

logging.basicConfig(filename="log_monitor.log", level=logging.INFO)


def log_event(event):
    logging.info(event)
