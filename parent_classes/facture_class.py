import json


class Facture:
    def __init__(self):
        self.dictionary = None
        self.file = None
        self.stock = None

    #  Write file
    def write_into(self, path, data):
        print(path)
        self.file = open(f"{path}", "a+")
        text = json.dumps(data)
        self.file.write(f"{text}\n")
        self.file.close()

    #  Read file
    def read_file(self, path):
        self.file = open(f"{path}", "r")

        #  Read the file and convert it to a list
        data = self.file.read()
        data = data.split("\n")

        dictionary = []
        for key in range(len(data) - 1):
            dictionary.append(json.loads(data[key]))
        return dictionary

    def update_stock(self, products, doc):
        self.file = open(f"/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/stocktaking.txt")
        data = self.file.read()
        data = data.split("\n")

        # array of dictionary
        dictionary = []

        for key in range(len(data) - 1):
            dictionary.append(json.loads(data[key]))

        # Check if it is a purchase or a sale 
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
        self.file = open(f"/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/stocktaking.txt", "w")
        self.file = open(f"/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/stocktaking.txt", "a+")
        for i in range(len(dictionary)):
            text = json.dumps(dictionary[i])
            self.file.write(f"{text}\n")
