import psutil
import time
import datetime
import cpuinfo


def boot_time():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%y %H:%M:%S")
    return f"System started at {boot_time}"

def uptime():
    boot = datetime.datetime.fromtimestamp(psutil.boot_time())
    current = datetime.datetime.fromtimestamp(time.time())
    delta = current - boot


    return f"Uptime {delta} "

def cpu_info():
    return f"{cpuinfo.get_cpu_info().get('brand_raw')} Cores {psutil.cpu_count()}"

def disks():
    disks = []
    for disk in psutil.disk_partitions():
        if(disk.fstype != "squashfs"):
            disk_usage = psutil.disk_usage(disk.mountpoint)
            disks.append({ "device"  : disk.device, "mountpoint" :disk.mountpoint, "fstype" :disk.fstype, "usage": disk_usage})

    return disks

def cpu_freq():
    return f"CPU Frequancy {psutil.cpu_freq().current:12.0f} Max/Min {psutil.cpu_freq().max:6.0f}/{psutil.cpu_freq().min:6.0f}"

def cpu_percent(raw):
    if raw == True:
        return psutil.cpu_percent()
    
    return f"{psutil.cpu_percent():.0f}%"

def disk_io():
    return psutil.disk_io_counters()

def load():
    load = psutil.getloadavg()
    load_string = f"load 1min {load[0]:.1f} 5min {load[1]:.1f}  15min {load[2]:.1f}"
    return load_string

def sensors_fans():
    psutil.sensors_fans()

def sensors_temperatures():
    return psutil.sensors_temperatures()

def memory():
    return psutil.virtual_memory()

def disk_partitions():
    return psutil.disk_partitions