num=int(input("Enter the number:-"))
reverse=int(str(num)[::-1])
if num==reverse:
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not prime number ")
                break
        else:
            print(num,"is a prime palindrome number")
else:
    print("The number is not palindrome")
