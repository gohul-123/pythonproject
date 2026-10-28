def calculate_bill(units):
    bill=0
    if units<=100:
        bill=units*1.50
    elif units<=200:
        bill=100*1.50 +(units-100)*2.50
    elif units<500:
        bill=(100*1.50) + (100*2.50)+(units-200)*4.00
    else : 
        bill (100*1.50)+(100*2.50)+(300*4.00) + (units-500)*6.00

    return bill 

n = int(input("enter the number of custormers : "))
for i in range(1,n+1):
    print(f"\n Customer {i}")
    name = input("enter the customer name : ")
    units = float(input("enter the units consumesd : "))
bill=calculate_bill(units)
print("customer name : ",name )
print("units :",units)
print("bill amount : Rs.",round(bill,2))

