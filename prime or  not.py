num = int(input("Enter your number"))
if num<=1:
    print("The number",num,"is not prime")
else:
    for i in range(2,num):
        if(num%i == 0):
            print("The number",num, "is not prime")
            break
    else:
        print("The number",num, "is prime")
