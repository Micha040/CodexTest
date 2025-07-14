import random

MESSAGES = [
    "You're awesome!",
    "Keep on coding!",
    "Python FTW!",
    "Make it happen!",
    "Stay cool!"
]

def get_cool_message() -> str:
    """Return a random cool message."""
    return random.choice(MESSAGES)
