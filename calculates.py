import sys
import psutil

data = {}
debug_mode = False

if not hasattr(psutil, "sensors_temperatures"):
    sys.exit("platform not supported")

def calculate():
    global data
    temps = psutil.sensors_temperatures()

    if not temps:
        sys.exit("can't read any temperature")

    for name, entries in temps.items():
        data[name] = []
        for entry in entries:
            data[name].append({entry.label: [entry.current, entry.high, entry.critical]})

        if debug_mode:
            print(data[name])
