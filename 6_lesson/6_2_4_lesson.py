with open('students.txt', encoding='utf-8') as file:
    for student_data in file:
        data = student_data.rstrip('\n').split(':')
        name = data[0]
        language = data[0]

        #---------------Вариант 2------------------
        name2, language2 = student_data.rstrip('\n').split(':')
        print(f'Студент {name} учит язык {language}!')
        print(f'Студент {name2} учит язык {language2}!')

items_count = 0
items_sum = 0

with open('shopping_list.txt', 'r', encoding='utf=8')as file:
    for item_data in file:
        item, quantity, price = item_data.strip('\n').split(':')
        items_count+=1
        items_sum += int(price) * int(quantity)



print(f'В списке {items_count} позиций на сумму {items_sum}')