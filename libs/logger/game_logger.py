# src/logger/game_logger.py
import logging
from rich.logging import RichHandler

# Configure Rich logger once here
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, show_path=False)]
)

# Create a shared logger instance
logger = logging.getLogger("game_logger")
