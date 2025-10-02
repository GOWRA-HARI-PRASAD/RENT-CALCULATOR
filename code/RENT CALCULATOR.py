#total_rent
#food
#water
#elec_charges
#persons 

total_rent=int(input("enter the total rent= "))
food=int(input("enter the total food charges= "))
water=int(input("enter the water charges= "))
elec_charges=int(input("enter the electricity charges= "))
persons=int(input("enter the persons living in room= "))

total_amount=(total_rent+food+water+elec_charges)//persons
print("Each person will pay= ",total_amount)