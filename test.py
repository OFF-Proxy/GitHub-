numbers = [1, 2, 4, 7]
for number in numbers:
    mod = number % 2
    if mod == 0:
        print('偶数なのでbreakします')
        break
    else:
        print(str(number) + 'は奇数')
else:
    print('全て奇数でした')
