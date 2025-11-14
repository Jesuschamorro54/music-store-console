import json
from child_classes.path_manager import get_file_path # funcion para la ruta dinamica

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
<<<<<<< HEAD
        self.file = open(f"C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/stocktaking.json")
=======
        self.file = open(get_file_path("stocktaking.json")) # Dinamico
>>>>>>> joss
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
<<<<<<< HEAD
        self.file = open(f"C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/stocktaking.json", "w")
        self.file = open(f"C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/stocktaking.json", "a+")
=======
        self.file = open(get_file_path("stocktaking.json"), "w") # Dinamico
        self.file = open(get_file_path("stocktaking.json"), "a+") # Dinamico
>>>>>>> joss
        for i in range(len(dictionary)):
            text = json.dumps(dictionary[i])
            self.file.write(f"{text}\n")
