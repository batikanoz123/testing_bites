

class Gratitudes():
    def __init__(self):
        self.gratitudes = []

    def add(self,gratitude):
        self.gratitudes.append(gratitude)
        return self.gratitudes

    def format(self):
        formatted = "Be grateful for : "
        formatted += " ".join(self.gratitudes)
        return formatted
    