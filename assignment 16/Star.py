def star():
    
    value=(int(input("enter the number of time you wish the star to appear:" )))
    
    for i in range (value ):
        print("*",end="   ")
if __name__=="__main__":
    star()