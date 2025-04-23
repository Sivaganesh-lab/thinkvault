from datetime import datetime

def get_utc_timestamp() -> str:
    """Returns current UTC time as a string"""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
