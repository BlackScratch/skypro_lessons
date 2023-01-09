with open('guests.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open('write_data.txt', 'wt') as file:
    file.write('hello')

user_language = input('На каком языке вы говорите?')
user_time = input('как давно?')
user_where = input('Где?')

with open('answers.txt', 'w', encoding='utf-8') as file:
    file.write(user_language + '\n')
    file.write(user_time + '\n')
    file.write(user_time + '\n')