from logging import DEBUG, ERROR, INFO
from pathlib import Path

import logzero

project_root = Path(__file__).parent.parent.resolve()

logzero.logfile(
    filename=str(project_root.joinpath("logs/debug.log")),
    maxBytes=1024,
    backupCount=1,
    loglevel=DEBUG,
)

logzero.logger.info(f"Project directory: {project_root}")
