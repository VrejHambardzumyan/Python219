class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        return f"{self.make} {self.model}"
    