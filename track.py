import time
from rich.progress import Progress
import monithor

with Progress() as progress:

    task1 = progress.add_task("[blue]CPU", total=101)
    #task2 = progress.add_task("[green]MEM", total=101)

    while not progress.finished:
        progress.update(task1, =monithor.cpu_percent(raw=True))
        #progress.update(task2, advance=0.3)
        time.sleep(0.02)