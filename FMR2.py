def main():
    print("Enter how many number we want from user:")
    iSize=int(input())
    Data_Input=[]
    print("Enter Number here")
    for get in range(0,iSize,1):
        iValue=int(input())
        Data_Input.append(iValue)

    print("Data is :",Data_Input)



if __name__ == "__main__":
     main()
