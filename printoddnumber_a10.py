def printOddNumbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0: #the only change in odd and even 
            print(i)

printOddNumbers(10)