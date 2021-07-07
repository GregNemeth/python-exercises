
isbn_no = '978-0-306-40615-'

def isbn_func(isbn_no):
    isbn_formatted = isbn_no.replace('-', '')  #formats the string

    counter = 0       # to keep track of index in isbn_formatted
    digit_12 = 0    # for adding up digits


    for i in isbn_formatted:    # iterate through indexes and adds up digits
        if counter % 2 == 0:
            digit_12 += int(i)
            counter += 1
        else:
            digit_12 += 3 * int(i)
            counter += 1

    final_digit = 10 - (digit_12 % 10)  # calculate the final digit
    isbn_complete = list(isbn_no)      # converts isbn to list so we can use .append
    isbn_complete.append(str(final_digit)) # attach last digit
    var = ''.join(isbn_complete)   # format and print the output
    return var

print(isbn_func(isbn_no))