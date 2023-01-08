import pickle

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

# команды такие же, как и для json
pickle.dump(layers, open("Layers.pkl", "wb"))

data = dict(pickle.load(open("Layers.pkl", "rb")))
print(data.keys())