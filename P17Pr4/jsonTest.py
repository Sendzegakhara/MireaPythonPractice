# TODO: работаем с json
import json

'''
data = dict(json.load(open("Config.json", "r", encoding="utf-8")))
print(data)

print(data.keys())
'''

layers = {
    "Layer1":
        {
            "Background": "/Изображения/BigMountains.png",
            "Color": "GRAY",
            "Width": 1920,
            "Height": 1080
        },
    "Layer2":
        {
            "Background": "/image/Mask.png",
            "Color": "WHITE",
            "Width": 720,
            "Height": 480
        }
}
#indent - создаем отступы
#unsure_ascii - убираем обязательную проверку на ascii, что позволяет использовать, например
#русские символы
json.dump(layers, open("Layers.json", 'w', encoding='utf-8'), indent=4, ensure_ascii=False)

users = dict(json.load(open("Layers.json", 'r', encoding="utf-8")))
print(users.keys())