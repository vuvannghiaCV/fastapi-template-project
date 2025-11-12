import os
import shutil

from loguru import logger

PATH_FILE_CODE = os.path.abspath(__file__)
logger.info(f"PATH_FILE_CODE = {os.path.abspath(PATH_FILE_CODE)}")
PATH_FOLDER_CODE = os.path.dirname(PATH_FILE_CODE)
logger.info(f"PATH_FOLDER_CODE = {os.path.abspath(PATH_FOLDER_CODE)}")

PATH_FILE_GITIGNORE = os.path.join(PATH_FOLDER_CODE, "..", ".gitignore")
logger.info(f"PATH_FILE_GITIGNORE = {os.path.abspath(PATH_FILE_GITIGNORE)}")

PATH_FILE_DOCKERIGNORE = os.path.join(
    PATH_FOLDER_CODE, "..", "code", "backend", ".dockerignore"
)
logger.info(f"PATH_FILE_DOCKERIGNORE = {os.path.abspath(PATH_FILE_DOCKERIGNORE)}")

shutil.copy(PATH_FILE_GITIGNORE, PATH_FILE_DOCKERIGNORE)

# with open(PATH_FILE_GITIGNORE, "r", encoding="utf-8") as f:
#     content = f.read()

# with open(PATH_FILE_DOCKERIGNORE, "w", encoding="utf-8") as f:
#     f.write(content)
