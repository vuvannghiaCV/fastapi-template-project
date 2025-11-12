import os
import shutil
import subprocess

from loguru import logger

PATH_FILE_CODE = os.path.abspath(__file__)
logger.info(f"PATH_FILE_CODE = {os.path.abspath(PATH_FILE_CODE)}")
PATH_FOLDER_CODE = os.path.dirname(PATH_FILE_CODE)
logger.info(f"PATH_FOLDER_CODE = {os.path.abspath(PATH_FOLDER_CODE)}")

PATH_FOLDER_ROOT = os.path.join(PATH_FOLDER_CODE, "..")
logger.info(f"PATH_FOLDER_ROOT = {os.path.abspath(PATH_FOLDER_ROOT)}")

subprocess.run(["pre-commit", "run", "--all-files"], cwd=PATH_FOLDER_ROOT)
