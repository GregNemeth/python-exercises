def times_tables(x):
    result = ''
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            result +=f"{i * j}\t"
        result += "\n"
    return result
           
if __name__ == "__main__":      
    x = int(input("please enter a number:"))
    print(times_tables(x))