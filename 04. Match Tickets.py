budget = float(input())
game_place = input()
group = int(input())
vip = 499.99
normal = 249.99
result = 0
transport = 0
rest_money = 0
not_enough_money = 0

if group >= 1 and group <= 4:
    result = budget * (7.5/10)
elif group >= 5 and group <= 9:
    result = budget * (6/10)
elif group >= 10 and group <= 24:
    result = budget * (5/10)
elif group >= 25 and group <= 49:
    result = budget * (4/10)
else:
    result = budget * (2.5/10)
    
transport = budget - result
   
if game_place == "VIP":
    sum = group * vip
else:
    sum = group * normal

if transport >= sum:
    rest_money = transport - sum                          
    print(f"Yes! You have {rest_money:.2f} leva left.")
else:
    not_enough_money = sum - transport
    print(f"Not enough money! You need {not_enough_money:.2f} leva.")