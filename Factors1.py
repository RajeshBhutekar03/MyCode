def main():
    print("Enter Number here:")
    No=int(input())
    for i in range(1,No,1):
        if No % i == 0:
            print(i)

if __name__ == "__main__":
    main()