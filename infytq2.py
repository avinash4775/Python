'''
You have x no. of 5 rupee coin and y no. of 1 rupee coin .you have to make  payment of exact amount  such that you will pay
maximum number of 5 rupee coins .If payment amount is greater than availabe amount then return -1 else
find the number of 5 rupee coins and 1 rupee coins needed to pay amount.

'''
five_rupee_coin=int(input("Enter the number of 5 rupee coin:"))
one_rupee_coin=int(input("Enter the number of 1 rupee coin: "))
payment_amount=int(input("Enter the amount of payment:"))
require_five_rupee_coin=0
require_one_rupee_coin=0
available_amount=5*five_rupee_coin+one_rupee_coin

if payment_amount>available_amount:
    print("-1")
else:
    require_five_rupee_coin=payment_amount//5
    if require_five_rupee_coin<=five_rupee_coin:
        require_one_rupee_coin=payment_amount-(5* require_five_rupee_coin)
    else:
        require_five_rupee_coin=five_rupee_coin
        require_one_rupee_coin=payment_amount-(5* require_five_rupee_coin)
    print("No of 5 rupee coin=",require_five_rupee_coin)
    print("No of 1 rupee coin=",require_one_rupee_coin)
