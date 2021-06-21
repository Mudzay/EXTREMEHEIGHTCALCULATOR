class Human:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

print("EXTREME HEIGHT CALCULATOR")
x = input("Please input your name: ")
y = input("Please input your height: ")
z = x
x = y
y = z
human1 = Human(y, x)
print("Name: ", human1.name)
print("Height: ", human1.height)