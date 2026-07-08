def NumberDesign():
    num= (int(input("enter your desired number :")))
    for i in range (1,num+1):
        for j in range (1,num+1):
            print(j,end="\t")
        print()

def main():
    NumberDesign()
    
if __name__=="__main__":
    main() 