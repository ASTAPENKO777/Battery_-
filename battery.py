import psutil

battery = psutil.sensors_battery()

if battery is not None:
    percent = int(battery.percent)
    print(f'Заряд батареї: {percent}%')
else:
    print('Не вдалося отримати інформацію про батарею.')