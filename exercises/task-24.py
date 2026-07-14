def the_richest(accounts):
    """
    Богатейший клиент

    Дан двумерный массив accounts, где accounts[i][j] - это сумма денег i-клиента в j-банке.
    Необходимо вернуть макс. богатство среди всех клиентов:
    - богатство клиента - сумма всех денег этого клиента по всем банкам
    - богатейший клиент - клиент с макс. богатством
    """
    info = {}
    for client, money in enumerate(accounts, start=1):
        if client not in info:
            info[client] = sum(money)
        else:
            info[client] += sum(money)
    res = max(info.items(), key=lambda x: x[1])
    the_richest_client, max_money = res
    print(f'Богатейший клиент: {the_richest_client}, его богатство = {max_money}')
        


rows = int(input())
cols = int(input())

accounts = []
for i in range(rows):
    row = list(map(int, input().split()))
    accounts.append(row)

the_richest(accounts)