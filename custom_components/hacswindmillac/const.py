"""Constants for Windmill AC."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Windmill AC"
DOMAIN = "Windmill_AC"
VERSION = "1.0.0"
PLATFORMS = ["climate"]
UPDATE_INTERVAL = 60
CONF_TOKEN = "token"
BASE_URL = "https://dashboard.windmillair.com"