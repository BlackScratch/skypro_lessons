store = [
    {"name":"яблоки","price":"100","availibility":40},
    {"name":"апельсины","price":"200","availibility":20},
    {"name":"Гранаты","price":"400","availibility":5},
]

store = {
    "apples":{"name":"яблоки","price":"100","availibility":40},
    "oranges":{"name":"апельсины","price":"200","availibility":20},
    "granades":{"name":"Гранаты","price":"400","availibility":5},
}

print(store["apples"]["name"])
print(store["oranges"]["availibility"])

# Обращение по ключу
meters = {1:"метр", 0.1:"Колбаса"}
print(meters[1])

# Не повторяющаяся структура словарей
lesson = {
"topic": "Вложенные списк и множества",
"course": {"title": "Питон для веб разработки", "id": "008"},
"students" : [ "Сергей" , "Юлий", "Роман", "Ольга", "Валера" , "Юлия" ],
"speaker": {"name":	"егор","surname": "",	"professions" : ["developer", "instructional designer"]
            }
}
print(lesson["speaker"]["name"], lesson["speaker"]["professions"][1])

print(list(store.keys()))
print(list(store.values()))

stocktaking = {}
for key, value in store.items():
    stocktaking[key] = value['availibility']

print(stocktaking)