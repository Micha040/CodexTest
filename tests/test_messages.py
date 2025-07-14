from coolapp.messages import get_cool_message, MESSAGES


def test_get_cool_message_returns_known_message():
    message = get_cool_message()
    assert message in MESSAGES
