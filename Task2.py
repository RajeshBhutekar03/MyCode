import schedule
import time
import datetime


def fun():
    print("Inside fun time is :",datetime.datetime.now())



def main():
    print(" Inside task Scheduler")
    print("currunt time in main is:",datetime.datetime.now())
    schedule.every(1).minutes.do(fun)
    while(True):
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()