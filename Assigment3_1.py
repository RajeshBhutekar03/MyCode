def SumOfAllNumberFromList():

 list=[]
Get=int (input('Enter five here :'))
for num in range(Get):
    five =int (input('Enter number one by one'))
    list.append(five)
    print("Sum of all Five Number",sum(list))

    if __name__ == "__main__":
        main()