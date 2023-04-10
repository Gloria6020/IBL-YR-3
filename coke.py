total_amount=50

while total_amount > 0:
    print("Total amount required: ", total_amount)

    coin = int(input("Enter coin: "))

    if coin in [25,10,5]:
        total_amount -= coin

change= abs(total_amount)

print("change owed: ", change)