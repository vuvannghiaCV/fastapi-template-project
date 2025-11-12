import os
import subprocess

from loguru import logger

path_folder_code_python = r"C:\Users\Admin\Desktop\google_drive_check"
logger.info(f"path_folder_code_python = {path_folder_code_python}")


if not os.path.exists(path_folder_code_python):
    logger.info("Thư mục không tồn tại")
    exit()


os.chdir(path_folder_code_python)
# subprocess.run(["black", "code/"], shell=True)
subprocess.run(["black", "./"], shell=True)
