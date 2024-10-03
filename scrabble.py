joe = '18 22 14 15 16 14 18 10 16 12 18 21 30 10 3 2'
ivy = '10 4 20 6 14 9 28 2 18 10 11 8 21 16 6 12 9 4 11'


def agg_sum(scores):
    return sum(int(s) for s in scores.split(' '))


print('joe=', agg_sum(joe))
print('ivy=', agg_sum(ivy))
