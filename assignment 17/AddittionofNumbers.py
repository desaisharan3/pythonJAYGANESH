def AddittionofNumbers(n):
    total=0 

    for value in n :
        value = int(value)
        total = total +value
    return print (total)

            
def main():
    num=input("enter the numbers here :")
    AddittionofNumbers(num)


if __name__=="__main__":
    main()
    
