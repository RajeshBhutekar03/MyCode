import math
class Circle:
    PI=3.14

    def __init__(self, Radius,Area,Circumference):
        self.No1=Radius
        self.No2=Area
        self.No3=Circumference

    def Accept(self):
        return self.No1



    def CalculateArea(self):
        return self.No2



    def CalculateCircumference(self):
        return self.No3


    def Display(self):
        return self.No1
        return self.No2
        return self.No3


    def main():
        print("Enter value of Radius")
        Value1=int(input())

        print("Enter value of Area")
        Value2 = int(input())

        print("Enter value of Circumference")
        Value3 = int(input())

        obj=Circle(Value1,Value2,Value3)
        Ans=obj.Accept()

        Ans=obj.CalculateArea()


        Ans=obj.CalculateCircumference()









if __name__ == "__main__":
    main()