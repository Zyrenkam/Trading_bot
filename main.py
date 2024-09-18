import get_data as gd
# import graphics
import notification
from color_text import *

# определяем нужные монеты
couples_text = str(input('Coins to check: '))
couples = couples_text.split(', ')

counter = 1
while couples_text.count('/') != len(couples):
    print(Bcolors.WARNING + 'Error, incorrect input' + Bcolors.ENDC)

    couples_text = str(input(f'Try: {counter} \nCoins to check: '))
    couples = couples_text.split(', ')

    counter += 1

# получаем из курсы и цены с уровнями
for couple in couples:
    cost, ema = gd.get_data(couple)

    # проверяем что скользящая пересекла график
    cost_interval = cost[200::]
    flag = False

    for i in range(0, len(ema)-1, 2):
        if (cost_interval[i] > ema[i]) and (cost_interval[i+1] < ema[i+1]):
            flag = True
        elif (cost_interval[i] < ema[i]) and (cost_interval[i+1] > ema[i+1]):
            flag = True
        elif (cost_interval[i] == ema[i]) and (cost_interval[i+1] == ema[i+1]):
            flag = True

    # строим графики, уведомляем
    if flag:
        print(Bcolors.OKGREEN + couple + ' INTERSECTION' + Bcolors.ENDC)
        # graphics.draw(cost_interval, ema, couple)
        notification.notification(couple)
    else:
        print(Bcolors.FAIL + couple + ' NO INTERSECTION' + Bcolors.ENDC)
