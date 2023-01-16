def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 ==0):
            print("Even NUmber :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 !=0):
            print("odd NUmber:",i)

def main():
    DisplayOdd(20)
    DisplayEven(20)

if __name__ == "__main__":
    main()
