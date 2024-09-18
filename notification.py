from win11toast import toast


def notification(couple):
    name = couple.replace('/', '')

    toast(str(couple + '\nЗамечено пересечение EMA 200'), 'Нажми, чтобы открыть биржу', on_click=f'https://www.bybit.com/trade/usdt/{name}')
    return 0
