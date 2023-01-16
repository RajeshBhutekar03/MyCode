
def main():
    print("Enter First number")
    No1= int(input())

    print("Enter Second  number")
    No2 = int(input())

    try:
         Ans= No1 /No2
         print("Division Of Two number:",Ans)

    except ZeroDivisionError:
        print("Inside Division error")

    except ValueError:
        print("Inside value error")

    finally:
        print("Inside finally block")

if __name__ == "__main__":
    main()