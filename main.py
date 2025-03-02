import sys
import psutil

names = []
labels = []
currents = []
highs = []
criticals = []

if not hasattr(psutil, "sensors_temperatures"):
    sys.exit("platform not supported")

temps = psutil.sensors_temperatures()

if not temps:
    sys.exit("can't read any temperature")

for name, entries in temps.items():
    names.append(name)
    for entry in entries:
        labels.append(entry.label)
        currents.append(entry.current)
        highs.append(entry.high)
        criticals.append(entry.critical)
match int(input("Choose - ")):
    case 1:
        print(names)
    case 2:
        print(currents)
    case 3:
        print(highs)
    case 4:
        print(criticals)
    case 5:
        print(names)

