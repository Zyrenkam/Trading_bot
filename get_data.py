import datetime
from CryptoPrice import get_default_retriever
import time
from color_text import *


def get_data(coin_couple):
    # current time in UNIX
    unixtime_stop = time.mktime(datetime.datetime.now().timetuple()) + 3 * 3600

    # need 8.3 days to nearest candle
    indent = 9.3033 * 24 * 60 * 60

    # time to start in UNIX
    unixtime_begin = unixtime_stop - indent

    print(Bcolors.OKCYAN + '================================')
    print(Bcolors.OKCYAN + 'Time begin:', datetime.datetime.utcfromtimestamp(unixtime_begin).strftime('%Y-%m-%d %H:%M:%S'))
    print(Bcolors.OKCYAN + 'Time stop:', datetime.datetime.utcfromtimestamp(unixtime_stop).strftime('%Y-%m-%d %H:%M:%S'))
    print(Bcolors.OKCYAN + '================================' + Bcolors.ENDC)

    coin_couple = coin_couple
    asset, ref_asset = coin_couple.split('/')

    print('Coin 1:', asset)
    print('Coin 2:', ref_asset)

    retriever = get_default_retriever()

    cost_info = []

    for i in range(int(unixtime_begin), int(unixtime_stop), 3600):
        timestamp = int(datetime.datetime.utcfromtimestamp(i).timestamp())
        cost_info.append(retriever.get_closest_price(asset, ref_asset, timestamp).value)

    #print(cost_info)

    ema = []

    for i in range(0, len(cost_info)-200):
        average = 0
        for j in range(i, i+201):
            average += cost_info[j]
        average /= 200
        ema.append(average)

    #print(ema)

    return [cost_info, ema]
