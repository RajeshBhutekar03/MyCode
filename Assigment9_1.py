import os
def CheckFile(FileName):
    if(os.path.exists(FileName)):
        print("Chcek Whteher file is persent o")
        Data=input()
        fd = open(FileName, 'w')
        fd.write(Data)

    else:
        print("File is not existing")
        return


def main():
    print("Checek for Existing file:")
    Name=input()

    CheckFile(Name)


if __name__=="__main__":
    main()