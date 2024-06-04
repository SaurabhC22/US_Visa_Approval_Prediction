# SAME CODE FOR ALL THE PROJECTS

import logging
import os

from from_root import from_root
from datetime import datetime  ## This will save the logs with the diff different time stamps. The number of time we run thi logs that many time the different log will be created.

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)