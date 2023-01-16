def EvenFctor(No):
    print("Factors are  Even : ")
    for i in range(1, No, 1):
        if No % i== 0:
            if i %2 ==0:
             print(i)

def OddFctor(No):
    print("Factors are  Odd: ")
    for i in range(1, No, 1):
        if No % i== 0:
            if i %2 !=0:
             print(i)

def main():
    EvenFctor(20)
    OddFctor(50)
if __name__ == "__main__":
    main()