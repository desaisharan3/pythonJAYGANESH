def FactorialSums():
        num=int(input("enter the number for factorial :"))
        sum=0 



        for i in range (1,num):
                if num % i == 0:
                        sum = sum + i
                        print(sum)
                        
                







if __name__=="__main__" :
        FactorialSums()