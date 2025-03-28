import time


def generate_unique_email():
    """Generates a unique email for test users."""
    timestamp = int(time.time())  # Get current timestamp
    return f"testuser_{timestamp}@example.com"


def format_date(day, month, year):
    return f"{str(day).zfill(2)}-{str(month).zfill(2)}-{str(year)}"
