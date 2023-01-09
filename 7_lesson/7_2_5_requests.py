import time
import requests



response = requests.get("http://sky.pro")

print(response.status_code)

# ---------------------------------Задание - получить три факта о кошках взять ссылку 1)link, создать цикл, в цикле сделать 2)запрос три раза к ссылке
# и перевести с помощью сервиса по ссылке link_to_pirate-------------------------------------------------------------

# 1)Создаём ссылку для запроса link
link = 'https://catfact.ninja/fact'

# link_to_pirate сервис для перевода по ссылке
link_to_pirate="https://api.funtranslations.com/translate/pig-latin.json"

# 2)Создаём цикл для трёх запросов по ссылке
for x in range(3):

    # СОздаём запрос по ссылке и кладём в переменную response2
    response2 = requests.get(link)

    # преобразуем ответ в формат json
    fact = response2.json()
    text_to_add = fact['fact']
    text_to_translate=link_to_pirate
    link_to_pirate = "https://api.funtranslations.com/translate/pirate.json"
    data={
        "text":text_to_add
    }
    request_to_pirate = requests.post(text_to_translate, json=data)
    print(request_to_pirate.text)

    time.sleep(3)


