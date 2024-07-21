from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from time import sleep
from rich.panel import Panel
import monithor

def perc(value):
    return f"{value:.0f}%"

def mb(value):
    return f"{value >> 20} MB"

def gb(value):
    return f"{value >> 30} GB"

def general_info():
    return f"{monithor.cpu_info()}\n{monithor.load()} "

def disks_table():
    disks_table = Table(expand=True)

    disks_table.add_column("device")
    disks_table.add_column("usage")

    for disk in monithor.disks():
        disk_percent = f"{disk.get("usage").percent:.0f}%"
        disks_table.add_row(disk.get('device'), disk_percent)
    
    return disks_table

def memory_info():
    #total=33548365824, available=28166766592, percent=16.0, 
    #used=4695076864, free=25200201728

    return (f"total {gb(monithor.memory().total)}\n"
            f"available {gb(monithor.memory().available)}\n"
            f"percent {perc(monithor.memory().percent)}\n"
            f"free {gb(monithor.memory().free)}\n"
            f"used {gb(monithor.memory().used)}"
            )

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
        layout["header"].update(Panel(general_info(), title="General"))
        layout["left"].update(Panel(monithor.cpu_percent(), title="CPU"))
        layout["middle"].update(Panel(memory_info(), title="Memory"))
        layout["right"].update(Panel(disks_table(),title="Disk"))
        layout["footer"].update(Panel("Rede...", title="Network"))
        #sleep(1)