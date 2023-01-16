import psutil
import os
import time
from sys import *

def ProcessDisplay(log_dir="Marvellous"):
  listprocess=[]
  if not os.path.exists(log_dir):
    try:
      os.mkdir(log_dir)
    except:
        pass
        
  separator="_"* 80
  log_path=os.path.join (log_dir,"MarvellousLog%.log"%(time.ctime()))
  f=open(log_path,'w')
  f.Write(separator +"\n")
  f.Write("MarvellousInfosytem Process Logerr:"+time.ctime()+"\n")
  f.Write(separator +"\n")

  for proc in psutil.process_iter():
    try:
      pinfo=proc.as_dict(attrs=['pid','name','process'])
      vms=proc.memory_info().vms/(1024* 1024)
      pinfo['vms']=vms
      listprocess.append(pinfo);
    except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombleProcess):
        pass

  for element in listprocess:
    f.Write("%s\n"% element)

def main():
  print("----------- Marvellous Infosystems Automations -----------")

  print("Automation script started with name : ",argv[0])

  if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

  if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to perform _____________")
        exit()

  if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ____ number of arguments as")
        print("First Argument as :________")
        print("Second Argument as :________")
        exit()

  try:
      ProcessDisplay(argv[1])

  except ValueErrors:
        print("Invalid datatpes of input")

  except Expactions:
        print("Error: Invalid input")

if __name__=="__main__":
  main()                  