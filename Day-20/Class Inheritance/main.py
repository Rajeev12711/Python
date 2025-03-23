class Animals:
    def __init__(self):
        self.count_eyes= 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animals):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing under water")

    def swim(self):
        print("moving in water")


new = Fish()
new.swim()
new.breathe()
print(new.count_eyes)