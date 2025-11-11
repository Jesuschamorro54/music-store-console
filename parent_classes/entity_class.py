import json

class Entity:
    def __init__(self):
        self.dictionary = None
        self.file = None

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
