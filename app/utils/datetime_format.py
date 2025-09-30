from datetime import datetime
from typing import Optional, Union
import pytz
from khayyam import JalaliDatetime

IRAN_TZ = pytz.timezone("Asia/Tehran")
UTC = pytz.UTC

def correct_format(datetime_utc: Union[datetime, str, None]) -> Optional[str]:
    if datetime_utc is None:
        return None

    if isinstance(datetime_utc, str):
        try:
            datetime_utc = datetime.fromisoformat(datetime_utc)
        except Exception:
            from dateutil import parser
            datetime_utc = parser.parse(datetime_utc)

    if not isinstance(datetime_utc, datetime):
        raise ValueError("datetime_utc must be datetime or ISO string")

    if datetime_utc.tzinfo is None:
        datetime_utc = UTC.localize(datetime_utc)
    else:
        datetime_utc = datetime_utc.astimezone(UTC)

    tehran_dt = datetime_utc.astimezone(IRAN_TZ)

    jalali_datetime = JalaliDatetime(tehran_dt).strftime("%Y/%m/%d - %H:%M")

    return jalali_datetime
