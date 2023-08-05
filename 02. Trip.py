money = float(input())
season = input().lower()
place = ''
type_holiday = ''
payment = 0

if season == 'summer':
    type_holiday = 'Camp'
    if money <= 100:
        place = 'Bulgaria'
        payment = money * (3/10)
        # type_holiday = 'Camp'
    elif money <= 1000:
        place = 'Balkans'
        payment = money * (4/10)
        # type_holiday = 'Camp'
    else:
        place = 'Europe' 
        payment = money * (9/10)
        type_holiday = 'Hotel'   
else:
    type_holiday = 'Hotel'
    if money <= 100:
        place = 'Bulgaria'
        payment = money * (7/10)
        # type_holiday = 'Camp'
    elif money <= 1000:
        place = 'Balkans'
        payment = money * (8/10)
        # type_holiday = 'Camp'
    else:
        place = 'Europe' 
        payment = money * (9/10)
        type_holiday = 'Hotel'   
    
print(f"Somewhere in {place}")
print(f"{type_holiday} - {payment:.2f}")
