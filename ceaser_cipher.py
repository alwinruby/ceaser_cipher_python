# Input : a list of number

# Output : number of even
# def number_of_even(list_number):
#     even_number = 0
#
#     for x in list_number:
#         if x % 2 == 0:
#             even_number = even_number + 1
#     return even_number
#
#
# list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print('number of even : ', number_of_even(list_number))


org_message = 'I love programming'
# org_message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3

# make all character inside original message upper case
org_message = org_message.upper()
encrypt_message = ''

# print all character
for org_character in org_message:

    if org_character in alphabe:

        org_position = alphabe.find(org_character)
        new_position = org_position + key

        if new_position > (len(alphabe) - 1):

            new_position = new_position - len(alphabe)

        new_character = alphabe[new_position]

    else:

        new_character = org_character

    encrypt_message = encrypt_message + new_character


print(encrypt_message)