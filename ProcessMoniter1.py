import psutil

def DisplayProcess():
    listprocess= []

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo);

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombleProcess):
            pass

    return listprocess






def main():
     print("Marvellous Infosystem: Python Automation & Machine Learing")

     print("Process Moniter")

     listprocess=DisplayProcess()

     for elem in listprocess:
         print(elem)

if __name__=="__main__":
    main()