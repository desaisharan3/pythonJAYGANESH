def StarPattern():
    rows= int(input("enter the number of rows :"))
    columns=int(input("enter the number of columns:"))
    
    for i in range (rows):
        print("* "*rows, end ="\n")         # dont use another loop instead use *rows 
        

if __name__=="__main__":
    StarPattern()
    
