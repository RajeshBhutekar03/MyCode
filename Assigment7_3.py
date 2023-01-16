def DisplayEven():
    print("Enter First NUmber:")
    No=int(input())
    Ans=0
    for i in range(1,No,1):
        if(i % 2==0):
            Ans = Ans + i
            print("Print Even:",Ans)

def Displayodd():
    print("Enter Second NUmber:")
    No = int(input())
    Ans=0
    for i in range(1,No,1):
        if(i % 2!=0):
            Ans=Ans+i
            print("Print odd:",Ans)
def main():
    DisplayEven()
    Displayodd()


if __name__ == "__main__":
        main()