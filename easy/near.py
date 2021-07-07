
string_a = 'dragoon'
string_b = 'dragon'


def near(string_a, string_b):

    if len(string_b) != len(string_a)-1:
        return False
    else:
        for i in range(len(string_a)):
            if string_a[:i] + string_a[i+1:] == string_b:
                return True
        else:
            return False

print(near(string_a, string_b))