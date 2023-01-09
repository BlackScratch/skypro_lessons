
import json
# Преобразование словаря в джейсон
profile = {
    "name": "Алексей",
    "is_online": True,
    "hobbies": {
        1: "beginner",
        2: "middle",
        3: "test",

    }
}

json.dumps(profile)


# Преобразование из джейсон в словарь

raw_json = """{
    "name": "Алексей",
    "is_online": true,
    "hobbies": {
        "1": "beginner",
        "2": "middle",
        "3": "test"

    }
}"""

profile = json.loads(raw_json)
print(type(profile))