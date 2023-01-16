class Demo:
    Value=11
    def __init__(self):
        print("Enter First Number :")
        self.no1=int(input())
        print("Enter Second Number :")
        self.no2=int(input())
    # This instance Method Fun
    def Fun(self):
        Add=self.no1+self.no2
        return Add

    # This instance Method Gun
    def Gun(self):
        sub = self.no1 - self.no2
        return sub


def main():
    obj=Demo()
    out1=obj.Fun()
    print("Addition Two Number is:",out1)
    out2=obj.Gun()
    print("Subtraction of Two number is :",out2)

if __name__ == "__main__":
    main()