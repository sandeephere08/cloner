import logging

# Create a custom filter to suppress pyrogram-specific errors
class NoPyrogramErrorFilter(logging.Filter):
    def filter(self, record):
        # Suppress any messages from pyrogram
        if "Peer id invalid" in record.getMessage():
            return False
        return True

# Set up the basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

# Add the custom filter to suppress the "Peer id invalid" messages
logging.getLogger("pyrogram").addFilter(NoPyrogramErrorFilter())
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

# Function to get a logger
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
