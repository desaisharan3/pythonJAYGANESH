def NumberDesignX():
    num= int(input("enter the number :"))
    for i in range (1 , num+1 ):
        for j in range (1 , i + 1 ):
            print(j, end ="")
        print()
def main():
    NumberDesignX()



if __name__=="__main__":
    main()
        
        
           
        