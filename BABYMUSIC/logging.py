import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

# This will handle the exception related to 'Peer id invalid' without printing it
try:
    # The code block that may raise the exception
    # Your logic that causes the peer ID error
    pass  # Replace with your actual code

except ValueError as e:
    if "Peer id invalid" in str(e):
        # Handle or ignore the exception without printing
        pass
    else:
        # Re-raise other exceptions that are not handled
        raise

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
