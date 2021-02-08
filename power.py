def raise_power(base, power):
    if power == 0:
        return 1
    else:
        print(base)
        return base * raise_power(base, power-1)


print(raise_power(5, 3))
