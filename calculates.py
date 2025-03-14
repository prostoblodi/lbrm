import sys
import psutil

data = {}

if not hasattr(psutil, "sensors_temperatures"):
    sys.exit("platform not supported")

def calculate(arguments):
    global data
    temps = psutil.sensors_temperatures()

    if not temps:
        sys.exit("can't read any temperature")

    for name, entries in temps.items():
        data[name] = []
        for entry in entries:
            data[name].append({entry.label: [entry.current, entry.high, entry.critical]})

        if (len(arguments) >= 2 and arguments[1] == '1') or (len(arguments) >= 4 and arguments[3] == '1'): print("** DATA[NAME]:: ", data[name])
    if (len(arguments) >= 2 and arguments[1] == '1') or (len(arguments) >= 4 and arguments[3] == '1'): print("&& DATA::", data)