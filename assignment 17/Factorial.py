#When the loop runs for the first time (i = 1), Python tries to evaluate:
#fact = fact * 1

def factorial():
    num=int(input("enter the number you want :"))
    fact=1
    for i in range (1,num+1):
        fact=fact*i
        print("factoria !!! ",fact)


if __name__=="__main__":
    factorial()


