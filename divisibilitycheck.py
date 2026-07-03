def checkdivisibility(num):
    if num%3==0 and num%5==0:
        print("divisible by both 3 and 5 ")
    elif num%3==0:
        print("divisible by  3  ")
    elif num%5==0:
        print("divisible by  5  ")
    else:
        print("not divisible by both 3 and 5 ")

checkdivisibility(15)


#output-----------------------------------------
#C:\Users\shara\OneDrive\Desktop\python\assignment\assignment9>python divisibilitycheck.py
#divisible by both 3 and 5
