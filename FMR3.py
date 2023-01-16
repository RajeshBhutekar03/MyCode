def CheckEvenNumber(No):
    return (No % 2 ==0)

def filterx(Data_Helper,Data):
    Result=[]
    for No in Data:
        if(Data_Helper(No) == True):
            Result.append(No)
    return Result

def main():
    print("Enter Number here")
    iSize=int(input())
    Data_Input=[]
    print("Enter random nuber here")
    for get in range(0,iSize,1):
        iValue=int(input())
        Data_Input.append(iValue)
    Data_filter=filterx(CheckEvenNumber,Data_Input)
    print("Print data after filter :",Data_filter)

if __name__ == "__main__":
     main()