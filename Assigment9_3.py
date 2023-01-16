import os
import shutil



def CopyFile():
    print("Copy From Soruce File Name :")
    src_File=input()

    print("Copy to  dist  File Name :")
    dst_File = input()
    cop=shutil.copy(src_File, dst_File)
    print(cop)




def main():
    print("Checek for Copying file:")


    CopyFile()


if __name__=="__main__":
    main()