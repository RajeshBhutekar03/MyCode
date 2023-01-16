import os


def Delete_File(FileName):
    if (os.path.exists(FileName)):
        fd =os.remove(FileName)




    else:
        print("File is not existing")
        return


def main():
    print("Enter the file name ")
    Name = input()

    Delete_File(Name)


if __name__ == "__main__":
    main()