#!/bin/python3

def sockMerchant(n, ar):
    pair_stock_count = 0
    stock_colors = {}
    for i in range(n):
        if stock_colors.get(ar[i], 0) == 1:
            pair_stock_count += 1
            stock_colors[ar[i]] = 0
        else:
            stock_colors[ar[i]] = stock_colors.get(ar[i], 0) + 1
    return pair_stock_count


if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))
