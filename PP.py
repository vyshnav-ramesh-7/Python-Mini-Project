import random
A=int(input("Enter starting range: "))
B=int(input("Enter ending range: "))
if A>B:
    print("Please enter a valid range")
else:
    x=random.randint(A,B)

    def positive_negative():
        if x>0:
            print(x,"is a positive number")
        elif x==0:
            print(x,"is neither positive nor negative")
        else:
            print(x,"is a negative number")

    positive_negative()

            
    def odd_even():
        if x%2==0:
            print(x,"is an even number")
        else:
            print(x,"is an odd number")

    odd_even()

            
    def prime_composite():
        if x==0 or x==1:
            print(x,"is neither prime nor composite")
        elif x<0:
            print(x,"cannot be checked wheather prime or not")
        else:
            f=0
            for i in range (2,x):
                if x%i==0:
                    f=1
                    break
            if f==1:
                print(x,"is a composite number")
            else:
                print(x,"is a prime number")
                
    prime_composite()
