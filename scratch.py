class Car:

    current_speed = 0

    """__init__ - это Dunder Method"""
    def __init__(self, title, model, max_speed, color):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color

    """CarTitle CarModel engine started!"""
    def start_engine(self):
        print(f"{self.title} {self.model} engine started!")

    """gas --> self.current_speed + 20"""
    def gas(self):
        self.current_speed += 20
        print(self.current_speed)


# Instance Car
bmw = Car("BMW", "x5 e53", 350, "BLACK")
bmw.start_engine()

mercedes = Car("Mercedes", "e63 //AMG", 100, "pink")
mercedes.start_engine()
mercedes.gas()
mercedes.gas()
mercedes.gas()
mercedes.gas()