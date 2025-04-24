# core/logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import os

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 輸出格式
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    # 控制台
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 檔案紀錄（最大 5MB，保留 3 份）
    file_handler = RotatingFileHandler(f"{log_folder}/app.log", maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
