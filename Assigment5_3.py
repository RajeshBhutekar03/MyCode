class Arithmetic:


    def __init__(self):
        print("Plese Enter Value1  is :")
        self.Value1= int(input())
        print("Plese Enter Value2  is :")
        self.Value2 = int(input())

    def Addition(self):
        Ans = self.Value1 +self.Value2
        return Ans

    def Subtarction(self):
        Ans = self.Value1 - self.Value2
        return Ans

    def Multipaction(self):
        Ans = self.Value1 * self.Value2
        return Ans

    def Divisiable(self):
        Ans = self.Value1 / self.Value2
        return Ans




def main():
    obj = Arithmetic()
    out1 = obj.Addition()
    print("Display Addition Value:", out1)
    out2 = obj.Subtarction()
    print("Display  Subtarction method Value:", out2)
    out3 = obj.Multipaction()
    print("Display Multipaction method Value:", out3)
    out4 = obj.Divisiable()
    print("Display Divisiable method Value:", out4)



if __name__ == "__main__":
    main()
