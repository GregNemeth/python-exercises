
string_a = 'dragoon'
string_b = 'dragon'


def near(string_a, string_b):
    counter = 0
    for i in range(len(string_a) + 1):
        new_string = string_a.replace(string_a[counter], '', 1)
        
        counter +=1
        if new_string == string_b:
            break
    return new_string == string_b
  

print(near(string_a, string_b))