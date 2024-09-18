import matplotlib.pyplot as plt


def draw(cost, ema, couple):
    dates = list(range(24))
    # coin
    plt.plot(dates, cost, color=(0.7, 0.1, 0.7), label=couple)
    # EMA
    plt.plot(dates, ema, color=(0.2, 0.1, 0.9), label='EMA')

    plt.legend()
    plt.title(couple)

    plt.savefig(str('graphics/' + couple.replace('/', '') + '.png'))


