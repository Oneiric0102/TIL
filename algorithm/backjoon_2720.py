units = [25, 10, 5, 1]
coins = [0, 0, 0, 0]

T = int(input())

for i in range(0, T):
    C = int(input())
    for i in range(0, 4):
        coins[i] = C // units[i]
        C = C % units[i]

    for coin in coins:
        print(coin, end=" ")
