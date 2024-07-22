from rich.console import Console
from rich.text import Text

console = Console()
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)

from rich import print
from rich.panel import Panel
from rich.text import Text


bars = chr(9608)*25

panel = Panel(Text(f"86% {bars}", justify="left", style="bold green"))
print(panel)