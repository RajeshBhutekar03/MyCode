import os

import filecmp



def CompareFile():
    print("Enter first File Name :")
    FileOne=input()

    print("Enter Second  File Name :")
    FileTwo = input()

    compare = filecmp.cmp(FileOne, FileTwo)

    if compare == True:
        print("The two files are the same.")
    else:
        print("The two files are different.")

def main():
    print("Checek for Copying file:")


    CompareFile()


if __name__=="__main__":
    main()