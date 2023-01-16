from sys import *
import os
import  hashlib


def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)

    return hasher.hexdigest()


def FindDuplicates(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exits=os.path.isdir(path)

    dups={}
    if exits:
        for dirName,subdirs,fileList in os.walk(path):
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                 dups[file_hash]=[path]
        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates Found")

        print("The Follwoing files are iedentical")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print('\t\t%s'% subresult)
        else:
           print("No duplicates files found")

def main():
    print("___Marvellous Infosytem by Piyush Khairnar__")

    print("Appliction name :"+argv[0])

    if (len(argv)!=2):
        print("Error:INvalid number of arguments")
        exit()

    if (argv[1]=="-h") or (argv[1]=="-H"):
        print("This Scropt is used to traverse specific directory and didplay sizes of files")
        exit()

    if (argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:ApplicationName Absolutepath_of_Direactory Extenstion")
        exit()

    try:
        arr={}
        arr=FindDuplicates(argv[1])
        PrintDuplicate(arr)

    except ValueError:
       print("Error :Inavlid dataTpes or input")

if __name__=="__main__":
    main()










