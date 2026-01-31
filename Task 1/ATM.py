balance = int(input("Enter initial balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
if withdrawal % 100 == 0:
    if withdrawal <= balance:
        balance -= withdrawal
        if balance >=500:
            print(f"Transaction successful. Remaining balance is {balance}.")
        else:
            print(f"Transaction successful. Remaining balance is {balance}. However, your balance is below the minimum required balance of Rs. 500.")
    else:
        print("Insufficient balance for the withdrawal.")
else:
    print("Invalid withdrawal amount. Please enter a multiple of 100.")