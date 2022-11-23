# Input : a list of number

# Output : number of even
def number_of_even(list_number):
    even_number = 0

    for x in list_number:
        if x % 2 == 0:
            even_number = even_number + 1
    return even_number


list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('number of even : ', number_of_even(list_number))
