user_info_1 = {"name":"Алексей","surname":"Егоров", "age":35}
user_info_2 = {"i":"Алексей","f":"Егоров", "yo":35}

user_info_3 = {"i":user_info_1['name'],"f":user_info_1['surname'], "yo":user_info_1['age'] }
print(user_info_3)

user_infos_raw = [
{"name":"Алексей","surname":"Егоров", "age":35},
{"name":"анна","surname":"максимова", "age":38},
{"name":"Поликарп","surname":"Антонов", "age":25}
]
user_infos = []

for user_raw in user_infos_raw:
    user = {
        "i":user_raw['name'],
        "f":user_raw['surname'],
        "yo":user_raw['age']
    }
    user_infos.append(user)

print(user_infos)


coder_info = {
    "name":"Алексей",
    "languages":{
        "java":"beginner",
        "php":"middle",
        "python":"test",
        "go":"none",
    }
}
coder_info_shot = {"name":coder_info["name"],
                   "languages":[],
                   }
for language, level in coder_info['languages'].items():
    print(language,level)
    if level in ("middle", " senior"):
        coder_info_shot["languages"].append(language)

print(coder_info_shot)