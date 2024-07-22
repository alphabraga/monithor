from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from time import sleep
from rich.panel import Panel
from rich.text import Text
import monithor

def perc(value):
    return f"{value:.0f}%"

def mb(value):
    return f"{value >> 20} MB"

def gb(value):
    return f"{value >> 30} GB"

def general_info():
    return f"{monithor.cpu_info()}\n{monithor.load()}\n{monithor.boot_time()}, {monithor.uptime()}"

def disks_table():
    disks_table = Table(expand=True)

    disks_table.add_column("device")
    disks_table.add_column("usage", justify="right", style="green")

    for disk in monithor.disks():
        disk_percent = f"{disk.get("usage").percent:.0f}%"
        disks_table.add_row(disk.get('device'), disk_percent)
    
    return disks_table

def memory_info():
    
    
    mem_table = Table(expand=True)

    mem_table.add_column("Key")
    mem_table.add_column("Value", justify="right", style="green")
    mem_table.add_row("Total", gb(monithor.memory().total))
    mem_table.add_row("%", perc(monithor.memory().percent))
    mem_table.add_row("Aval", gb(monithor.memory().available))
    mem_table.add_row("Free", gb(monithor.memory().free))
    mem_table.add_row("used", gb(monithor.memory().used))

    return mem_table

layout = Layout()

layout.split(
    Layout(name="header", ratio=2, minimum_size=1),
    Layout(name="main", ratio=10, minimum_size=1),
    Layout(name="footer", ratio=4, minimum_size=1),
)

layout["main"].split_row(
    Layout(name="left", ratio=3, minimum_size=1),
    Layout(name="middle", ratio=3, minimum_size=1),
    Layout(name="right", ratio=3, minimum_size=1),
)

with Live(layout, screen=True):
    while True:

        cpu_percent = monithor.cpu_percent(raw=True)
        bars = chr(9608)* int(cpu_percent) 
        cpu_panel = Panel(Text(f"{cpu_percent:.0f}% {bars}", justify="left", style="bold green"), title="CPU")

        mem_percent = monithor.memory().percent
        bars = chr(9608)* int(mem_percent) 
        mem_panel = Panel(Text(f"{mem_percent:.0f}% {bars}", justify="left", style="bold blue"), title="MEM")

        layout["header"].update(Panel(general_info(), title="General"))
        layout["left"].update(cpu_panel)
        layout["middle"].update(mem_panel)
        layout["right"].update(Panel(disks_table(),title="Disk"))
        layout["footer"].update(Panel("Rede...", title="Network"))
        #sleep(1)