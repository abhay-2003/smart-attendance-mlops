import logging
import os



# CREATE LOGS DIRECTORY


os.makedirs("logs", exist_ok=True)

# LOGGER CONFIGURATION


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)


# LOGGER INSTANCE


logger = logging.getLogger("smart_attendance")