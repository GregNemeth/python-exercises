x = int(input("please enter a number:",))

def times_tables(x):
    print("\n")
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            print(i * j, end="\t")
        print("\n")
            
        

print(times_tables(x))