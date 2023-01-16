
def Display(No):
    if(No>0):

        No=No-1
        #Head Recursion
        Display(No) # Recursion call here
        print(No)


Display(4)
