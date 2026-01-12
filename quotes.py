from inspirational_quotes import quote as inspirational_quote # type: ignore
from datetime import datetime
import random

DAY_CATEGORY_MAP = {
    "Monday": "happiness",
    "Tuesday": "success",
    "Wednesday": "inspirational",
    "Thursday": "life",
    "Friday": "confidence",
    "Saturday": "funny",
    "Sunday": "motivational"
}


def get_today_category():
    return DAY_CATEGORY_MAP.get(datetime.now().strftime("%A"), "motivational")


def get_quote():
    category = get_today_category()
    q = inspirational_quote()
    return f"🌟 {category.upper()} QUOTE 🌟\n\n{q}"
