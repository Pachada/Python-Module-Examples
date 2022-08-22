#https://docs.python.org/es/3/howto/logging.html
import logging
from datetime import datetime
import pytz

def timetz(*args):
    return datetime.now(pytz.timezone("America/Mexico_City")).timetuple()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [ %(levelname)s ]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.Formatter.converter = timetz
logger = logging.getLogger(__name__)


logger.info("Better Prints!!")
logger.warning("Mayoeba yabuereru")
logger.error("404 Not Found")

a = 5
b = 0

try:
    result = a / b
except Exception as e:
    logger.exception("Problema")


print("Pero seguimos")