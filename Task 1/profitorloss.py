cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))
if sp > cp:
    profit = sp - cp
    print(f"Profit is {profit}.")
elif cp > sp:
    loss = cp - sp
    print(f"Loss is {loss}.")  
else:
    print("No profit no loss.") 