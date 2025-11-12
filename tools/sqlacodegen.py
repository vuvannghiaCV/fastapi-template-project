import os
import shutil
import subprocess
from datetime import datetime

from loguru import logger

PATH_FILE_CODE = os.path.abspath(__file__)
logger.info(f"PATH_FILE_CODE = {os.path.abspath(PATH_FILE_CODE)}")
PATH_FOLDER_CODE = os.path.dirname(PATH_FILE_CODE)
logger.info(f"PATH_FOLDER_CODE = {os.path.abspath(PATH_FOLDER_CODE)}")


FOLDER_DATA = os.path.join(PATH_FOLDER_CODE, "sqlacodegen-data")
FOLDER_BACKUP = os.path.join(PATH_FOLDER_CODE, "sqlacodegen-backup")
MYSQL_ROOT_PASSWORD = "matkhau_cuc_manh_cua_toi"


def ensure_folder(folder_path):
    folder_path = os.path.abspath(folder_path)
    logger.info(f"folder_path: {folder_path}")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f"Created folder: {folder_path}")


PATH_FILE_CODE = os.path.abspath(__file__)
PATH_FOLDER_CODE = os.path.dirname(PATH_FILE_CODE)
logger.info(f"PATH_FILE_CODE = {PATH_FILE_CODE}")
logger.info(f"PATH_FOLDER_CODE = {PATH_FOLDER_CODE}")


logger.info(f"FOLDER_DATA = {FOLDER_DATA}")
ensure_folder(FOLDER_DATA)


logger.info(f"FOLDER_BACKUP = {FOLDER_BACKUP}")
ensure_folder(FOLDER_BACKUP)


logger.info(f"MYSQL_ROOT_PASSWORD = {MYSQL_ROOT_PASSWORD}")


logger.info(f"Environment variables loaded successfully...")


def main():
    for item in os.listdir(FOLDER_DATA):
        source_path = os.path.join(FOLDER_DATA, item)

        now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        logger.info(f"now: {now}")
        destination_path = os.path.join(FOLDER_BACKUP, f"models_{now}.py")

        shutil.move(source_path, destination_path)
        logger.info(f"Moved file: {item}")
    logger.success("Quá trình di chuyển hoàn tất.")

    subprocess.run(
        f"sqlacodegen mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@localhost:3306/python > {FOLDER_DATA}/models.py",
        shell=True,
    )
    logger.success(f"Created file: {FOLDER_DATA}/models.py")


if __name__ == "__main__":
    main()
