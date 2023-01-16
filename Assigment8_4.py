def main():
    iValue= int(input("Enter a number:"))
    SumNo = 0
    while (iValue > 0):
        Num = iValue % 10
        SumNo = SumNo + Num
        iValue = n / 10
    print("The total sum of digits is:", SumNo)



if __name__=="__main__":
    main()