def Add(*Values):
    #print(type(Values))
    #print("Number of Agrugment are :",len(Values))
    sum=0
    for no in Values:
        sum =sum + no
        return sum

def main():
    Ans=0
    Ans=Add(10,11,33,43,56)
    print("Addation is :",Ans)


if __name__ == '__main__':
   main()