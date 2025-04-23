import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        # logging.FileHandler("app.log"),  # Save logs to a file
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)