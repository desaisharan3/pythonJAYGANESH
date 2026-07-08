def NumberofDigits():
    count = 0 
    num=int(input("enter number of digits :"))
    while num > 0 :
        count = count +1 
        num = num // 10 
    print (" the numbe of digits the number has :", count )
        
def main():
    NumberofDigits()
    


if __name__=="__main__":
    main()