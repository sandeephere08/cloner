import logging

class NoErrorFilter(logging.Filter):
    def filter(self, record):
        # Suppress specific messages by checking the message
        if 'Peer id invalid' in record.getMessage():
            return False
        return True

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

# Add the filter to prevent logging the 'Peer id invalid' messages
logging.getLogger().addFilter(NoErrorFilter())


logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
