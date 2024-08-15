import logging
import traceback


logger = logging.getLogger(__name__)


def ensure_data(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            logger.warning(f"An error occurred: {traceback.format_exc()}, Fatal error: {ex}")

            return args[0] if args else None

    return wrapper
