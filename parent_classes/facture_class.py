import json

class Facture:
    def __init__(self):
        self.dictionary = None
        self.file = None
        self.stock = None

    def write_into(self, path, data):
        print(path)
        self.file = open(f"{path}", "a+")
        text = json.dumps(data)
        self.file.write(f"{text}\n")
        self.file.close()

    def read_file(self, path):
        self.file = open(f"{path}", "r")

        data = self.file.read()
        data = data.split("\n")

        dictionary = []
        for key in range(len(data) - 1):
            dictionary.append(json.loads(data[key]))
        return dictionary

    def update_stock(self, products, doc):
        self.file = open(f"C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/stocktaking.json", "r")
        data = self.file.read()
        data = data.split("\n")

        dictionary = []

        for key in range(len(data) - 1):
            dictionary.append(json.loads(data[key]))

        if doc == "sale":
            for key in products:
                for i in range(len(dictionary)):
                    if dictionary[i]["name"].lower() in key.lower():
                        dictionary[i]["lot"] -= products[key]
        else:
            for key in products:
                for i in range(len(dictionary)):
                    if dictionary[i]["name"].lower() in key.lower():
                        dictionary[i]["lot"] += products[key]
        self.file.close()
        self.file = open(f"C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/stocktaking.json", "w")
        self.file = open(f"C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/stocktaking.json", "a+")
        for i in range(len(dictionary)):
            text = json.dumps(dictionary[i])
            self.file.write(f"{text}\n")
