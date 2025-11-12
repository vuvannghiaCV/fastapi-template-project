import os

from loguru import logger

PATH_FILE_CODE = os.path.abspath(__file__)
logger.info(f"PATH_FILE_CODE = {PATH_FILE_CODE}")
PATH_FOLDER_CODE = os.path.dirname(PATH_FILE_CODE)
logger.info(f"PATH_FOLDER_CODE = {PATH_FOLDER_CODE}")


logger.info(f"Loading environment variables...")


PORT = 8002
logger.info(f"PORT = {PORT}")

# DEBUG=False
DEBUG = True
logger.info(f"DEBUG = {DEBUG}")


logger.success(f"Done loading environment variables successfully")
