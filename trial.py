import psutil 

usage = str(psutil.cpu_percent())
# speak("CPU is at : "+usage)
battery = psutil.sensors_battery()
print(battery)
# speak("Battery is at: "+battery.percent)