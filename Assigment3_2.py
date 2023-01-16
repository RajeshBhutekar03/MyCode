
class FindMax:
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

    def Maximum(self):
     Max = self.Arr[0]
     for i in range(0, self.Size):
      if (self.Arr[i] > Max):
       Max = self.Arr[i]


def main():
    obj = FindMax()
    obj.Accept()

    output=obj.Maximum()
    print("Display Maximum Number from list:",output)

if __name__ == "__main__":
    main()
