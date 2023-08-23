def reverse_integer(x: int) -> int:
    diapason = {'max_val': 2 ** 31 - 1, 'min_val': -2 ** 31}
    res = 0
    flag = False
    if x < 0:
        x = abs(x)
        flag = True
    while x != 0:
        res = res * 10 + x % 10
        x = x // 10

        if res > diapason['max_val'] or x < diapason['min_val']:
            return 0
    if flag:
        res = -res
    return res




