'''

Cost of veg plate is 120 and cost of non-veg plate is 150 .cost of delivery for first 3 km is 0 ,next 3 km is 3 rs/km,
otherwise 6 rs/km, find the cost to be paid if a person order the food from the restaurant

'''
plate=input("Enter 'veg' for veg plate and 'non-veg' for non-veg plate:")
distance=int(input("Enter the distance of your house from restaurant:"))
no_of_plate=int(input("Number of plate:"))
cost_of_plate=0
cost_of_delivery=0
dist=0
total_amount=0
if plate=="veg":
    cost_of_plate=120
elif plate=="non-veg":
    cost_of_plate=150
else:
    print("Plate Not availabe")
if distance<=3:
    cost_of_delivery=0
elif distance<=6:
    dist=distance%3
    cost_of_delivery=dist*3
else:
    cost_of_delivery=9+6*(distance-6)
total_amount=no_of_plate*cost_of_plate+cost_of_delivery
print("Total amount is :",total_amount)
