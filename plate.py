

L = [1, 5, 2, 5, 2, 5, 6]
def recur_func(L):
    if len(L) == 0:
        return [], []
    else:
        evens, odds = recur_func(L[1:])
        print(evens, odds)
        if L[0] % 2 == 0:
            evens.append(L[0])
        else:
            odds.append(L[0])
        return evens, odds
print(recur_func(L))