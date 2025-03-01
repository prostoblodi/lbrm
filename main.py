import psutil

f = 0
s = ''
plist = psutil.sensors_temperatures(False)

print(psutil.cpu_stats())
print(psutil.cpu_freq())
print(psutil.cpu_count())
print(psutil.cpu_times())
print(psutil.cpu_percent(1))
print(psutil.cpu_times_percent(1))

print(plist)

for i in plist:
    f += 1
    print(f"INFO {f}: {i} = {plist[i]}")
