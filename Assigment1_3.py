
def Add(A,B):
    Ans=0
    Ans=A+B
    return  Ans


def main():
    print("Enter First Number is:")
    no1=int(input())
    print("Enter Second Number")
    no2=int(input())

    Total=Add(no1,no2)
    print("Addition Two Number is :",Total)




if __name__ == "__main__":
    main()