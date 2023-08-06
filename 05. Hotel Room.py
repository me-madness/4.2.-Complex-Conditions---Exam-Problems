month = input()
days = int(input())
price_apartment = 0
price_studio = 0
sum = 0



if month == "May" or month == "October":
    price_apartment = days * 65
    if days > 7 and days <= 14:
        sum = 50 - (50 * (0.5/10))
        price_studio = days * sum
    else:
        sum = 50 - (50 * (3/10))
        price_studio = days * sum   
elif month == "June" or month == "September":
    price_apartment = days *  68.70
    if days > 14:
        sum = 75.20 - - (75.20 * (2/10))
        price_studio = days * sum
    else:
        price_studio = days *  75.20    
else:
    price_apartment = days *  77
    price_studio = days *  76
    
if days > 14:
    price_apartment = price_apartment - (price_apartment * (1/10))    

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")