from authz.config import Config
from pytz import timezone, utc
from datetime import datetime


def now(name=Config.TIMEZONE):
    tz = timezone(name)
    return datetime.utcnow().replace(tzinfo=utc).astimezone(tz).replace(microsecond=0, tzinfo=None)
