def fat(x):
    if x == 0:
        return 1
    return x * fat(x-1)


def sf(x):
    if x == 0:
        return 1
    return fat(x) * sf(x-1)