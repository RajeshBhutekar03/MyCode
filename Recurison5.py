
def Display(No):
    if(No>0):
        print(No)
        No=No-1
        #Tile Recursion 
        Display(No) # Recursion call here

Display(4)
