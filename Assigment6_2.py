# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()

class Bank_Account:
    ROI=10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0


    def Display(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())

    def Desposit(self):
        print("Enter your  amount : ")
        self.Amount = int(input())





    def WithDarew(self):


        print("Enter your WithDreaw amount : ")
        self.Amount = int(input())

    def CaluateInterst(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your intial amount : ")
        self.Amount = int(input())






def main():
    User1 = Bank_Account()


    print(User1.ROI+User1.Desposit)
    print(User1.Amount-User1.ROI)





if __name__ == "__main__":
    main()