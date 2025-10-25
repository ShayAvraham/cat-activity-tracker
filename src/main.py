import traceback

from src.utils.app import App
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    app = App()
    try:
        app.start()
    except KeyboardInterrupt:
        logger.warning("Keyboard interrupt - exiting")
    except Exception as ex:
        logger.error(f"Unexpected error: {ex} - {traceback.format_exc()}")
    finally:
        app.stop()


if __name__ == '__main__':
    main()
