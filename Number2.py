class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()

    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are : ")
        for i in range(0,self.Size):
            print(self.Arr[i])


    def Sumation(self):
        Toatal=0
        for i in range(0,self.Size):
            Toatal=Toatal + self.Arr[i]
            return Toatal


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()
    obj.Sumation()
if __name__ == "__main__":
    main()