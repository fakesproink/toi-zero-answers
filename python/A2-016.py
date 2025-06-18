winning_lottery = list(input().split())
bought_lottery = list(input().split())

if winning_lottery == bought_lottery:
    print(1000000)
elif winning_lottery[0] != bought_lottery[0] and winning_lottery[1] == bought_lottery[1]:
    print(100000)
elif winning_lottery[0] == bought_lottery[0] and winning_lottery[1][-3:] == bought_lottery[1][-3:]:
    print(2000)
elif winning_lottery[0] == bought_lottery[0] and winning_lottery[1][-2:] == bought_lottery[1][-2:]:
    print(1000)
elif winning_lottery[0] != bought_lottery[0] and winning_lottery[1][-3:] == bought_lottery[1][-3:]:
    print(200)
elif winning_lottery[0] != bought_lottery[0] and winning_lottery[1][-2:] == bought_lottery[1][-2:]:
    print(100)
elif winning_lottery[0] == bought_lottery[0] and winning_lottery[1] != bought_lottery[1]:
    print(20)
else:
    print(0)
