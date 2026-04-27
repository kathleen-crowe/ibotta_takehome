from datetime import datetime

def parse_datetime(v):
    if v in ("", None):
        return None
    return datetime.fromisoformat(v.replace(" ", "T"))