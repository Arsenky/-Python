duration = int(input())
print('duration =', duration)

if duration//86400 > 0:
    print(duration//86400, 'дн ', end='')
    duration -= (duration // 86400) * 86400
if duration//3600 > 0:
    print(duration//3600, 'час ', end='')
    duration -= (duration // 3600) * 3600
if duration//60 > 0:
    print(duration//60, 'мин ', end='')
    duration -= (duration // 60) * 60
print(duration, 'сек')


