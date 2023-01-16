def main():
    print("Enter Number Here :")
    No=int(input())

    print("Enter Factores are:")
    for i in range(1,int(No/2)+1,1):
        if No % i == 0:
            print(i)

if __name__ == "__main__":
    main()
