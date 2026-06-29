from datetime import date

TARGET_DATE = date(2026, 9, 23)

def get_remaining_days():
    today = date.today()
    return (TARGET_DATE - today).days