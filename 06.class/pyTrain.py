
#
class Service:
    def __init__(self, service, port, configure, hard):
        self.service = service
        self.port = port
        self.configure = configure
        self.hard = hard

    def getConFile(self, path):
        with open(path, "r", encoding="utf8") as file:
            text = file.read()
            print(text)
