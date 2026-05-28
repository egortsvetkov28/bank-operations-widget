import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename="logs/project.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)
