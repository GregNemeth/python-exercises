
isbn = '978-0-306-40615-'
isbn_formatted = isbn.replace('-', '')  #formats the string

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
isbn_complete = list(isbn)      # converts isbn to list so we can use .append
isbn_complete.append(str(final_digit)) # attach last digit
print(''.join(isbn_complete))   # format and print the output