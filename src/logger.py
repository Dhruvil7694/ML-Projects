import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

if __name__ == "__main__":
    logging.info("Logging has been set up.")
    logging.info("This is an info message.")
    logging.error("This is an error message.")
    logging.debug("This is a debug message.")
    logging.warning("This is a warning message.")
    logging.critical("This is a critical message.") 