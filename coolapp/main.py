from rich.console import Console
from rich.text import Text

from .messages import get_cool_message


def main() -> None:
    console = Console()
    message = get_cool_message()
    text = Text(message, style="bold magenta")
    console.print(text)


if __name__ == "__main__":
    main()
