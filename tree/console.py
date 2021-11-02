from rich.console import Console
from rich.theme import Theme

themes = Theme(
    {
        "root": "green",
        "file": "white",
        "dir": "dim cyan",
        "pipe": "white",
    }
)

console = Console(theme=themes)
