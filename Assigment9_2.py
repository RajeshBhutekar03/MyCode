import os

def CheckAndRead(FileName):
    print("Check File is pesrent or not")
    #os.path.exists(FileName)= we check that file is persent or not
    if(os.path.exists(FileName)):
        fd = open(FileName, 'r')
        Data=fd.read()
        print("Print Data from file")
        print(Data)

        fd.close()

    else:
        print("File is not existing")
        return


def main():
    print("Enter FileName is:")
    Name=input()

    CheckAndRead(Name)

if __name__=="__main__":
    main()
