def PosorNegv():
    value=(int(input("enter the number :")))
    if value > 0 :
        print("the number is greater than 0 which is why its positive number ") 
    elif value < 0 :
        print("the number is smaller than 0 , hence its negative")
    else:
        print("the value you entered is 0")
if __name__=="__main__":
    PosorNegv()   