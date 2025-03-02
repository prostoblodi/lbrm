import sys
import psutil

data = {}
timed_data = []

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
            timed_data.append(entry.label)
            timed_data.append(entry.current)
            timed_data.append(entry.high)
            timed_data.append(entry.critical)
            data[name] = timed_data
    print(data)

