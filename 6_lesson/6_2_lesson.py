file = open('guests.txt', 'r')
file2 = open('guests.txt', 'rb')

#
# content = file.read()
#
# test_string='писька, какашка, жопка'

# for line in file:
#     print(line)
#
# for line in file:
#     print(line)


print(file.read(3))
file.close()
#
# with open('guests.txt', 'rt', encoding='utf-8') as file2:
#     for line in file2:
#         print(line)