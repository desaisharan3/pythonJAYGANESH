def PrimeorNot():
    count = 0

    num= int(input("enter the number :"))
    for i in range (1,num+1):
        if num % i == 0 :
            count = count +1 

    if count >= 2 :
        print(" the entered value is prime number ")
    else :
        print("entered value is not prime number ")

if __name__=="__main__":
    PrimeorNot()
















if __name__=="__main__":
    PrimeorNot()